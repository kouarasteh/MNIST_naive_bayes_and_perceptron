import numpy as np

class NaiveBayes():

	def __init__(self):
		self.class_0 = np.zeros((32, 32), float, 'C')
		self.class_1 = np.zeros((32, 32), float, 'C')
		self.class_2 = np.zeros((32, 32), float, 'C')
		self.class_3 = np.zeros((32, 32), float, 'C')
		self.class_4 = np.zeros((32, 32), float, 'C')
		self.class_5 = np.zeros((32, 32), float, 'C')
		self.class_6 = np.zeros((32, 32), float, 'C')
		self.class_7 = np.zeros((32, 32), float, 'C')
		self.class_8 = np.zeros((32, 32), float, 'C')
		self.class_9 = np.zeros((32, 32), float, 'C')

	def train(self):
		


nb = NaiveBayes()
print(nb.class_0)
		