import pandas as pd
import numpy as np
import csv


file_path = '/home/tran/Pseudo-Inverse-Jacobian-Inverse-Kinematics/squarev2.csv'
data = pd.read_csv(file_path, decimal=',', header=0, skipinitialspace=True)

# print(df.to_string())
# print(data.head(10))
X = np.array(data['x'])
Y = np.array(data['y'])
Z = np.array(data['z'])
x_len = len(X)
y_len = len(Y)
z_len = len(Z)
for x_data in X:
    print(x_data)
