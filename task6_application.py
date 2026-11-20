import numpy as np

# x = number of basic bundles
# y = number of premium bundles

# Basic bundle: 2 GB, KSh 100
# Premium bundle: 5 GB, KSh 200

A = np.array([
    [2.0, 5.0],
    [100.0, 200.0]
])

b = np.array([22.0, 1000.0])

solution = np.linalg.solve(A, b)

residual = b - A @ solution

print(f"Basic bundles sold: {solution[0]:.0f}")
print(f"Premium bundles sold: {solution[1]:.0f}")
print("Verification:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
