from ctypes import Structure, cdll, c_int, c_void_p
from ctypes import byref, cast, POINTER

class FOOBAR(Structure):
    _fields_ = [
        ("count", c_int),
        ("void_pointer", c_void_p),
    ]


# create structure objects
foobar = FOOBAR()

#load library contents into Python
libfoo = cdll.LoadLibrary("./libfoo.so")

libfoo.set_values_foobar(6, byref(foobar))

print("Number of elements in foobar structure: {}".format(foobar.count))

# If you just print foobar.void_pointer it will show the address, but not the actual contents
# print(foobar.void_pointer)
#cast void pointer into int pointer
array = cast(foobar.void_pointer, POINTER(c_int))

print("Elements in array are:")
for i in range(foobar.count):
    print(array[i])


