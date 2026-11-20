import numpy as np

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

# Modified CPU total from 20 to 28
b = np.array([28.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
