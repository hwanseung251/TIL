# Hugging Face 개요

Hugging Face는 **최신 NLP(자연어 처리) 딥러닝 기술을 누구나 쉽게 사용할 수 있도록 도와주는 플랫폼이자 라이브러리**입니다.

복잡한 모델을 직접 학습하지 않아도, 미리 학습된 모델을 가져와 **단 몇 줄의 코드로 바로 활용**할 수 있다는 점이 핵심입니다.

---

## 구성 요소

### 1. **Models**

- 전 세계 개발자들이 미리 학습시켜둔 수많은 AI 모델이 공개되어 있음.
- 예: BERT, RoBERTa, GPT, T5 등
- 각 모델은 특정 작업(분류, 요약, 번역 등)에 맞게 사전학습되어 있음.

### 2. **Tokenizer**

- 텍스트를 **모델이 이해할 수 있는 정수 형태(input_ids)** 로 변환하는 역할.
- 모델마다 고유한 토크나이저가 존재하며, 반드시 짝을 맞춰 사용해야 함.
- 예: BERT 모델 ↔ BERT 전용 토크나이저

> 핵심 규칙:
> 
> 
> 모델과 토크나이저는 **항상 짝꿍**이어야 함.
> 
> (`AutoTokenizer`로 모델 이름만 알려주면 자동으로 해당 토크나이저를 찾아줌.)
> 

### 3. **Transformers**

- Hugging Face의 핵심 라이브러리로,
    
    모델과 토크나이저를 **파이썬 단 몇 줄로 손쉽게 사용할 수 있게 해주는 도구**.
    
- 예시 코드:
    
    ```python
    # !pip install transformers
    from transformers import AutoTokenizer
    
    # 'klue/bert-base'라는 책(모델)에 맞는 단어 사전을 빌려옵니다.
    tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
    ```
    

---

## 토크나이저 동작 과정

1. **텍스트 입력**
    
    ```python
    text = "안녕하세요. 이 실습은 허깅페이스 토크나이저 사용법을 익히는 좋은 예제입니다." 
    
    # 토크나이저로 문장을 인코딩합니다.
    encoded_input = tokenizer(text) 
    ```
    
    - 반환값은 **딕셔너리 형태**
        
        ```python
        {'input_ids': [2, 5891, 2205, 5971, 18, 1504, 10256, 2073, 1905, 2186, 15092, 9157, 7461, 2190, 20650, 2069, 9754, 2259, 1560, 2073, 1439, 2021, 12190, 18, 3], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, ...
        ```
        
2. **input_ids**
    - 텍스트를 **토큰 단위로 나눈 뒤 정수로 인코딩**한 결과
    - 모델은 이 정수 시퀀스를 입력으로 받아 처리함.
3. **서브워드(Subword) 토크나이징**
    
    인코딩된 ‘input_ids’를 다시 토큰으로 변환해 보면… `tokenizer.convert_ids_to_tokens`
    
    ```python
    # 정수 ID를 다시 토큰으로 변환합니다.
    tokens = tokenizer.convert_ids_to_tokens(encoded_input['input_ids'])
    
    print(tokens)
    # ['[CLS]', '안녕', '##하', '##세요', '.', ..., '[SEP]']
    ```
    
    - `##세요`, `##다`  이렇게 ## 이 된 단어를 볼 수 있는데..
    - 사전에 없는 단어(OOV, Out-Of-Vocabulary)를 더 작은 의미 단위로 쪼개어 처리.
    - 덕분에 새로운 단어도 의미를 일부 유추할 수 있음.

> **OOV (Out Of Vocabulary):**
> 
> 
> 학습 시 단어 사전에 없는 새로운 단어.
> 
> 기존에는 `[UNK]` 토큰으로 처리했지만,
> 
> 서브워드 분할을 통해 의미를 보존할 수 있게 되었음.
> 

---

## 임베딩 (Embedding)

- 인코딩된 `input_ids`를 모델에 입력하면,
    
    모델은 각 단어를 **고차원 벡터(embedding vector)** 로 변환함.
    
    ```python
    from transformers import AutoModel
    
    # 토크나이저와 '똑같은 이름'의 모델을 빌려옵니다. 짝꿍!
    model = AutoModel.from_pretrained("klue/bert-base") 
    
    # 1. 인코딩 시, 결과를 PyTorch 텐서 형태로 반환하도록 옵션을 추가합니다.
    encoded_input = tokenizer(text, return_tensors='pt')
    
    # 2. 인코딩된 딕셔너리를 모델에 통째로 전달합니다. (**)
    output = model(**encoded_input)
    
    # 3. 모델의 여러 출력 중, 'last_hidden_state'가 우리가 원하는 최종 임베딩 벡터입니다.
    embedding_vector = output.last_hidden_state
    ```
    
- `last_hidden_state`:
    
    입력된 각 토큰에 대응하는 **최종 임베딩 벡터**를 의미함.
    
- 임베딩은 **단어 간의 의미적 관계를 수치화**한 표현이며,
    
    유사한 의미의 단어는 벡터 공간에서 **가까운 위치**에 존재함.
    

> 예시:
> 
> 
> `king - man + woman ≈ queen`
> 

```python
print(embedding_vector.shape) 

# torch.Size([1, 25, 768])
```

- `1` (Batch Size): 한 번에 처리한 문장의 개수
- `26` (Sequence Length): 문장이 토큰화된 후의 토큰 개수 ([CLS] … [SEP])
- `768` (Hidden Size): 하나의 토큰을 표현하는 벡터의 차원(숫자의 개수)

→ 즉 1문장을 26개의 토큰으로 나눴고 토큰은 각각 768개의 숫자로 이루어진 의미 벡터

---

## 정리
| 구성요소 | 역할 | 예시 |
| --- | --- | --- |
| **Models** | 사전학습된 AI 모델 | BERT, GPT, T5 |
| **Tokenizer** | 텍스트를 토큰/정수로 변환 | AutoTokenizer |
| **Transformers** | 모델·토크나이저를 쉽게 사용하도록 지원 | from transformers import AutoModel |
| **Embedding** | 단어를 의미 벡터로 변환 | last_hidden_state |