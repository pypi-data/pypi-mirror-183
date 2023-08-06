Esto es un ejemplo de creación de paquetes en Python.
# Compilación
Se compila con el siguiente comando:
"py -m build"

Esto generara varios archivos, pero las distribuciones que queremos subir se encuentran en la carpeta generada "dist" donde estara el paquete comprimido.

# Subida
Subimos el paquete con el siguiente comando:
"py -m twine upload --repository testpypi dist/*"

Donde el usuario sera: __token__
y la contraseña la generada una unica vez.
Esto lo sube a "testpypi", un repositorio temporal de paquetes de python. Si quisieramos subirlo de manera definitiva a Pypi (repositorio real de paquetes oficiales) bastaría con usar el comando:
"twine upload dist/*".

Se instalaría como un paquete normal.


# Notas
A la hora de realizar cualquier clase de cambio en el paquete, habria que cambiar la version, de lo contrario no dejara subirlo.



# Enlaces utiles
-https://packaging.python.org/en/latest/tutorials/packaging-projects/