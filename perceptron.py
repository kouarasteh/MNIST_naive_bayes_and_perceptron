import numpy as np
from Digit_Data_IO import Digit_Data_IO

class Perceptron():

	def __init__(self):
		# open training data file
		self.ddtrain = Digit_Data_IO('digitdata/optdigits-orig_train.txt')
		# open testing data file
		self.ddtest = Digit_Data_IO('digitdata/optdigits-orig_test.txt')
		# randomly generate initial weights
		self.weights = [(np.random.random((32,32))) for x in range(10)]
		# learning rate
		self.k = 1.5
		# 10 perceptrons
		self.class_sums = [0 for x in range(10)]




	def train(self):
		num_loops = 0
		num_incorrect = 0
		self.ddtrain.done = False
		# this loop reads in all training data, and trains the weights
		while self.ddtrain.done is not True:
			self.ddtrain.readNextNum()
			weight_idx = self.ddtrain.answer
			class_weight = self.weights[weight_idx]
			guessed_class = 0
			actual_class = self.ddtrain.answer
			minimum = -10000000000

			for x in range(10):
				for y in range(32):
					for z in range(32):
						self.class_sums[x] += self.ddtrain.img[y][z] * self.weights[x][y][z]
				if self.class_sums[x] > minimum:
					minimum = self.class_sums[x]
					guessed_class = x

			# print("CURRENT DIGIT DATA: ", end='')
			# print()
			# self.printImg()
			# print()
			# print("WEIGHTS BEFORE LEARNING: ", end='')
			# print()
			# self.printWeights(guessed_class)
			# print()
			# class_weight = self.weights[guessed_class]

			if guessed_class != actual_class:
				num_incorrect += 1
				for x in range(32):
					for y in range(32):
						self.weights[guessed_class][x][y] -= self.k * self.ddtrain.img[x][y]
						self.weights[actual_class][x][y] += self.k * self.ddtrain.img[x][y]


			num_loops += 1

			# print("WEIGHTS AFTER LEARNING: ", end='')
			# print()
			# self.printWeights(guessed_class)
			# print('\n')
			# print("GUESSED CLASS: ", guessed_class, end='')
			# print()
			# print("ACTUAL CLASS: ", actual_class, end='')
			# print('\n')
			# self.checkWeights(class_weight, self.weights[guessed_class])

		accuracy = (num_loops - num_incorrect)/num_loops
		print("ACCURACY: ", accuracy)




	def test(self):
		num_correct = 0
		num_loops = 0
		self.ddtest.done = False
		# this loop reads in testing data
		while self.ddtest.done is not True:
			self.ddtest.readNextNum()
			guessed_class = 0
			actual_class = self.ddtest.answer
			minimum = -10000000000

			for x in range(10):
				for y in range(32):
					for z in range(32):
						self.class_sums[x] += self.ddtest.img[y][z] * self.weights[x][y][z]
				if self.class_sums[x] > minimum:
					minimum = self.class_sums[x]
					guessed_class = x


			if guessed_class == actual_class:
				num_correct += 1

			num_loops += 1
			# print("CURRENT DIGIT DATA: ", end='')
			# print()
			# self.printImg()
			# print()
			# # print("WEIGHTS BEFORE LEARNING: ", end='')
			# # print()
			# # self.printWeights(guessed_class)
			# # print()
			# # class_weight = self.weights[guessed_class]


			# # print("WEIGHTS AFTER LEARNING: ", end='')
			# # print()
			# # self.printWeights(guessed_class)
			# # print('\n')
			# print("GUESSED CLASS: ", guessed_class, end='')
			# print()
			# print("ACTUAL CLASS: ", actual_class, end='')
			# print('\n')
			# self.checkWeights(class_weight, self.weights[guessed_class])

		accuracy = num_correct/num_loops
		print("ACCURACY: ", accuracy)



	# print function
	def printWeights(self, idx):
		for x in range(32):
			for y in range(32):
				print("{0:.3f}".format(self.weights[idx][x][y]), end=' ')
			print()



	def printImg(self):
		for x in range(32):
			for y in range (32):
				print(self.ddtrain.img[x][y], end='')
			print()



	def checkWeights(self, array1, array2):
		for x in range(32):
			for y in range(32):
				if array1[x][y] != array2[x][y]:
					print("WEIGHTS ARE DIFFERENT")
					return

		


p1 = Perceptron()
for x in range(5):
	p1.train()
	p1.test()
