# 스케줄러(Scheduler) 정리

## 1. 스케줄러란 무엇인가

스케줄러(Scheduler)는 학습 과정에서 **학습률(Learning Rate, LR)**을 동적으로 조정하기 위한 도구이다.

학습 초기에는 큰 학습률로 빠르게 손실을 줄이고, 후반부에는 작은 학습률로 안정적으로 수렴하도록 돕는 역할을 한다.

학습률 조정은 모델의 수렴 속도와 성능에 큰 영향을 주기 때문에, 대부분의 딥러닝 학습 과정에서 스케줄러를 함께 사용한다.

---

## 2. 일반적인 스케줄러

일반적인 스케줄러는 **epoch 또는 iteration(반복 수)**를 기준으로 학습률을 감소시킨다.

이들은 보통 **train 루프 내부(또는 train 이후)**에서 호출된다.

| 스케줄러 | 주요 인자 | 동작 방식 | 호출 시점 |
| --- | --- | --- | --- |
| `StepLR` | `step_size`, `gamma` | 지정한 epoch마다 lr을 `gamma`배로 감소 | train 루프 끝 |
| `MultiStepLR` | `milestones`, `gamma` | 특정 epoch에 도달할 때 lr을 감소 | train 루프 끝 |
| `ExponentialLR` | `gamma` | 매 epoch마다 lr에 `gamma`를 곱함 | train 루프 끝 |
| `CosineAnnealingLR` | `T_max`, `eta_min` | cosine 형태로 lr을 감소시킴 | train 루프 끝 |
| `OneCycleLR`, `CyclicLR` | `max_lr`, `cycle_momentum` 등 | 배치(iteration) 단위로 lr을 주기적으로 변동 | train 루프 내부 |
| `LambdaLR` | `lr_lambda` | 사용자가 정의한 함수로 lr 조정 | train 루프 끝 |

이들 스케줄러는 모두 **학습 과정(train)**을 기준으로 lr을 변경하며,

성능 지표(validation loss 등)는 고려하지 않는다.

---

## 3. ReduceLROnPlateau 스케줄러

`ReduceLROnPlateau`는 다른 스케줄러와 달리 **성능(metric) 기반**으로 학습률을 조정한다.

일정 기간 동안(validation 손실 등) 개선이 없으면 자동으로 학습률을 감소시킨다.

### 주요 인자

| 인자 | 의미 |
| --- | --- |
| `mode` | `'min'`이면 손실이 감소할 때 개선으로 판단, `'max'`이면 정확도 등 증가 기준 |
| `factor` | lr을 감소시킬 비율 (예: `0.1` → lr을 1/10로 줄임) |
| `patience` | 개선이 없을 때 기다릴 epoch 수 |
| `threshold` | 개선으로 간주할 최소 변화량 |

### 사용 예시

```python
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.1, patience=2
)

for epoch in range(num_epochs):
    train(...)
    val_loss = validate(...)
    scheduler.step(val_loss)  # val 결과를 인자로 전달
```

이 스케줄러는 **train이 아니라 validation 단계 이후에 호출**해야 한다.

왜냐하면 학습률을 조정하는 기준이 손실의 감소 여부이기 때문이다.

---

## 4. 결론

| 구분 | 호출 기준 | 인자 | 사용 위치 | 특징 |
| --- | --- | --- | --- | --- |
| 일반 스케줄러 | epoch 또는 iteration 수 | 없음 | train 루프 내부 또는 종료 후 | 단순 주기적 감소 |
| ReduceLROnPlateau | 성능 지표(보통 val_loss) | 필요 | validation 종료 후 | 개선 없을 때 lr 감소 |

**정리하자면**,

- 대부분의 스케줄러는 **train 루프에서 사용**하며, 학습 횟수(epoch)에 따라 lr을 감소시킨다.
- 단 하나의 예외는 **`ReduceLROnPlateau`**로, **validation 성능이 정체될 때** lr을 감소시킨다.
- 따라서 스케줄러의 종류에 따라 `scheduler.step()`의 **호출 시점과 인자**가 다르다는 점을 반드시 구분해야 한다.