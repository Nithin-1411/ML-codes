import pandas as pd
import numpy as np
data_frame=pd.read_excel(r"C:\Users\G NITHIN\Documents\Machine_learning\Lab Session1 Data.xlsx",sheet_name="Purchase data")
data1=data_frame.iloc[0:10,1:4]
A=data1.to_numpy()
data3=data_frame.iloc[0:10,4:5]
C=data3.to_numpy()
Ain=np.linalg.pinv(A)
X=np.matmul(Ain,C)
Ain=np.linalg.pinv(A)
X=np.matmul(Ain,C)
Xt=np.array(X.tolist())
print("The model vector X for predicting the cost of the products is ")
print(Xt)

