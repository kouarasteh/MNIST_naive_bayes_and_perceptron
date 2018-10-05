# MNIST Classifier 

# Naive Bayes Implementation

Our implementation for the Naïve Bayes Classifier was structurally intuitive using primarily python 2d lists and
separate functions for training, testing, and several for formatted printing. We had a Digit_Data_IO class that
parses through the digit data provided for training and testing and feeds it into our train (and test) functions in
naive_bayes.py as a single 32x32 matrix of 1’s and 0’s. Once we have this digit data, we begin training our
classifier by iterating through each cell in the 32x32 matrix and incrementing the respective probability
matrices for each class in accordance with the given probability equation. Upon iterating through all the 32x32
matrices, we are finished with training our model and proceed to test. Given these calculated pixel
probabilities, we can calculate the priors, MAP rule, and test.
We then begin testing using another instance of Digit_Data_IO class to parse the testing data samples and
begin MAP classification. We then use the math library to perform the log of the MAP classification quantity to
avoid underflow. Our default hyperparameters included randomized start values, no bias, and a Laplace
smoothing value of 0.01.

![Alt text](mp3/confmat.png?raw=true "Title")
# Perceptron Implementation

Our Perceptron Classifier used the same Digit_Data_IO to read in the text files. We used an array of
randomly generated weight matrices, a learning rate, and another array of sums to represent our 10
perceptrons. We trained our Perceptron by taking in every input, multiplying it by the weight for that given
classification, and adding them all together. This is then stored in the correct index based on the classification
and used to determine whether a weight matrix needs to be updated or not. If our predicted classification was
not the correct classification, we weaken the weighting of the incorrect classification, and reinforce the
weighting of the correct classification. We test our Perceptron by simply using the trained weight matrices to
classify the provided test digit data. Our learning rate was set to .01 and performed 20 epochs.

# Parameter Tuning | Perceptron

# Bias
We introduced our Perceptron to a bias of +1 and we noticed a significant decrease in both training and
testing accuracy. Before adding a +1 bias, our Perceptron was performing classifications with about 89%
accuracy (in testing, not training). After adding a bias of +1, our classification accuracy dropped to around 65%
in testing.

# Zero-Filled Initial Weight Matrix vs. Random Initial Weight Matrix
We ran our Perceptron with an empty weight matrix and a random weight matrix and we noticed that an
empty initial weight matrix performed significantly better with an average performance increase of about
4-5% in training and 5-6% in testing.

# Number of Epochs
We noticed that an epoch parameter of ~20 was ideal to prove convergence, given a learning rate of .001. We
tried as many as 200 epochs, and no significant improvement in accuracy was seen beyond 20 epochs. With a
faster learning rate, we needed less epochs, and with a slower learning rate, we needed more epochs.
However, we noticed that if a learning rate is too slow, our Perceptron would converge on a local minimum
and never exceeded ~75% accuracy.
