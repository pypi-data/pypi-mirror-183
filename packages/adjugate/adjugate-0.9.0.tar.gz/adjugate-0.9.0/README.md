# adjugate

A package the calculation of submatricies, minors, adjugate- and cofactor matricies.


```python
import numpy as np
from adjugate import adj

M = np.random.rand(4, 4)
adjM = adj(M)
M, adjM
```




    (array([[0.18329442, 0.94536378, 0.34391239, 0.20550072],
            [0.78458047, 0.22499907, 0.77014223, 0.47769537],
            [0.88592897, 0.4528784 , 0.55644987, 0.41555019],
            [0.01536316, 0.01204791, 0.18303602, 0.39473538]]),
     array([[-0.06511768, -0.09164306,  0.18272557, -0.04755706],
            [ 0.07837219, -0.06018737,  0.037211  , -0.00713731],
            [ 0.06085684,  0.29195247, -0.26938624, -0.10140202],
            [-0.02807654, -0.12997254,  0.11666507,  0.24495152]]))



## Installation


```python
pip install adjugate
```

    Requirement already satisfied: adjugate in c:\users\sebas\appdata\local\programs\python\python310\lib\site-packages (0.9.0)
    Requirement already satisfied: numpy in c:\users\sebas\appdata\local\programs\python\python310\lib\site-packages (from adjugate) (1.23.2)
    Note: you may need to restart the kernel to use updated packages.
    

## Usage

This package provides four functions:

### submatrix

`submatrix(M, i, j)`

Removes the `i`-th row and `j`-th column of `M`. Multiple indices or slices can be provided.


```python
from adjugate import submatrix

M = np.arange(16).reshape(4, 4)
M, submatrix(M, 1, 2)
```




    (array([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11],
            [12, 13, 14, 15]]),
     array([[ 0,  1,  3],
            [ 8,  9, 11],
            [12, 13, 15]]))



### minor

`minor(M, i, j)`

Calculates the (`i`, `j`) minor of `M`.


```python
from adjugate import minor

M = np.random.rand(4, 4)
minor(M, 1, 2)
```




    -0.2538708866028015



### adj

`adj(M)`

Calculates the adjugate of `M`.


```python
M, adj(M)
```




    (array([[0.35381183, 0.54730453, 0.35431937, 0.89590154],
            [0.91740846, 0.19762669, 0.94414055, 0.55011907],
            [0.68733545, 0.90827084, 0.62361795, 0.33229656],
            [0.92673781, 0.71399516, 0.4132883 , 0.43831859]]),
     array([[-0.16343332,  0.04516309, -0.32022591,  0.52013549],
            [ 0.03057683, -0.21278356,  0.34006538, -0.05324915],
            [-0.04418908,  0.25387089,  0.37337688, -0.51136777],
            [ 0.33740518,  0.01174995, -0.22894734,  0.02935693]]))



### cof

`cof(M)`

Calculates the cofactor matrix of `M`.


```python
from adjugate import cof

M, cof(M)
```




    (array([[0.35381183, 0.54730453, 0.35431937, 0.89590154],
            [0.91740846, 0.19762669, 0.94414055, 0.55011907],
            [0.68733545, 0.90827084, 0.62361795, 0.33229656],
            [0.92673781, 0.71399516, 0.4132883 , 0.43831859]]),
     array([[-0.16343332,  0.03057683, -0.04418908,  0.33740518],
            [ 0.04516309, -0.21278356,  0.25387089,  0.01174995],
            [-0.32022591,  0.34006538,  0.37337688, -0.22894734],
            [ 0.52013549, -0.05324915, -0.51136777,  0.02935693]]))



## Speed

If you know that you matrix is invertible, then `np.linalg.det(M) * np.linalg.inv(M)` might be a faster choice (O(3) instad of O(5)). But this is in general, especially as the determinant approaches zero, not possible or precise:


```python
import matplotlib.pyplot as plt

N = 20
dets, errs = [], []
for _ in range(1000):
    M = np.random.rand(N, N)
    dets += [np.linalg.det(M)]
    errs += [np.linalg.norm(adj(M)-np.linalg.det(M)*np.linalg.inv(M))]

fig, ax = plt.subplots()
ax.scatter(dets, errs, marker='o', s=(72./fig.dpi)**2)
ax.set_yscale('log')
ax.set_xlim(-2, +2)
ax.set_ylim(1e-16, 1e-12)
plt.show()
```


    
![png](output_14_0.png)
    

