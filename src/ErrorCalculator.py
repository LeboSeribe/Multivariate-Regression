from math import sqrt
from sklearn.metrics import mean_squared_error
class ErrorCalculator:
    def __init__(self,y,y_predict):
        self.y = y
        self.y_predict = y_predict
        
    
    def get_residuals(self):
        residual = self.y.values - self.y_predict
        return residual
        
    def get_standardised_residuals(self):
        resid = self.get_residuals()
        residual_std = resid.std()
        standardised_residual =  resid/residual_std
        return standardised_residual
    
    def get_mse(self):
        mse = mean_squared_error(self.y,self.y_predict)
        return mse
    
    def get_rmse(self):
        mse = self.get_mse()
        RMSE = sqrt(mse)
        return RMSE
    
    
    def error_summary(self):
        resids= self.get_standardised_residuals()
        print('error summary:')
        print(f'average standard residuals: {resids.mean()}')
        print(f'minimum standard residuals: {min(resids)}')
        print(f'maximum standard residuals: {max(resids)}')
        print(f'MSE: {self.get_mse()}')
        print(f'RMSE: {self.get_rmse()}')
        
        
