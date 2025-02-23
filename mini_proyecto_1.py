import pandas as pd
import random

# Define operations and their corresponding lambda functions
operations = {
    'SUM': lambda x, y: x + y,
    'SUB': lambda x, y: x - y,
    'MUL': lambda x, y: x * y,
    'DIV': lambda x, y: x / y if y != 0 else None,
    'POW': lambda x, y: x ** y if y < 10 else x ** 10 # limit exponent to avoid very large numbers
}

# Generate data
data = []
for _ in range(1000):
    operation = random.choice(list(operations.keys()))
    operand_1 = random.randint(1, 1000)
    operand_2 = random.randint(1, 1000)
    if operation == 'POW' and operand_2 < 10: operand_2 = random.randint(1, 15)
    result = operations[operation](operand_1, operand_2)
    data.append([operation, operand_1, operand_2, result])

# Create DataFrame
df = pd.DataFrame(data, columns=['operation', 'operand_1', 'operand_2', 'result'])

# Save to CSV
csv_path = './data/math_operations.csv'
df.to_csv(csv_path, index=False)