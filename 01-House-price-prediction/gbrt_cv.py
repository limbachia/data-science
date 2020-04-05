#!/usr/bin/env python
#SBATCH -t 5-30:30:30
#SBATCH --cores-per-socket=4
#SBATCH --sockets-per-node=2
#SBATCH --nodes=2-4
#SBATCH --mem=24000
#SBATCH -J python
#SBATCH -o gbrt_cv.out

import pandas as pd
import numpy as np
import pickle

with open('processed_data.pkl','rb') as file:
    FEATURES, ordinal_map, interactions, train, y = pickle.load(file)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train, y, test_size=0.3, random_state=42)

print("X_train : " + str(X_train.shape))
print("X_test : " + str(X_test.shape))
print("y_train : " + str(y_train.shape))
print("y_test : " + str(y_test.shape))

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

param_grid_gbrt = {
    'loss' : ['ls','lad','huber','quantile'],
    'learning_rate' : [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1],
    'n_estimators':[50,100,150,200,250,300,350,400],
    'min_samples_split':[2,4,8,10,15,20,25,30],
    'min_samples_leaf':[2,4,6,8,10,12,15,30],
    'max_depth':[None,2,5,10,15,20,25,50,75,100],
}

gbrt = GradientBoostingRegressor()
gbrt_cv = GridSearchCV(gbrt,param_grid=param_grid_gbrt,cv=10,n_jobs=-1)
gbrt_cv.fit(X_train,y_train)

with open('gbrt_mod.pkl','wb') as out:
    pickle.dump(gbrt_cv,out)
