

import os
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression


class Job_Portal:
    def __init__(self):
        self.dataset = []
        self.x_train,self.x_test,self.y_train,self.y_test = [], [], [], []
        self.load_dataset()
        self.train_test_split()
        self.model = None
        self.tfidf_train = None
        self.tfidf_test = None
        self.result = []
        self.preprocess()
    def preprocess(self):
        self.vectorize()
        self.initialize_algorithm()
        self.train_data()
    def load_dataset(self):

        self.dataset=pd.read_csv(os.getcwd() + "/on_job_portal/dataset/job_portal.csv", encoding="latin-1")
        self.dataset.drop("title",axis=1)
    def train_test_split(self):
        self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.dataset['description'].fillna(' '), self.dataset.label.fillna(' '), test_size=0.01, random_state=7)
    def vectorize(self):
        self.tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
        self.tfidf_train=self.tfidf_vectorizer.fit_transform(self.x_train)
    def initialize_algorithm(self):
        self.model=PassiveAggressiveClassifier(max_iter=100)
        # self.model=LinearRegression()
    def train_data(self):
        self.model.fit(self.tfidf_train,self.y_train)
    def print_result(self):
        print (self.result)
        return self.result[0]

    def predict(self, custom_input):
        custom_input='00'+pd.Series([[custom_input]]).astype(str)
        self.tfidf_test=self.tfidf_vectorizer.transform(custom_input)
        self.result=self.model.predict(self.tfidf_test)
        return self.print_result()

