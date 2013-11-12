from distutils.core import setup
from distutils.extension import Extension
examplemodule = Extension(name="minpqFast", sources=['minpqFast.c', ])
setup(name="minpqFast", ext_modules=[examplemodule])