# Execution Results

The following test cases were executed using the original Newton-Raphson implementation.

The program uses:

- `epsilon = 0.01`
- Maximum iteration count = `100`

---

## Case 1 — Maximum Iteration Limit

Functions:

```math
f_1(x,y)=x^2+1
```

```math
f_2(x,y)=y^2+1
```

Initial point:

```math
(x_0,y_0)=(2,3)
```

Since both functions are always greater than or equal to 1 for real values of \(x\) and \(y\), the stopping condition cannot be satisfied.

The iteration continues until the maximum iteration count of 100 is reached.

### Output

```text
다른 초기값을 넣어보세요. 뉴턴-랩슨 방법으로 근사가 어렵습니다.
```

---

## Case 2 — Singular Jacobian

Functions:

```math
f_1(x,y)=x^2+y^2-1
```

```math
f_2(x,y)=x^2-y^2
```

Initial point:

```math
(x_0,y_0)=(0,0)
```

At the initial point, the Jacobian matrix is

```math
J(0,0)
=
\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}.
```

Since the Jacobian is singular, `np.linalg.solve` cannot determine a unique Newton step.

### Output

```text
Jacobian이 특이행렬이어서 Newton step을 계산할 수 없습니다.
다른 초기값을 입력해보세요.
다른 초기값을 넣어보세요. 뉴턴-랩슨 방법으로 근사가 어렵습니다.
```

---

## Case 3 — Successful Convergence

Functions:

```math
f_1(x,y)=x^2+y^2-5
```

```math
f_2(x,y)=xy-2
```

Initial point:

```math
(x_0,y_0)=(0.8,1.8)
```

One exact solution near the initial point is

```math
(x,y)=(1,2).
```

### Output

```text
2번 반복한 결과, 근사해는 x = 1.0000780944943382, y = 2.000078094494338 입니다.
```

The result is very close to the exact solution \((1,2)\).

---

## Case 4 — Successful Convergence

Functions:

```math
f_1(x,y)=x^2+y^2-2
```

```math
f_2(x,y)=x^2-y^2
```

Initial point:

```math
(x_0,y_0)=(0.5,1.5)
```

One exact solution near the initial point is

```math
(x,y)=(1,1).
```

### Output

```text
3번 반복한 결과, 근사해는 x = 1.0003048780487804, y = 1.0000051200131073 입니다.
```

The result is very close to the exact solution \((1,1)\).

---

## Case 5 — Successful Convergence

Functions:

```math
f_1(x,y)=x^2+y^2-4
```

```math
f_2(x,y)=x^2-y
```

Initial point:

```math
(x_0,y_0)=(1.5,2.0)
```

The positive solution is approximately

```math
(x,y)\approx(1.2496,1.5616).
```

### Output

```text
2번 반복한 결과, 근사해는 x = 1.2502009894867037, y = 1.561904761904762 입니다.
```

The approximation satisfies both equations within the stopping tolerance.

---

## Summary

These test cases show three possible behaviors of the implementation:

- Successful convergence to an approximate root
- Termination after reaching the maximum iteration count
- Failure when a singular Jacobian matrix is encountered
