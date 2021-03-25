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

#type = 1 在1不再2的
#type = 2 在1不再1的
#type = 0 在1不再2或者在2不在1
def get_not_common(str1, str2, type):
    ret = []
    if (type == 1 or type == 0):
        for tmp in str1:
            if tmp not in str2:
                ret.append(tmp)
    if (type == 2 or type == 0):
        for tmp in str2:
            if tmp not in str1:
                ret.append(tmp)
    return ret
