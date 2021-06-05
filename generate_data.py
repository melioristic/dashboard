import numpy as np
import pandas as pd
from datetime import datetime, timedelta

strt_time = datetime(2020,1,1)
time = np.array([strt_time+timedelta(days=i) for i in range(100)]).reshape(100,1)


res_level = np.random.rand(100).reshape(100,1)

precip = np.random.randint(low = 0, high = 100, size =100).reshape(100,1)

stacked_array = np.hstack([time, precip, res_level])


data = pd.DataFrame(stacked_array)
data.columns = ['time', 'precip', 'res_level']

data.to_csv('gen_data.csv', index=False)