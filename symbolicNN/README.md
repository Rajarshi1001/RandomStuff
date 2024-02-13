## Task 3: Build Symbolic Equation from Neural Network Output

In this task, you will develop a program that takes the output of a 2-hidden layer feedforward neural network as input and constructs a symbolic equation representing the network’s output. The goal is to understand and interpret the neural network’s decision-making process through symbolic representation.

The sparse feed forward networks has been trained on the _IRIS_ dataset which consists of 4 features per flower and the network is trained to predict the correct class aong 3 classes from the set of input features. The script trains the model for around `1000` epochs with a learning rate of `0.003` and stores the `state_dict` in `iris_model.pth` file. The trained model is loaded again while inferencng and building the symbolic equation of the model


> In order to the run the program
```py

python3 symbolic.py --x1 {first_value} --x2 {second_value} --x3 {third_value} --x4 {fourth_value}

```
