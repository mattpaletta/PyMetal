# rectangle.pyx
cdef extern from "metal.h" namespace "pymtlpp":
    cdef cppclass Metal:
        Metal()
        int runTest()

cdef class PyMetal:
    cdef Metal *thisptr      # hold a C++ instance which we're wrapping
    def __cinit__(self):
        self.thisptr = new Metal()
    def __dealloc__(self):
        del self.thisptr
    def runTest(self):
        return self.thisptr.runTest()