import pandas as pd
import numpy as np
import hpat

@hpat.jit
def rolling_df1(n):
    df = pd.DataFrame({'A': np.ones(n), 'B': np.random.ranf(n)})
    Ac = df.A.rolling(3).sum()
    return Ac.sum()

@hpat.jit
def rolling_df2(n):
    df = pd.DataFrame({'A': np.ones(n), 'B': np.random.ranf(n)})
    Ac = df.A.rolling(3, center=True).sum()
    return Ac.sum()

n = 10
print(rolling_df2(n))
