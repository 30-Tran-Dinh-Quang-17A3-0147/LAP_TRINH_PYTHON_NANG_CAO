path_1 = 'E:\\Năm2\\HK1\\python nang cao\\LAB\\LAB2\\DATA\\efficiency.txt'
path_2 = 'E:\\Năm2\\HK1\\python nang cao\\LAB\\LAB2\\DATA\\shifts.txt'

efficiency = []
with open(path_1, 'r') as file:
    for line in file:
        efficiency.append(float(line.strip()))

shifts = []
with open(path_2, 'r') as file:
    for line in file:
        shifts.append((line.strip()))
efficiency[:5] , shifts[:5]

import numpy as np 
np_shifts = np.array(shifts)
np_shifts.dtype

np_efficiency = np.array(efficiency)
np_efficiency.dtype

morning_mask = np_shifts == 'morning'

hieu_suat_morning = np_efficiency[morning_mask]

hieu_suat_tb_morning = np.mean(hieu_suat_morning)
hieu_suat_tb_morning  

non_morning = np_shifts != 'morning'

hieu_suat_non_morning = np_efficiency[non_morning]

hieu_suat_tb_non_morning = np.mean(hieu_suat_non_morning)
hieu_suat_tb_non_morning

dtype = [('shifts','U10'),('efficiency',float)]

workers = np.array(list(zip(shifts, efficiency)), dtype=dtype)
workers[:5]

sorted_workers = np.sort(workers , order='efficiency')

Hieu_suat_Max = sorted_workers[+1]['shifts']
Hieu_suat_Min = sorted_workers[0]['shifts']

print(sorted_workers[:10])
print(Hieu_suat_Max , Hieu_suat_Min)
