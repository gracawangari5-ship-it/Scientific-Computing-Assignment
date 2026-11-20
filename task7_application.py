import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Conductance matrix of a three-node electrical network
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

# Current measurements entering the three nodes (Amperes)
current_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Factor the conductance matrix once
lu, piv = lu_factor(A)

for i, currents in enumerate(current_sets, start=1):
    voltages = lu_solve((lu, piv), currents)

    residual = currents - A @ voltages

    print(f"Current measurement set {i}")
    print("Node voltages (V):", voltages)
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Direct solution for comparison
print("Direct voltage solution for first set:",
      np.linalg.solve(A, current_sets[0]))
