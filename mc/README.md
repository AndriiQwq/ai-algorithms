MNIST classifier on PyTorch. Modular code, config support, training and visualization included.

# Usage Examples
```md
optimizer(sgd, sgd_momentum, adam) = adam 
epoch_count = 200 
train_batch_size = 64 
test_batch_size = 64 
learning_rate = 0.001
```

Input layer: 
- Input: 784 neurons  
- Output: 256 neurons 
- Activation: ReLU

Hidden 1 layer: 
- 256 neurons  
- Output: 128 neurons 
- Activation: ReLU

Hidden Layer 2: 
- 128 neurons  
- Output: 64 neurons 
- Activation: ReLU

Output layer: 
- 64 
- Output: 10 

Output: 
- Success rate: 98.6

<img width="823" height="431" alt="image" src="https://github.com/user-attachments/assets/7f8dedd4-7615-495f-9900-aa8f3f5a2815" />

---
      
Another Example: 

```md
optimizer(sgd, sgd_momentum, adam) = adam 
epoch_count = 200 
train_batch_size = 64 
test_batch_size = 64 
learning_rate = 0.001 
```

Vstupná vrstva: 
- Vstup: 784 neurónov  
- Výstup: 256 neurónov 
- Aktivácia: ReLU 

Skrytá 1 vrstva: 
- Vstup: 256 neurónov  
- Výstup: 64 neurónov 
- Aktivácia: ReLU 

Výstupná vrstva: 
- Vstup: 64 
- Výstup: 10

Output: 

<img width="583" height="640" alt="image" src="https://github.com/user-attachments/assets/9011482d-fb8e-4796-b5a9-0044d9ad45a7" />

