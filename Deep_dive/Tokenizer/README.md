### `AutoTokenizer.form_pretrained(’모델’)` vs `~~Tokenizer() + train(files=’말뭉치’)`

| 구분 | 사전 학습된 토크나이저 불러오기 | 새로 토크나이저 학습시키기 |
| --- | --- | --- |
| 목적 | 이미 학습된 모델(BERT, RoBERTa 등)에 맞는 토크나이저 사용 | 내가 가진 말뭉치(nsmc.txt 등)에 맞는 새 토크나이저 생성 |
| 방법 | `AutoTokenizer.from_pretrained("bert-base-multilingual-cased")` | `BertWordPieceTokenizer()` + `train(files=...)` |
| 데이터 | 필요 없음 (Hugging Face에서 가져옴) | 로컬 말뭉치 필요 (`nsmc.txt`) |
| 결과 | BERT에서 쓰던 vocab과 동일한 토크나이저 | `nsmc.txt(말뭉치)`  기반의 새 vocab (`vocab.txt`) 생성됨 |
| 활용 시점 | 모델 fine-tuning 시 | 모델 pre-training 시 또는 도메인 특화 말뭉치에 맞게 튜닝할 때 |
|  |  |  |

즉, 

**`BertWordPieceTokenizer` 등을 가져와서 `train()`을 호출하는 경우**는,

“이미 학습된 토크나이저를 가져오는 것”이 아니라

**직접 새로운 토크나이저를 학습시키는 것**

```python
from tokenizers import BertWordPieceTokenizer

tokenizer = BertWordPieceTokenizer(lowercase=False, strip_accents=False)

tokenizer.train(
    files='nsmc.txt',
    vocab_size=30000,
    min_frequency=2,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
)
```

## 그럼 ‘지식 이전’ 이란?

내가 말뭉치로 새로 임베딩한 것은 `무작위 가중치` 로 임베딩이 되어있음.

이 상황에서 내가 만든 Vocabulary 중 사전학습된 Vocabulary와 같은 **단어**가 있다면 사전 학습된 임베딩을 가져와서 **기존 모델의 언어 지식을 최대한 보존하면서 새 도메인에 빠르게 적응하려는 것임**

- 순서도 중요함! 지식 이전 후 토크나이저 새로 만들면 토큰 ID 매핑이 다 틀어짐

### “단어 기준” 으로 매칭하자

```python
if token in pretrained_tokenizer.vocab:
    pretrained_id = pretrained_tokenizer.convert_tokens_to_ids(token)
    embedding_layer.weight[token_id] = pretrained_embeddings[pretrained_id]
```

- **custom_vocab의 token_id** → 새 토크나이저의 vocab 인덱스
- **pretrained_id** → pretrained 모델에서 그 token의 인덱스

이렇게 해서

> “같은 단어(token)”를 서로 다른 vocab 공간에서 찾아 매칭
> 
> 
> 그 단어의 임베딩 벡터를 “복사”하는 거예요.
> 

즉,

“ID는 다르지만 단어가 같으니, 그 단어의 의미 벡터를 복사해 써라”

라는 논리

### Code 과정

1. 토크나이저 불러오고, 말뭉치를 통해 토크나이저 학습 후 무작위 가중치 행렬로 초기화된 임베딩 레이어 생성
    
    ```python
    import torch
    import torch.nn as nn
    from tokenizers import BertWordPieceTokenizer
    
    vocab_size = 30000
    tokenizer = BertWordPieceTokenizer(lowercase=False, strip_accents=False)
    
    # 1 ~ 2. 사전 처리된 데이터로 토크나이저 학습
    tokenizer.train(
        files='nsmc.txt',
        vocab_size=vocab_size,
        min_frequency=2,
        special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
    )
    
    # 3. 임베딩
    embedding_dim = 768
    # 무작위 가중치 행렬로 초기화된 임베딩 레이어 생성
    embedding_layer = nn.Embedding(
        num_embeddings=vocab_size, embedding_dim=embedding_dim
    )
    ```
    

2. 사전 학습 모델 로드
    
    ```python
    # transformers 라이브러리에서 제공하는 사전 학습된 모델과 토크나이저를 불러오기 위한 모듈
    # AutoTokenizer: 다양한 모델에 맞는 토크나이저를 자동으로 불러오는 클래스
    # AutoModel: 다양한 모델에 맞는 사전 학습된 모델을 자동으로 불러오는 클래스
    from transformers import AutoTokenizer, AutoModel
    
    # (Pre-trained Model) 로드 -> klue/bert-base
    pretrained_model_name = "klue/bert-base"
    # from_pretrained 메서드는 모델 이름을 입력받아 해당 모델에 맞는 토크나이저를 자동으로 불러옴
    pretrained_tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
    pretrained_model = AutoModel.from_pretrained(pretrained_model_name)
    
    # klue/bert-base의 임베딩 레이어에서 가중치 행렬(임베딩 벡터들)을 추출
    pretrained_embeddings = pretrained_model.embeddings.word_embeddings.weight
    
    # 장치 설정 (GPU 사용 가능 시 GPU 사용)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # 디바이스 이동
    embedding_layer = embedding_layer.to(device)
    pretrained_embeddings = pretrained_embeddings.to(device)
    
    ```
    

3. 지식 이전
    
    ```python
    from tqdm import tqdm  # 진행 상황을 시각적으로 보여주는 라이브러리
    
    # get_vocab(): 토크나이저의 단어 사전을 딕셔너리 형태로 반환
    custom_vocab = tokenizer.get_vocab()
    
    # 공통 단어에 대해 Pre-trained 벡터를 복사
    copied_count = 0
    # no_grad(): 이 블록 내에서는 그래디언트 계산을 하지 않아 메모리를 효율적으로 사용
    with torch.no_grad():
        # custom_vocab의 각 단어에 대해 반복
        # tqdm: 진행 상황을 시각적으로 보여줌
        for token, token_id in tqdm(custom_vocab.items()):
            # klue/bert-base의 토크나이저는 BertWordPieceTokenizer와 동일한 구조를 사용
            # 해당 단어가 사전 학습된 토크나이저의 단어 사전에 존재하는지 확인
            if token in pretrained_tokenizer.vocab:
                # 단어에 해당하는 ID 추출
                pretrained_id = pretrained_tokenizer.convert_tokens_to_ids(token)
                # 임베딩 레이어의 가중치 행렬에서 해당 단어의 벡터를 복사
                embedding_layer.weight[token_id] = pretrained_embeddings[
                    pretrained_id
                ]
                # 복사된 단어 수 증가
                copied_count += 1
    
    print(
        f"총 {len(custom_vocab)}개의 단어 중 {copied_count}개의 벡터를 성공적으로 이식했습니다."
    )
    '''
    100%|██████████| 30000/30000 [11:45<00:00, 42.50it/s]총 30000개의 단어 중 9084개의 벡터를 성공적으로 이식했습니다.
    '''
    ```