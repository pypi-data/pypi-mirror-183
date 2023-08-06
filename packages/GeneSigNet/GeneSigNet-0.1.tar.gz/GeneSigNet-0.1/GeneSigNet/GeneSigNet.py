import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import moment
from numpy import linalg as LA
from sklearn.linear_model import Lasso, LassoLarsIC
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
#Estimation of a Sparce Partial correlation matrix for a given data
def WeightMatrix(D, maxit, tolerance):
    [N_patients,N_variables]=D.shape
    w=np.zeros((N_variables, N_variables), dtype=float)
    Data=np.array(D)
    for k in range(N_variables):
        X=np.delete(Data,k,1)
        y=Data[:,k]
        model = LassoLarsIC(criterion='aic')
        model.fit(X, y)
        dense_lasso = Lasso(alpha=model.alpha_, fit_intercept=True, max_iter=maxit, tol=tolerance)
        dense_lasso.fit(X, y)
        w[k,:]=np.insert(dense_lasso.coef_, k, 0)
    W = pd.DataFrame(w, columns=D.columns, index=D.columns)
    W=Directionality(W, D)
    W=AM_Normalization(W)
    return W
def Directionality(W, D):
    eps=0.01 
    w=np.array(W); A=np.array(W)
    A[A!=0]=1; A=A+A.T; A[A!=2]=0
    for i in range(len(W.iloc[:,1])):
        A[i,0:i]=0
    index=np.transpose(np.nonzero(A))
    Genes=W.columns;
    for k in range(len(index)): 
        [x,y]=np.array(index[k])
        if abs(W.iloc[x,y])>eps and abs(W.iloc[y,x])>eps:
            Wx=w[x,:]; Wx[y]=0; X=D.iloc[:,x]-D.dot(Wx)
            Wy=w[y,:]; Wy[x]=0; Y=D.iloc[:,y]-D.dot(Wy)
            GamX=abs(moment(X, moment=3)/pow(stats.tstd(X),3))
            GamY=abs(moment(Y, moment=3)/pow(stats.tstd(Y),3))
            DelX=abs(moment(X, moment=4)/pow(stats.tstd(X),4)-3)
            DelY=abs(moment(Y, moment=4)/pow(stats.tstd(Y),4)-3)
            if abs(W.iloc[y,x])>=abs(W.iloc[x,y]) and GamX>GamY and DelX>DelY:
                W.iloc[x,y]=0
            elif abs(W.iloc[y,x])<=abs(W.iloc[x,y]) and GamX<GamY and DelX<DelY:
                W.iloc[y,x]=0
        elif abs(W.iloc[x,y])>eps and abs(W.iloc[y,x])<=eps:  
            W.iloc[y,x]=0
        elif abs(W.iloc[x,y])<=eps and abs(W.iloc[y,x])>eps: 
            W.iloc[x,y]=0
    return W

def Inside_L1ball(v): 
    n, = v.shape  
    s = np.abs(v)
    if s.sum() <= 1:
        return v
    else:
        u = np.sort(s)[::-1]
        cSum = np.cumsum(u)
        rho = np.nonzero(u * np.arange(1, n+1) > (cSum - 1))[0][-1]
        theta = float(cSum[rho] - 1) / (rho+1)
        x = (s - theta).clip(min=0)
        x *= np.sign(v)
    return x

def AM_Normalization(W):
    NormW=0; k=0
    while NormW<LA.norm(W) or k<1:
        for i in range(W.shape[0]):
            W.iloc[i,:]=Inside_L1ball(np.array(W.iloc[i,:]))
        for i in range(W.shape[1]):
            W.iloc[:,i]=Inside_L1ball(np.array(W.iloc[:,i]))
        NormW=LA.norm(W)
        k=k+1
    return W