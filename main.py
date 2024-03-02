import tensorflow as tf
import numpy as np
import pandas as pd


np.set_printoptions(precision=3, suppress=True)

training_data = pd.read_csv("train.csv")
testing_data = pd.read_csv("test.csv")

print(training_data.info())