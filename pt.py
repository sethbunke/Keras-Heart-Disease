import torch
import numpy as np

torch.manual_seed(42)

features = torch.randn((1,5))
weights = torch.randn_like(features)

bias = torch.randn((1,1))




#import torch
import random
import numpy as np

features = np.random.rand(1,5)
weights = np.random.rand(1,5)
bias = np.random.rand(1,1)

result = np.dot(features, weights.T)

print(result)

print(bias + result)