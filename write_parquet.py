import pandas as pd
import numpy as np

T = 1000
t_sec = np.arange(0,T)
sinr_dB = np.random.randn(T) + 5
bigNum = np.arange(0,T,dtype='uint64') + (1 << 62)

df = pd.DataFrame({'t_sec':t_sec, 'sinr_dB':sinr_dB, 'bigNum':bigNum})
df.to_parquet(fname='data.parquet',compression='snappy')
