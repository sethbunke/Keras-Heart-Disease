import torch
import numpy as np

torch.manual_seed(42)

features = torch.randn((1,5))
weights = torch.randn_like(features)

bias = torch.randn((1,1))