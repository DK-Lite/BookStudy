import torch
import torch.nn as nn

x = torch.Tensor([[1,2],[3,4]])
x = torch.from_numpy(np.array([[1,2],[3,4]]))

import numpy as np
x = np.array([[1,2],[3,4]])



def linear(x, w , b):
    return torch.mm(x,w) + b


class nn.Module():
    def __call__(self, *args, **kwargs):


        self.forward()

        self.backward()

class MyLinear(nn.Module):
    def __init__(self, config=None):
        #super(Linear, self).__init__(config)
        super().__init__()
        self.linear = nn.Linear(config.input_size, config.output_size)
        #self.w = nn.Parmeter(torch.FloatTensor(config.input_size, config.output_size))
        #self.b = nn.Parmeter(torch.FloatTensor(config.output_size))


    def forward(self, inputs=None, labels=None):
        output = self.linear(inputs)

        #output = torch.mm(x, self.w) + self.b

        return output


class Config:
    input_size = 0
    output_size = 0
    def __init__(self):
        pass

def train(model, x, y, optim):
    optim.zero_grad()

    y_hat = model(x)
    loss = ((y - y_hat)**2).sum() / x.size(0)

    loss.backward()

    optim.step()

    return loss.data




def ground_truth(x):
    return 3 * x[:,0] + x[:,1] + -2 * x[:,2]

def main():
    # # [batch_size, input_size]
    # x = torch.FloatTensor(16, 10)
    # # [input_size, output_size]
    # w = torch.FloatTensor(10, 5)

    # b = torch.FloatTensor(5)

    # y = linear(x, w, b)




    # linear = MyLinear(config)

    # y = linear(x)

    config = Config()
    batch_size = 1
    _epochs = 1000
    _iter = 10000
    config.input_size = 10
    config.output_size = 5

    model = MyLinear(config)
    optim = torch.optim.SGD(model.parmeters(), lr=1e-4, momentum=0.1)

    print(model)



    for epoch in range(_epochs):
        avg_loss = 0

        for i in range(_iter):
            x = torch.rand(batch_size, 3)
            y = ground_truth(x.data)

            loss = train(model, x, y, optim)

            avg_loss += loss
            avg_loss avg_loss / _iter

        x_valid = torch.FloatTensor([[.3, .2, .1]])
        y_valid = ground_truth(x.data)

        model.eval()
        y_hat = model(x_valid)
        model.train()

        print(avg_loss, y_valid.data[0], y_hat.data[0, 0])

        if avg_loss < .001 :
            break










if __name__ == "__main__":
    main()