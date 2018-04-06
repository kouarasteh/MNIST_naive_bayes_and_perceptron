import numpy as np
from Digit_Data_IO import Digit_Data_IO
from copy import deepcopy
import math
class NaiveBayes():

	def __init__(self):
		self.ddtrain = Digit_Data_IO('digitdata\optdigits-orig_train.txt')
		self.ddtest = Digit_Data_IO('digitdata\optdigits-orig_test.txt')
		#set of training probabilities for all 10 classes
		self.probs = np.zeros((10,32,32), float, 'C')
		#number of training samples of each class
		self.numSamples = [0 for x in range(10)]
		#total number of training samples
		self.totSamples = 0
		#prior probs for each class
		self.priors = [0 for x in range(10)]
		#laplace smoothing value
		self.k = 0.01
		#list of map classifications for each testing image
		self.maps = []
		#number of training samples of each class
		self.numTestSamples = [0 for x in range(10)]
		#accuracy of classification for each class
		self.probSucc = [0 for x in range(10)]
		#confusion matrix, where r is correct classification and c is guess
		self.confMat = [[0 for x in range(10)] for y in range(10)]
		#best and worst guesses for each class
		self.bestWorstTokens = [(np.zeros((10,32,32), float, 'C'),np.zeros((10,32,32), float, 'C')) for x in range(10)]
		# max and min posterior probabilities for each class
		self.maxMinPostProbs = [(-10000000,100000000) for x in range(10)]

	def train(self):
		#loop to add counts for each pixel for each class
		while self.ddtrain.done is not True:
			self.ddtrain.readNextNum()
			self.numSamples[self.ddtrain.answer] += 1
			for line in range(32):
				for x in range(32):
					#if pixel is colored, add to count for the given class for that pixel
					if self.ddtrain.img[line][x] == 1:
						self.probs[self.ddtrain.answer][line][x] +=1

		self.totSamples = sum(self.numSamples)
		#calculate priors given total samples, then turn pixel counts for each class into frequencies and add Laplace smoothing k
		for i in range(10):
			a = self.numSamples[i]
			self.priors[i] = a/self.totSamples
			print("count of ",i,"s in samples is",a)
			self.probs[i] = (self.probs[i]/a)+self.k
		#print("PROBS",self.probs,"ENDPROBS")
	def test(self):
		while self.ddtest.done is not True:
			self.ddtest.readNextNum()
			self.numTestSamples[self.ddtest.answer] += 1
			dfv = (0,[0 for x in range(10)])

			#for calculating the best classification
			maxidx = 0
			max = -100000000

			for k in range(10):
				dfv[1][k] = self.priors[k]
				for i in range(32):
					for j in range(32):
						if self.ddtest.img[i][j] == 1:
							dfv[1][k] += math.log(self.probs[k][i][j])
						else:
							if self.probs[k][i][j] != (1 + self.k):
								dfv[1][k] += math.log((1 + self.k - self.probs[k][i][j]))
				#finds the best guess for the classification
				if dfv[1][k] > max:
					maxidx = k
					max = dfv[1][k]
			dfv = (maxidx, dfv[1])
			if dfv[1][dfv[0]] > self.maxMinPostProbs[dfv[0]][0]:
				self.maxMinPostProbs[dfv[0]] = (dfv[1][dfv[0]],self.maxMinPostProbs[dfv[0]][1])
				self.bestWorstTokens[dfv[0]] = (deepcopy(self.ddtest.img),self.bestWorstTokens[dfv[0]][1])
			elif dfv[1][dfv[0]] < self.maxMinPostProbs[dfv[0]][1]:
				self.maxMinPostProbs[dfv[0]] = (self.maxMinPostProbs[dfv[0]][0],dfv[1][dfv[0]])
				self.bestWorstTokens[dfv[0]] = (self.bestWorstTokens[dfv[0]][0],deepcopy(self.ddtest.img))
			#print("DFV: ",dfv[0]," ANSWER: ",self.ddtest.answer)
			self.confMat[self.ddtest.answer][dfv[0]] += 1
		print("NUM TEST SAMPLES ",self.numTestSamples)
		for x in range(10):
			self.probSucc[x] = self.confMat[x][x]
		for x in range(10):
			if self.numTestSamples[x] == 0:
				self.probSucc[x] = 0
			else:
				self.probSucc[x] = self.probSucc[x]/self.numTestSamples[x]
		print(self.probSucc)

		self.printConfMat()
		self.printBestWorst()




	#print function
	def printProbs(self,i):
		for j in range(32):
			for k in range(32):
				print(self.probs[i][j][k],end=' ')
			print()

	def printConfMat(self):
		str = "CLASSIFIED"
		print("               TRUE VALUES")
		print("        ",end='')
		for x in range(10):
			print(x,end='  ')
		print()
		for x in range(10):
			print(str[x]," ",x,end=' ')
			for y in range(10):
				print('{:3d}'.format(self.confMat[x][y]),end='')
			print()

	def printBestWorst(self):
		for x in range(10):
			print("PRINTING BEST EXAMPLE OF ",x)
			print("SAMPLE HAS PROBABILITY ",self.maxMinPostProbs[x][0])
			for y in range(32):
				for z in range(32):
					print(self.bestWorstTokens[x][0][y][z],end='')
				print()
			print("PRINTING WORST EXAMPLE OF ",x)
			print("SAMPLE HAS PROBABILITY ",self.maxMinPostProbs[x][1])
			for y in range(32):
				for z in range(32):
					print(self.bestWorstTokens[x][1][y][z],end='')
				print()
nb = NaiveBayes()
nb.train()
nb.test()
