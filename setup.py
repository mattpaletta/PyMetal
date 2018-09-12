# setup.py
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# ARCHFLAGS="-arch x86_64" python3 setup.py build_ext --inplace
# clang++ -std=c++11 -x objective-c++ -mmacosx-version-min=10.13 -fPIC -c mtlpp.mm -o mtlpp.o


setup(
        ext_modules=[
            Extension(name="pymtlpp",
                      sources=["metal/pymtlpp.pyx", "metal/metal.cpp"],
                      language="c++",
                      extra_objects=["mtlpp.o"],
                      extra_compile_args=["-std=c++11", "-mmacosx-version-min=10.13", "-fPIC"],
                      extra_link_args=["-mmacosx-version-min=10.13",
                                       "-framework", "Metal",
                                          "-framework", "MetalKit",
                                          "-framework", "Cocoa",
                                          "-framework", "CoreFoundation",
                                          "-fobjc-link-runtime",
                                          "-fPIC"],)],
        cmdclass = {'build_ext': build_ext})


# setup(
#         ext_modules=[
#             Extension("rectangle",
#               ["rect/rect.pyx", "rect/Rectangle.cpp"],
#               language="c++",)],
#         cmdclass = {'build_ext': build_ext})