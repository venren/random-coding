import numpy as np
class EuclideanDistance:
    def calc1DDistance(self, x: list, y: list):
        x = np.array(x)
        y = np.array(y)
        return np.sqrt(np.sum((x-y) **2 ))
    
    

dist = EuclideanDistance()
x = [1.8, 2.0,-3.7, 4.7]
y = [0.6,2.1,1.9,-1.4]
result = dist.calc1DDistance(x,y)
print(result)

x = [1.6,2]
y = [1.5,2]
result = dist.calc1DDistance(x,y)
print(result)



        


