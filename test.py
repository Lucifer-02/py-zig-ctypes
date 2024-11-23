import ctypes

# Load the shared library
module = ctypes.CDLL("./libmodule.so")

# Call the `add` function
add_c = module.add
add_c.argtypes = (ctypes.c_int, ctypes.c_int)  # Define argument types
add_c.restype = ctypes.c_int                  # Define return type


# Define a Python wrapper function for the Zig `add` function
def add(a: int, b: int) -> int:
    return add_c(a, b)

# Now you can call it using keyword arguments
result = add(a=1, b=2)
print(f"Result of add: {result}")
