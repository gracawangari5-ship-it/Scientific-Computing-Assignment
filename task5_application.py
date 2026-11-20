import numpy as np

# Quantities of products sold by three shops
quantities = np.array([
    [10, 5],
    [8, 7],
    [12, 4]
])

# Prices of the two products
prices = np.array([500, 200])

# Calculate revenue for each shop
revenue = quantities @ prices

# Calculate total revenue
total_revenue = np.sum(revenue)

# Display results
print("Revenue for each shop:")
print(revenue)

print("\nTotal revenue:")
print(total_revenue)
