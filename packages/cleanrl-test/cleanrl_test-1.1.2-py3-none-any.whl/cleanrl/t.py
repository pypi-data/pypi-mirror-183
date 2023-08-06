import torch
# this is the same example in wiki
P = torch.Tensor([0.36, 0.48, 0.16])
Q = torch.Tensor([0.333, 0.333, 0.333])

print((P * (P.log() - Q.log())))