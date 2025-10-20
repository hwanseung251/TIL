**Linear Probing**(선형 탐색)과 **Partial Fine-tuning**(부분 미세조정)은 모두 “기존 사전학습(Pretrained)” 모델을 새 태스크에 적응시키는 방법이지만, **접근 방식과 사용 목적**이 뚜렷하게 다르다

### Linear Probing

- 핵심 아이디어
    - 사전학습된 모델의 embedding을 고정하고 새로운 분류기(Linear Layer)만 학습
- 학습 범위
    - 마지막 Linear classifier만 학습
    - 파라미터 0.1 ~ 1% 수준으로 업데이트 됨
- 적용 목적
    - 표현 품질 평가 / 빠른 프로토타이핑

```python
for param in encoder.parameters():
    param.requires_grad = False

classifier = nn.Linear(hidden_dim, num_classes)
```

### Partial Fine-tuning

- 핵심 아이디어
    - 하위 일부 layer(보통 상단 몇개 layer)를 미세조정
- 학습 범위
    - 일부 transformer block까지 학습
    - 파라미터 5 ~ 30% 수준으로 업데이트(선택한 layer에 따라 다름)
- 적용 목적
    - 태스크 특화 모델 구축

```python
for name, param in model.named_parameters():
    if "layer.9" in name or "layer.10" in name or "layer.11" in name:
        param.requires_grad = True
    else:
        param.requires_grad = False
```