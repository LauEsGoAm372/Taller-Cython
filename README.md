# Taller-Cython


En el presente repositorio se encuentra un archivo en Python y Cython para comparar el tiempo del rendimiento que tarda cada lenguaje en el calculo
de los pasos que tarda alguien en dar la vuelta a un planeta. Sin embargo para poder descargar y ejecutar correctamente el presente taller debe hacer lo siguiente:

1. Debe usar el sistema operativo ubuntu linux

2. Debe ejecutar linea por linea en la terminal los siguientes comandos para instalar cython 
    sudo apt install cython
    sudo apt install build-essential
    sudo apt install python3-venv
    sudo apt install cython3
    sudo apt update
    sudo apt install build-essential
    sudo apt install python3-venv
    sudo apt install cython3
    
3. Para ejecutar debe de ejecutar linea por linea los siguientes comandos en la terminal de la carpeta que contiene los archivos presentes aqui:
    python3 setup.py build_ext --inplace
    python3 performance.py

Finalmente se presenta un ejemplo de los tiempos totales que pueden presentar cada lenguaje:
laura@laura-VirtualBox:~/Documents/Cython$ python3 performance.py
Tiempo total de Python 4.3392181396484375e-05
Tiempo total de Cython 1.9550323486328125e-05
Cython es 2.2195121951219514 veces más rápido que Python


En donde se identifica que el lenguaje Cython es mucho más rápido que el lenguaje Python por 2.22 segundos. Sin embargo no se garantiza que Cython siempre sea mucho
más rápido que Python.
