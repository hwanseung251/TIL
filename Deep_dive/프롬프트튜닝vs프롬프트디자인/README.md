## 핵심 차이 요약표

| 구분 | **프롬프트 디자인 (Prompt Design)** | **프롬프트 튜닝 (Prompt Tuning)** |
| --- | --- | --- |
| **의미** | 사람이 직접 문장을 설계해 모델의 출력을 유도 | 모델이 “좋은 프롬프트”를 **학습**하도록 하는 방법 |
| **대상** | 인간이 만든 자연어 프롬프트 | 학습 가능한 벡터(임베딩) 형태의 가상 토큰 |
| **형태** | “너는 과학 선생님이야. 이 문장을 요약해줘.” 같은 문장 | 모델 내부의 “가짜 토큰(soft prompt)” 벡터 |
| **목적** | **Prompt Engineering** — 모델을 잘 다루기 | **Parameter-efficient Fine-tuning** — 모델 일부만 학습 |
| **학습 여부** | 없음 (사람이 작성) | 있음 (학습 과정에서 최적화됨) |
| **대표 적용 방식** | In-context Learning, Chain-of-Thought 등 | Prefix-tuning, P-tuning, LoRA + Prompt tuning 등 |
| **비유** | 사람이 “질문 잘 던지는 법”을 배우는 것 | 모델이 “어떤 질문이 잘 통하는지” 스스로 배우는 것 |

---

## 예시로 구

| 상황 | 해당 개념 |
| --- | --- |
| “GPT에게 요약을 잘 시키려면, ‘한 문장으로 요약해줘’ 대신 ‘핵심 내용을 한 줄로 요약해줘’가 더 낫네!” | → **프롬프트 디자인** |
| “BERT 모델 앞단에 10개의 가상 토큰을 붙이고, 학습을 통해 이 토큰의 벡터를 최적화했더니 downstream task 성능이 올랐어.” | → **프롬프트 튜닝** |

---

## 기술적으로 보면

- **프롬프트 디자인**
    - 모델의 파라미터는 **고정**되어 있음.
    - 사용자는 **언어적 힌트(prompt)**를 설계함.
    - 즉, “**문장 설계 기술**”이 중심.
- **프롬프트 튜닝**
    - 모델의 파라미터는 거의 고정하지만,
    - **입력 앞단의 프롬프트 임베딩만 학습**함.
    - 즉, “**모델 학습 기술**”이 중심.
    - 구현 방법 (파이토치 + 트랜스포머 예시)
        
        ```python
        from transformers import T5ForConditionalGeneration, T5Tokenizer
        from peft import PromptTuningConfig, get_peft_model, TaskType
        
        # 1. 기본 모델 로드
        model_name = "t5-small"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        
        # 2. Prompt Tuning 설정
        peft_config = PromptTuningConfig(
            task_type=TaskType.SEQ_2_SEQ_LM,
            num_virtual_tokens=20,   # soft prompt 개수
            prompt_tuning_init="TEXT",  # 초기화 방법 ("TEXT" 또는 "RANDOM")
            prompt_tuning_init_text="Classify the sentiment of this text:"
        )
        
        # 3. 모델 래핑
        model = get_peft_model(model, peft_config)
        
        # 4. 학습 루프에서는 soft prompt 파라미터만 업데이트
        model.print_trainable_parameters()
        # 출력 예: trainable params: 0.1% of total parameters
        
        ```
        

---

## 정리

> 프롬프트 디자인 = 사람이 “프롬프트를 잘 짜는 기술”
> 
> 
>  **프롬프트 튜닝** = 모델이 “프롬프트를 스스로 배우는 기술”
>