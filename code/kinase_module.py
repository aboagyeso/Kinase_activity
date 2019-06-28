#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np



def add_gausian(y,mu,sigma):
    noise = np.random.normal(mu,sigma,[4639,117])
    df_aug = df +noise 
    df_new = pd.concat([df,df_aug])
    return(df_aug)

def drop_corr(df):
    '''Function drops highly correlated columns above a 0.95 threshold and outputs a new dataframe.

    Input:
        df: pandas DataFrame
        '''
    import numpy as np
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column]>0.95)]
    df_new = df.drop(df[to_drop],axis = 1)
    return(df_new)

def model_eval(model):
    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    model_score = model.score(X_test,y_test)
    model_mse =  mse(y_test,pred)
    model_r2 =r2(y_test,pred)
    return(model_score, model_mse, model_r2)

