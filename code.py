import numpy as np

# coeff[i][j] represents the coefficient of x^i * y^j.
x_degree1 = int(input("f1의 x 최고차수: "))
y_degree1 = int(input("f1의 y 최고차수: "))
coeff1 = np.zeros((x_degree1 + 1, y_degree1 + 1))

for i in range(x_degree1 + 1):
    for j in range(y_degree1 + 1):
        coeff1[i][j] = float(input(f"f1의 x^{i}y^{j} 계수: "))


x_degree2 = int(input("f2의 x 최고차수: "))
y_degree2 = int(input("f2의 y 최고차수: "))
coeff2 = np.zeros((x_degree2 + 1, y_degree2 + 1))

for i in range(x_degree2 + 1):
    for j in range(y_degree2 + 1):
        coeff2[i][j] = float(input(f"f2의 x^{i}y^{j} 계수: "))

# Compute the partial derivative with respect to x.
def df_dx(arr, x, y):
    result = 0
    for i in range(1, arr.shape[0]):
        for j in range(arr.shape[1]):
            result += arr[i][j] * i * x**(i-1) * y**j
    return result

# Compute the partial derivative with respect to y.
def df_dy(arr, x, y):
    result = 0
    for i in range(1, arr.shape[1]):
        for j in range(arr.shape[0]):
            result += arr[j][i] * i * y**(i-1) * x**j
    return result

# Evaluate the polynomial at (x, y).
def f(arr, x, y):
    result = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            result += arr[i][j] * x**i * y**j
    return result


epsilon = 0.01
count = 0
x = float(input("x의 초기값을 입력하세요: "))
y = float(input("y의 초기값을 입력하세요: "))


# Multivariable Newton-Raphson iteration.
while (abs(f(coeff1, x, y)) > epsilon or abs(f(coeff2, x, y)) > epsilon):

    # Construct the Jacobian matrix at the current approximation.
    Jacobian = np.array([
        [df_dx(coeff1, x, y), df_dy(coeff1, x, y)],
        [df_dx(coeff2, x, y), df_dy(coeff2, x, y)]
    ])

    F_old = np.array([
        [f(coeff1, x, y)],
        [f(coeff2, x, y)]
    ])

    x_old = np.array([
        [x],
        [y]
    ])

    # Solve J * delta = F directly instead of explicitly computing J^(-1).
    # det(J)=0 prevents the Newton step from being uniquely determined.
    try:
        delta = np.linalg.solve(Jacobian, F_old)
    
    except np.linalg.LinAlgError:
        print("Jacobian이 특이행렬이어서 Newton step을 계산할 수 없습니다.")
        print("다른 초기값을 입력해보세요.")
        break

    # x_(k+1) = x_k - delta.
    x_new = x_old - delta

    x = x_new[0][0]
    y = x_new[1][0]

    count += 1

    if count == 100:
        break

# Check whether the method actually converged before reaching the iteration limit.
if abs(f(coeff1, x, y)) > epsilon or abs(f(coeff2, x, y)) > epsilon:
    print("다른 초기값을 넣어보세요. 뉴턴-랩슨 방법으로 근사가 어렵습니다.")
else:
    print(f"{count}번 반복한 결과, 근사해는 x = {x}, y = {y} 입니다.")
