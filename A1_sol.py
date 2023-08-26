import pandas as pd
import numpy as np





data_frame=pd.read_excel(r"C:\Users\G NITHIN\Documents\Machine_learning\Lab Session1 Data.xlsx",sheet_name="Purchase data")
#data_frame.dropna(axis=1,inplace=True)
data1=data_frame.iloc[0:10,1:4]
A=data1.to_numpy()


data3=data_frame.iloc[0:10,4:5]
C=data3.to_numpy()


Ain=np.linalg.pinv(A)


X=np.matmul(Ain,C)


#A1
#Augumented matrix
Au = np.hstack((A, C))
#rank of Augumented matrix is dimensionality
dimensionality=np.linalg.matrix_rank(Au)
print("The dimensionality of vector space is ",dimensionality)
print()
#A2
print("The Number of vectors in vector space are",dimensionality)
print()
#A3
Rank_A=np.linalg.matrix_rank(A)
print("The rank of matrix is ",Rank_A)
print()

#A4
Ain=np.linalg.pinv(A)
X=np.matmul(Ain,C)


Xt=np.array(X.tolist())
print("The cost of Candy Mango Milk are respectively")
print(Xt[0])
print(Xt[1])
print(Xt[2])

