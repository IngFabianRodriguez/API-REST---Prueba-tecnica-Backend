# API - Operaciones
## Tecnologia:
API REST realizada en Python con el framework flask al momento de realizar su ejecucion este se encuentra en el puerto 5000.
Para ejecutar localmente la solucion se deben seguir los siguiente pasos:

1. Instalar Python 3.9.0
2. creacion de un entorno virtual con el comando:
	py -m venv venv 
3. Instalar las librerias que se encuentran en el archivo requirements.txt con el comando: pip install -r requirements.txt
4. Ejecutar el archivo main.py con el comando py main.py
## Descripcion API:
### 1. POST: /operacion/cuadratica
Se crea apuntamiento localhost:5000/operacion/cuadratica con el metodo POST para realizar la operacion cuadratica y calcular las 2 posibles soluciones para la fórmula cuadrática.

Este apuntamiento recibe por medio de JSON el envio de 3 valores: Valor_a, Valor_b y Valor_c. A verse de la siguiente manera:

``` json
{
	"valor_a": 2,
	"valor_b": 7,
	"valor_c": 2
}
```
Y recibe los siguiente resultados:

Cuando el determinado el Mayor que 0 la respuesta es:

``` json
{
	"x1": -5.563859338365493,
	"x2": -8.436140661634507
}
```

Si el determinante es igual a 0 la respuesta es:
``` json

{
	"x": 5.563859338365493,
}
```

Y si esta no tiene una respuesta se recibe el siguiente mensaje:

``` json
{ "Operacion": "No tiene solucion" }
```


### 2. POST: /operacion/fibonacci

Se crea apuntamiento localhost:5000/operacion/fibonacci con el metodo POST para realizar la operacion y mostrar la serie Fibonacci para el tamaño de la serie enviado como parámetro.

Este apuntamiento recibe el siguiente JSON para determinar cuantos valores a de devolver:

``` json
{
	"valor_n" : 10
}
```

Como respuesta se recibe un JSON con la cantidad de objetos solicitados:

``` json
{
	"result": [0,1,1,2,3,5,8,13,21,34]
}
```