import torch
import torch.nn as nn
import numpy as np


class MySoftmaxt(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        numerator = torch.exp(x)
        denumerator = numerator.sum(0, keepdims = True)
        output = numerator / denumerator
        return output


class MySoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0, keepdim=True)
        numerator = torch.exp(x - c.values)
        denumerator = numerator.sum(0, keepdims = True)
        output = numerator / denumerator
        return output

if __name__ == "__main__": 
    data = torch.Tensor([1, 2, 3])
    softmax = MySoftmaxt()
    output = softmax(data)
    print(output)

    data = torch.Tensor([1, 2, 3])
    softmax_stable = MySoftmaxStable()
    output = softmax_stable(data)
    print(output)
