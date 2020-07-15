#!/usr/bin/env python
#SBATCH -t 5-30:30:30
#SBATCH --cores-per-socket=4
#SBATCH --sockets-per-node=2
#SBATCH --nodes=2-4
#SBATCH --mem=24000
#SBATCH -J python
#SBATCH -o adaBoost.out


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
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

param_grid_tree = {
    'max_depth':[None,2,5,10,15,20,25,50,75,100],
    'min_samples_split':[2,4,8,10,15,20,25,30],
    'min_samples_leaf':[2,4,6,8,10,12,15,30],
}
tree = DecisionTreeRegressor()
tree_cv = GridSearchCV(tree,param_grid=param_grid_tree,n_jobs=-1,cv=10)
tree_cv.fit(X_train,y_train)

base_estimator = tree_cv.best_estimator_

param_grid_ada = {
    'n_estimators':[50,100,150,200,250,300,350,400],
    'learning_rate' : [0.01, 0.05, 0.1, 0.5],
    'loss' : ['linear', 'square', 'exponential'],
}

ada = AdaBoostRegressor(base_estimator=base_estimator)
ada_cv = GridSearchCV(ada,param_grid=param_grid_ada,cv=10,n_jobs=-1)
ada_cv.fit(X_train,y_train)

with open('ada_mod.pkl','wb') as out:
    pickle.dump(ada_cv,out)
