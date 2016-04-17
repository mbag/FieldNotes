# Fun with pointers in Python

Sometimes you need to use Python to access code from precompiled library written in C.
This can easily be done using Python's _ctypes_ module.
This module has many powerful features that enable you to interact with precompiled C library code.
In this short entry I will not write about ctypes from bottom up, rather I would like to document peculiar problem that I came across few weeks ago.
The problem was with dereferencing void pointer, that was within structure, which it self was also passed as pointer to library function :)

**libfoo.so** will be library which will be loaded into Python.
The sources can be compiled using Makefile attached.
The code was tested on Fedora, gcc (GCC) 5.3.1 20151207 (Red Hat 5.3.1-2).
Files:
* foo.h - header file
* foo.c - source code for the library
* main.c - file showing usage of the library in C
* foo.py - file showing usage of the library in Python
* Makefile - makefile used for building library and main executable

> Note:
> If you need to examine contents of any shared object (SO) under Linux, you can use utility called *nm*.
> This utility will list symbols from object files.
> Additional warning for C++ libraries, when using ctypes you will have to use mangled name of the function from SO, unless functions were compiled with extern "C".
> Either way *nm* will show you names of functions that are available in SO.

File **foo.h** holds definition of structure foobar, with two elements, count and void pointer.  
_count_ holds number of elements.  
_void pointer_ will be used to hold address of the dynamically allocated memory inside _set_values_foobar_ function.  
In **foo.c** you can see, that _void_pointer_ points to a memory allocated by malloc.
The values stored are ints, from _0_ to _value - 1_.

Now finally lets get to the Python :)  
**foo.py** is using standard way of accessing _set_values_foobar()_ function
```python
libfoo = cdll.LoadLibrary("./libfoo.so")

libfoo.set_values_foobar(6, byref(foobar))
```

To access non-pointer elements of the _foobar_ structure that was passed by reference, using ctypes function _byref_, the standard Python syntax for accessing attributes of object is used:
```python
print("Number of elements in foobar structure: {}".format(foobar.count))
```

However, accessing values pointed to by _void_pointer_ needs special handling.
If you just used print as in previous example, then you would get address of what is being pointed to, but not the values stored:
```python
# prints address of memory pointed to by _void_pointer_
print(foobar.void_pointer)
```

The solution is to cast it into other type of pointer using ctypes' _cast()_ function:
```python
array = cast(foobar.void_pointer, POINTER(c_int))
```
Now we can access the elements as if they were in an array in Python.

So, yeah, it was pretty obvious once I figured it out :)

What I would like to investigate further, but didn't have time at this point is how and when is the dynamic memory being allocated when library function is being called from Python script.

