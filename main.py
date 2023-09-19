import numpy as np

A = np.array([(1, 2), (3, 4)])
B = np.array([5, 6])
A1 = np.linalg.inv(A)  # tạo ma trận nghich đảo
print(A)
print(B)
print(A1)
X = np.dot(A1, B)
print('Nghiem cua he:', X)
print('lam thu')
print('aaaaaaaaaaaaaaaaaaaaaaaa')
print('tt')
