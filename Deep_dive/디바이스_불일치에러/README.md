<aside>
⚠️

RuntimeError: Input type (torch.FloatTensor) and weight type (torch.cuda.FloatTensor) should be the same or input should be a MKLDNN tensor and weight is a dense tensor

</aside>

- `net` 은 GPU에 올라가 있지만, 배치(input, labels)를 매 루프마다 CPU 텐서로 다시 덮어쓰고 있어서 터지는 것!
    - 루프 밖에서 한 번 to(device) 한 줄은 의미 없고 아래처럼 루프 안에서 매 배치를 디바이스로 옮기도록 수정해야함

**before**

```python
for epoch in range(2):
    net.train()
    running_loss = 0.0
    for i, (inputs, labels) in enumerate(trainloader):
				inputs, labels = data

        optimizer.zero_grad()
        outputs = net(inputs)          # 이제 inputs/weights 모두 같은 디바이스
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:
            print(f'[{epoch+1}, {i+1:5d}] loss: {running_loss/2000:.3f}')
            running_loss = 0.0

print('Finished Training')
```

**after**

```python
# Training Loop (핵심: 배치마다 .to(device))
for epoch in range(2):
    net.train()
    running_loss = 0.0
    for i, (inputs, labels) in enumerate(trainloader):
        inputs = inputs.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()
        outputs = net(inputs)          # 이제 inputs/weights 모두 같은 디바이스
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:
            print(f'[{epoch+1}, {i+1:5d}] loss: {running_loss/2000:.3f}')
            running_loss = 0.0

print('Finished Training')
```