#Autor: laura gomez 
#Fecha: 28 de octubre
# Fichero para la creacion del objeto compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cy_planeta.pyx"))
setup(ext_modules = exts)


