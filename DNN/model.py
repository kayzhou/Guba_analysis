import torch
import numpy as np
from tqdm import tqdm
from torch import nn
from torch.utils.data import Dataset, DataLoader, TensorDataset


class MyNet(nn.Module):
    """
    多层感知机
    """
    def __init__(self, input_size, hidden_size, output_size):
        super(MyNet, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        z1 = self.linear1(x)
        a1 = self.relu1(z1)
        y_pred = self.linear2(a1)
        return y_pred


def load_train_data(in_name):
    """
    加载训练数据
    """
    X = []
    y = []
    for line in open(in_name):
        label, vec = line.strip().split('\t')
        x = np.array([float(v) for v in vec.split(',')])
        y.append(int(label))
        X.append(x)
    X = np.array(X)
    y = np.array(y)
    return X, y


M, input_size, hidden_size, output_size = 300, 1000, 100, 5
mod = MyNet(input_size, hidden_size, output_size)

# x = torch.randn(M, input_size)
# y = torch.randn(M, output_size)
x_data, y_data = load_train_data('../train_data_ACL-20180710.txt')
x_data = torch.from_numpy(x_data)
y_data = torch.from_numpy(y_data).view(-1, 1)
print(x_data.size(), y_data.size())



# 定义损失函数
loss_fn = nn.MSELoss(size_average=False)

## 设置超参数 ##
learning_rate = 1e-4
EPOCH = 500

optimizer = torch.optim.SGD(mod.parameters(), lr=learning_rate)

## 开始训练 ##
for t in tqdm(range(EPOCH)):
    
    # 向前传播
    y_pred = mod(x_data)
    
    # 计算损失
    loss = loss_fn(y_pred, y_data)
    
    # 显示损失
    if t % 50 == 0:
        print(loss.data.item())
    
    # 在我们进行梯度更新之前，先使用optimier对象提供的清除已经积累的梯度。
    optimizer.zero_grad()
    
    # 计算梯度
    loss.backward()
    
    # 更新梯度
    optimizer.step()


print(mod)