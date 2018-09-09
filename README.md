# PyMtlpp

### Experimental, not yet working

Based on https://github.com/naleksiev/mtlpp

Tried to port the implementation to Python using Cython.

To compile, I am using the following commands: 

`clang++ -std=c++11 -x objective-c++ -mmacosx-version-min=10.13 -fPIC -c mtlpp.mm -o ../mtlpp.o`

to compile the library.  Then to compile the cython code:

`ARCHFLAGS="-arch x86_64" python3 setup.py build_ext --inplace`
