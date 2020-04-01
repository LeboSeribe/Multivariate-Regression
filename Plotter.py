import seaborn as sns
import matplotlib.pyplot as plt
class Plotter:
    def __init__(self,y,y_predict):
        self.y = y
        self.y_predict = y_predict
        
        
    def run_calculations(self):
        residual = self.y.values - self.y_predict
        return residual
        
        
        
    def plot(self):
        resid = self.run_calculations()    
        
        sns.distplot(resid)
        plt.title('The Residuals histogram plot')
        plt.ylabel('Distribution')
        plt.xlabel('Residuals')
        plt.show()