### Matrix Inverse 

Cho ma trận $A^{2\times 2}$ như sau: 

$A = \begin{bmatrix} -2 & 6 \\ 8 & -4 \end{bmatrix}$

1. Tính toán định thức của ma trận:

    $\det(A)$ = ad - bc
    $\det(A)$ = $-2 \times -4$ - $6 \times 8$ = -40
2. Do định thức của ma trận $A \neq 0$, do đó ma trận A khả nghịch
3. Tính toán ma trận nghịch đảo $A^{-1}$

    $A^{-1} = \frac{1}{\det(A)}  Adj(A) \\$
    $A^{-1} = \frac{1}{40} \begin{bmatrix} 4 & -6 \\ 8 & -4 \end{bmatrix}\\$
    Thực hiện tính toán element-wise cho scalar với matrix:

    
    $A^{-1} = \begin{bmatrix} 0.1 & 0.15 \\ 0.2 & 0.05 \end{bmatrix}$ 

### Eigenvector and eigenvalue 

Cho ma trận $A^{2\times 2}$ như sau: 

$A = \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix}\\$
#### Tính toán các giá trị riêng của A:
1. Công thức giá trị riêng
    $\\ \det(A - \lambda I) = 0$

2. Tính toán ma hiệu của $A - \lambda I$:
    $\\ A - \lambda I = \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda
     \end{bmatrix} =  \begin{bmatrix} 0.9 - \lambda & 0.2 \\ 0.1 & 0.8 - \lambda \end{bmatrix}\\$
3. Tính toán $\lambda$:
    $\\ \det(\begin{bmatrix} 0.9 - \lambda & 0.2 \\ 0.1 & 0.8 - \lambda \end{bmatrix}) = 0$
    $\longrightarrow \lambda = \{0.7,1\}$ 

#### Tính toán các vector riêng của A:
1. Công thức vector riêng
    $\\ Av = \lambda v \Leftrightarrow (A - \lambda I)v = 0$
2. Tính toán vector riêng với giá trị $\lambda = 0.7$
    $\\ \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix} - \begin{bmatrix} 0.7 & 0 \\ 0 & 0.7
     \end{bmatrix}v = 0$ 
    $\\ \rightarrow$ Phương trình có nghiệm tổng quát là:
    $\\  X = \left(\begin{matrix} -x_2 \\ x_2 \end{matrix}\right)$
    $\\ v_1 = \rightarrow \left(\begin{matrix} -1 \\ 1 \end{matrix}\right)$
3. Tính toán vector riêng với giá trị $\lambda = 1$
    $\\ \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1
     \end{bmatrix}v = 0$ 
    $\\ \rightarrow$ Phương trình có nghiệm tổng quát là:
    $\\  X = \left(\begin{matrix} 2x_2 \\ x_2 \end{matrix}\right)$
    $\\ \rightarrow v_2 = \left(\begin{matrix} 2 \\ 1 \end{matrix}\right)$
    
### Cosine Similarity
1. Đề bài
    Cho $x = \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix}$ và $y = \begin{bmatrix} 1 \\ 0 \\ 3 \\ 0 \end{bmatrix}$
2. Tính toán cosine similarity
    $cs(x,y) = \frac{x \cdot y}{||x|| ||y||} = \frac{(1 + 0 + 9 + 0)}{\sqrt{30}\sqrt{10}} = \frac{3}{\sqrt{3}}$