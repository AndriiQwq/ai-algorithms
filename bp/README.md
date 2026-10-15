# Backpropagation Algorithm for Solving XOR Problems

## Overview
This project implements a neural network to solve **XOR** and other logical problems using the **Backpropagation Algorithm**.  
The model supports flexible configurations, allowing you to set:

- Number and size of layers
- Activation functions for each layer
- Training parameters (epochs, learning rate, momentum)
- Logging options

Configuration is managed via a config file, for example:

```ini
[Training]
epoch_count = 200
learning_rate = 0.1
momentum = 0.9
use_momentum = True

[Logging]
enable_logging = True
log_level = INFO

[Network]
layer_sizes = 2,4,1
activations = Tanh,Tanh
```

### Key Features:
- **Multiple Layer Support**: Flexible architecture, set any number and size of layers.
- **Customizable Configuration**: All main parameters are set in the config file.
- **Integrated Logger**: Training and model operations are logged for easier debugging and analysis.
- **XOR Problem Solving**: The trained model achieves high accuracy on XOR and similar logical tasks.

### Usage Examples: 

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/6af35b4d-6626-4de5-8e5d-f6e0f7c4d9f6" />

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/4e144784-6a58-476a-ba8c-67a6976fee2b" />

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/99882db8-da94-4966-a939-1bf01a193606" />

```md
           CURRENT MODEL INFO
==================================================
Total layers: 3

Layer Details:
  Layer 1: 2 -> 4 (Tanh)
  Layer 2: 4 -> 4 (Tanh)
  Layer 3: 4 -> 1 (Tanh)

Configuration:
  Learning rate: 0.1
  Momentum: 0.9
  Use momentum: True
  Epochs: 500

Activations:
  Layer 2: Tanh
  Layer 3: Tanh
  Layer 4: Tanh
==================================================
Do you want to test the model? (y/n): y
-------------------------------------------------
Input set: [[0 0]], Label: 0 Correct prediction: 0.0006 == 0
Input set: [[0 1]], Label: 1 Correct prediction: 0.9970 == 1
Input set: [[1 0]], Label: 1 Correct prediction: 0.9864 == 1
Input set: [[1 1]], Label: 0 Correct prediction: 0.0018 == 0
-------------------------------------------------
Correct model
Do you want to save the model? (y/n): y
Enter model name (default is default generated bc0570b2-5ff2-431b-8afd-6636300bc0af.npy):

C:\Users\Andrii\Desktop\Repositories\Backpropagation-algoritmus\src>python main.py
Show training visualization? (y/n): y

==================================================
           CURRENT MODEL INFO
==================================================
Total layers: 3

Layer Details:
  Layer 1: 2 -> 4 (Tanh)
  Layer 2: 4 -> 4 (Tanh)
  Layer 3: 4 -> 1 (Tanh)

Configuration:
  Learning rate: 0.1
  Momentum: 0.9
  Use momentum: True
  Epochs: 500

Activations:
  Layer 2: Tanh
  Layer 3: Tanh
  Layer 4: Tanh
==================================================
Do you want to test the model? (y/n): y
-------------------------------------------------
Input set: [[0 0]], Label: 0 Correct prediction: 0.0000 == 0
Input set: [[0 1]], Label: 1 Correct prediction: 0.9936 == 1
Input set: [[1 0]], Label: 1 Correct prediction: 0.9937 == 1
Input set: [[1 1]], Label: 0 Correct prediction: 0.0001 == 0
-------------------------------------------------
Correct model
Do you want to save the model? (y/n): y
Enter model name (default is default generated b3b49ce7-55c4-496d-9fb7-c4345be93268.npy):

C:\Users\Andrii\Desktop\Repositories\Backpropagation-algoritmus\src>python main.py
Show training visualization? (y/n): y

==================================================
           CURRENT MODEL INFO
==================================================
Total layers: 3

Layer Details:
  Layer 1: 2 -> 4 (Tanh)
  Layer 2: 4 -> 4 (Tanh)
  Layer 3: 4 -> 1 (Tanh)

Configuration:
  Learning rate: 0.1
  Momentum: 0.9
  Use momentum: True
  Epochs: 500

Activations:
  Layer 2: Tanh
  Layer 3: Tanh
  Layer 4: Tanh
==================================================
Do you want to test the model? (y/n): y
-------------------------------------------------
Input set: [[0 0]], Label: 0 Correct prediction: -0.0085 == 0
Input set: [[0 1]], Label: 1 Correct prediction: 0.9784 == 1
Input set: [[1 0]], Label: 1 Correct prediction: 0.9804 == 1
Input set: [[1 1]], Label: 0 Correct prediction: 0.0003 == 0
-------------------------------------------------
Correct model
Do you want to save the model? (y/n): n
```

## Conclusion
This backpropagation neural network efficiently solves logical problems like AND, OR, XOR and more.  
Optimal performance is achieved with proper configuration and logging helps
