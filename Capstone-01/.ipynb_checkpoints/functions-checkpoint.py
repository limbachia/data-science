import numpy as np
import pandas as pd

def log1p(X,columns):
    X_new = X.copy()
    for col in columns:
        X_new['log1p({})'.format(col)] = np.log1p(X_new[col])
        #X_new.drop(col,axis=1,inplace=True)
    return X_new

def remove_outliers(X,columns,thresholds):
    outlier = pd.DataFrame()
    for column,threshold in zip(columns,thresholds):
        if column == 'GrLivArea':
            outlier[column] = X[column] > threshold
        elif column == 'LotArea':
            percentile = np.percentile(X[column],99)
            outlier[column] = X[column] > threshold
        else:
            print(column+' not processed for outliers')
    return X[~outlier.any(axis=1)]


def to_str(X,columns):
    for column in columns:
        X[column] = X[column].astype(str)
    return X


def impute_cat(X,feat_to_mode, mapper):
    """
    Imputes missing values in Electrical and MasVnrType with modes, 
    and replaces NaN values in all other categorical features with 'Missing'
    """
    for col, mode in mapper.items():
        if col in feat_to_mode:
            X[col].fillna(mode,inplace=True)
        else:
            X[col].fillna('Missing',inplace=True)
    return X


def impute_num(X,mapper):
    for feat,vals in mapper.items():
        if feat == 'LotFrontage':
            for key,val in vals.items():
                LotConfig,LotShape = key
                X.loc[(X['LotFrontage'].isnull()) & (X['LotConfig']==LotConfig) & (X['LotShape']==LotShape),['LotFrontage']] = val
            X.loc[X['LotFrontage'].isnull(),'LotFrontage'] = X['LotFrontage'].median()
        else:
            X[feat].fillna(vals,inplace=True)
    return X

def augment(X,geo_df):
    X.reset_index(inplace=True)
    X = X.merge(geo_df,how='left')
    X.set_index('Id',inplace=True)
    return X

def addFeatures(X, new_features=['AreaPerRoom','GarageYrBltMinusYearBuilt']):
    for feat in new_features:
        if feat == 'AreaPerRoom':
            #GrLivArea = np.expm1(X['log1p(GrLivArea)'])
            X['AreaPerRoom'] = X['GrLivArea'].divide(X.TotRmsAbvGrd)
            X['log1p(AreaPerRoom)'] = np.log1p(X.AreaPerRoom)
        elif feat == 'GarageYrBltMinusYearBuilt':
            X['GarageYrBltMinusYearBuilt']=X['GarageYrBlt'].subtract(X.YearBuilt)
    return X

def LabelEncode(X,mapper):
    return X.replace(mapper)