"""
Installing Python and Essential Libraries

Extracted from the companion book.
"""

# test_installation.py
print("Testing Python installation...")

# Test basic functionality
print("1. Basic Python test:")
x = 5
y = 10
print(f"   {x} + {y} = {x + y}")

# Test NumPy if installed
try:
    import numpy as np
    print("2. NumPy test:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"   Array: {arr}")
    print(f"   Mean: {arr.mean()}")
except ImportError:
    print("2. NumPy test: NumPy not installed")

# Test Pandas if installed
try:
    import pandas as pd
    print("3. Pandas test:")
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(f"   DataFrame:\n   {df}")
except ImportError:
    print("3. Pandas test: Pandas not installed")

# Test Matplotlib if installed
try:
    import matplotlib
    print("4. Matplotlib test: Successfully imported")
    matplotlib_version = matplotlib.__version__
    print(f"   Version: {matplotlib_version}")
except ImportError:
    print("4. Matplotlib test: Matplotlib not installed")

print("\nInstallation test complete!")
