from Plotter import Plotter
import seaborn as sns
import matplotlib.pyplot as plt
class ScatterPlotter(Plotter):
    def __init__(self,y,y_predict,residual = None):
        super().__init__(y,y_predict)
        self.residual = residual
    
    def plot(self):
        if self.residual is None:
            self.residual = self.run_calculations()

        f, axes = plt.subplots(1, 2,figsize=(30, 10))
        sns.scatterplot(x=self.y_predict, y=self.residual,ax=axes[0])
        sns.scatterplot(x=self.y,y=self.y_predict,ax=axes[1])
        axes[0].set_title('Residuals versus Predicted Values',fontsize=20)
        axes[1].set_title('Actual Values versus Predicted Values',fontsize=20)
        axes[0].set_xlabel('Predicted Values',fontsize=16)
        axes[0].set_ylabel('Residuals',fontsize=16)
        axes[1].set_xlabel('Predicted Values',fontsize=16)
        axes[1].set_ylabel('Actual Values',fontsize=16)
        sns.set(font_scale = 2)
    
        
        
