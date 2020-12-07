import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        [self.contents.append(attr) for attr in kwargs.keys() \
             for _ in range(kwargs[attr])]
            
    def draw(self, n):  
        if n > len(self.contents):
            return self.contents
        else:
            i = 0
            rnd = []
            while i < n:
                rnd.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
                i+=1
            return rnd       

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for _ in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        results = exp_hat.draw(num_balls_drawn)
        aux = 0
        for attr, value in expected_balls.items():
            if results.count(attr) >= value:
                aux += 1
        if aux == len(expected_balls.keys()):
            counter += 1
    return float(counter)/num_experiments