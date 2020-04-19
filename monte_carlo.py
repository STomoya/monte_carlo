'''
simulating pi by monte carlo method

numpy is super fast :)
'''

import time
import numpy as np

n_samples = 600000000

xs = np.random.rand(n_samples)
ys = np.random.rand(n_samples)
samples = np.stack([xs,ys])

start = time.time()
norms = np.linalg.norm(samples, axis=0)
inside_samples = (norms <= 1.).sum()
duration = time.time() - start

def calc_pi(n_samples, inside_samples):
    return inside_samples / n_samples * 4.

print('Total random samples                 : {}'.format(n_samples))
print('Numbers of samples inside the circle : {}'.format(inside_samples))
print('Simulated pi : {}'.format(calc_pi(n_samples, inside_samples)))

print('Time : {}'.format(duration))

'''
Total random samples                 : 600000000
Numbers of samples inside the circle : 471228925
Simulated pi : 3.1415261666666665
Time : 4.463215112686157
'''