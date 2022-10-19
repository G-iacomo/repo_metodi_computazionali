import numpy as np
import pandas as pd

g = np.arange(1,31,1)
t = np.random.uniform(low=0.0, high=35.0, size=(30))
dt = np.full(30,0.5)
p = np.random.uniform(low=0.0, high=10.0, size=(30))
dp = np.full(30,1.0)
df = pd.DataFrame(columns=['giorno','temperatura','err. t','pioggia','err. p'])
df ['giorno'] = g
df ['temperatura'] = t
df ['err. t'] = dt
df ['pioggia'] = p
df ['err. p'] = dp
df.to_csv('eserciziL02a.csv', index=False)
