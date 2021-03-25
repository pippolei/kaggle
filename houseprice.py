# coding=utf-8
import os, sys, gc, datetime
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import lightgbm as lgb
from xgboost import XGBClassifier
from sklearn.svm import SVC   
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from lib import *

file_dir = "C:\git\data\houseprice\\" 
sys.path.append(file_dir)
os.chdir(file_dir)

traindata = pd.read_csv("train.csv", sep=',') # encoding='utf-16')
testdata = pd.read_csv("test.csv", sep=',') 
train, test = train_test_split(traindata, test_size=0.2)

diff_string = get_not_common(traindata.columns, testdata.columns, 1)