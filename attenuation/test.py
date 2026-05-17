import numpy as np

# Generate the array
data = np.geomspace(1e-3, 10e3, 5000)

# Save the array to a text file, with all values in the first column
np.savetxt('output.txt', data, fmt='%.4e')
print("Data successfully saved to output.txt")
