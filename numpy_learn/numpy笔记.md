numpy中reshape(c,-1)的解读

```python

b = [[1, 2], [3, 4]]
b = np.array(b)
b.shape
Out[10]: (2, 2)
b.shape[1]
Out[11]: 2
b 
Out[12]: 
array([[1, 2],
       [3, 4]])
b.reshape(1,-1)
Out[13]: array([[1, 2, 3, 4]])
b
Out[14]: 
array([[1, 2],
       [3, 4]])
c = b.reshape(4,-1)
c
Out[16]: 
array([[1],
       [2],
       [3],
       [4]])
d = b.reshape(1,-1)
d
Out[18]: array([[1, 2, 3, 4]])

```

