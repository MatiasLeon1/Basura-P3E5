# Entrega 5
  
Para la presente entrega se generó una función llamada *`temperatura_hormigon`*.
La función fue creada para evaluar cada uno de los 7 casos por separado. Su estructura fue pensada para ser amigable de utilizar, ya que todos los parámetros que se deben cambiar se encuentran en 1 línea de código _(línea `258` para los casos 1-6, y línea `263` para el caso 7)_.
Junto a lo anterior, solo se requirió cambiar las variables `fp_in` y `fp_out`. Esto, ya que los frames y el gráfico de cada caso debían ir con su número correspondiente. Para los casos 1-6, las líneas que deben cambiarse en cada ejecución de código son las `275` y `276`. Para el caso 7 las líneas que deben cambiarse con la `280` y `281`.

La funcion *`temperatura_hormigon`* recibe los parámetros mencionados a continuación:

* `a`: altura del cubo de hormigón
* `b`: ancho del cubo de hormigón
* `Nx`: Número de intervalos en X
* `Ny`: Número de intervalos en Y
* `Temperatura_inicial`: temperatura inicial del bloque de Hormigón
* `T_S`: temperatura superior del bloque
* `T_IZ`: temperatura en borde izquierdo del bloque
* `T_IN`: temperatura inferior del bloque
* `T_D`: temperatura en el borde derecho del bloque
* `G_S`: gradiente de temperatura superior
* `G_IZ`: gradiente de temperatura borde izquierdo
* `G_IN`: gradiente de temperatura inferior
* `G_D`: gradiente de temperatura borde derecho
* `Titulo_carpeta`: variable que da nombre a la carpeta donde se almacenarán los archivos `.png`
* `Gráfico`: variable que da nombre al gráfico de la evolución de la temperatura c/r a los puntos de interés.

Los puntos de interés se muestran a continuación:

![image](https://user-images.githubusercontent.com/43649125/97931939-866e6080-1d4d-11eb-8b08-8bf8212bd9b1.png)

Junto a lo anterior, se presentarán imágenes de la distribución de la temperatura en tiempos específicos, siendo estos: `0h`, `2h`, `6h`, `12h` y `24h`. Y por último, se adjuntará un gráfico de la evolución de la temperatura en cada caso.

_Dato: las variables que tienen el valor "@" no se consideran, esto quiere decir que solo puede existir una temperatura fija o un gradiente para cada borde, pero no ambas._ 

### Caso 1
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 20°C |
| T_S | 0°C |
| T_IZ | 20°C |
| T_IN | 20° |
| T_D | 0°C |
| G_S | @ |
| G_IZ | @ |
| G_IN | @ |
| G_D | @ |

* #### Gráfico evolución T°

![Grafico_1](https://user-images.githubusercontent.com/43649125/97984325-64102d80-1db5-11eb-8efd-6194b03479f4.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985135-95d5c400-1db6-11eb-9bda-97b64733fc65.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985227-c61d6280-1db6-11eb-95b5-5175c9b44f99.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985235-c87fbc80-1db6-11eb-9dd4-8724630e8291.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985245-cb7aad00-1db6-11eb-9b85-c4da00279ce6.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985251-cd447080-1db6-11eb-9657-42053ec83a96.png)
##

* #### GIF

![GIF_caso_1](https://user-images.githubusercontent.com/43649125/97984342-6a060e80-1db5-11eb-8064-c9e210c8af1e.gif)

##

### Caso 2
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 20°C |
| T_S | 0°C |
| T_IZ | 20°C |
| T_IN | 20° |
| T_D | @ |
| G_S | @ |
| G_IZ | @ |
| G_IN | @ |
| G_D | 0 |

* #### Gráfico evolución T°

![Grafico_2](https://user-images.githubusercontent.com/43649125/97984498-9cb00700-1db5-11eb-9be2-3cc00abca490.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985135-95d5c400-1db6-11eb-9bda-97b64733fc65.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985227-c61d6280-1db6-11eb-95b5-5175c9b44f99.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985235-c87fbc80-1db6-11eb-9dd4-8724630e8291.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985245-cb7aad00-1db6-11eb-9b85-c4da00279ce6.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985251-cd447080-1db6-11eb-9657-42053ec83a96.png)
##

* #### GIF

![GIF_caso_2](https://user-images.githubusercontent.com/43649125/97984506-9faaf780-1db5-11eb-802b-b99abd967577.gif)

##

### Caso 3
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 10°C |
| T_S | 0°C |
| T_IZ | 20°C |
| T_IN | 20° |
| T_D | 20°C |
| G_S | @ |
| G_IZ | @ |
| G_IN | @ |
| G_D | @ |

* #### Gráfico evolución T°

![Grafico_3](https://user-images.githubusercontent.com/43649125/97984545-a9ccf600-1db5-11eb-8e5f-569183ccca82.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985396-fb29b500-1db6-11eb-9de9-f41f02e46581.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985411-fe24a580-1db6-11eb-8efd-4b9a5ee18ab8.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985417-0086ff80-1db7-11eb-8197-d2c70d347aed.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985430-02e95980-1db7-11eb-9d56-5f82cf911b83.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985432-054bb380-1db7-11eb-83e9-d33f61e680e6.png)
##

* #### GIF

![GIF_caso_3](https://user-images.githubusercontent.com/43649125/97984551-acc7e680-1db5-11eb-889d-84ae6614a458.gif)

##

### Caso 4
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 0.5 [m] |
| Nx | 15 |
| Ny | 30 |
| T°_inicial | 10°C |
| T_S | 0°C |
| T_IZ | 20°C |
| T_IN | 20° |
| T_D | @ |
| G_S | @ |
| G_IZ | @ |
| G_IN | @ |
| G_D | 0 |

* #### Gráfico evolución T°

![Grafico_4](https://user-images.githubusercontent.com/43649125/97984574-b3565e00-1db5-11eb-9354-c1acbf9cabcd.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985461-0ed51b80-1db7-11eb-9922-c0fa6c4d007b.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985469-109edf00-1db7-11eb-8f88-201b2e2d4448.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985474-1268a280-1db7-11eb-83a1-dc2af8fef3f9.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985484-15639300-1db7-11eb-8116-474eb8ba0fc3.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985490-17c5ed00-1db7-11eb-8f08-a3e6ae2812de.png)
##

* #### GIF

![GIF_caso_4](https://user-images.githubusercontent.com/43649125/97984584-b6e9e500-1db5-11eb-8807-2b66ec447f08.gif)

##

### Caso 5
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 5°C |
| T_S | @ |
| T_IZ | 25°C |
| T_IN | @ |
| T_D | 25°C |
| G_S | 0 |
| G_IZ | @ |
| G_IN | 0 |
| G_D | @ |

* #### Gráfico evolución T°

![Grafico_5](https://user-images.githubusercontent.com/43649125/97984622-c5380100-1db5-11eb-8202-63a67790dca8.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985513-1f859180-1db7-11eb-99b6-192234bee1a9.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985520-214f5500-1db7-11eb-98ee-015c04e3b79c.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985523-23b1af00-1db7-11eb-9f5e-4995677817fe.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985525-257b7280-1db7-11eb-9ab7-9578722d587d.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985527-27453600-1db7-11eb-90f1-a4851f2682ac.png)

##

* #### GIF

![GIF_caso_5](https://user-images.githubusercontent.com/43649125/97984630-c79a5b00-1db5-11eb-8c1a-c19790b04151.gif)

##

### Caso 6
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 30°C |
| T_S | @ |
| T_IZ | 10°C |
| T_IN | @ |
| T_D | @ |
| G_S | 0 |
| G_IZ | @ |
| G_IN | 0 |
| G_D | 0 |

* #### Gráfico evolución T°

![Grafico_6](https://user-images.githubusercontent.com/43649125/97984655-ce28d280-1db5-11eb-8882-f75e03f67ee8.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985543-2e6c4400-1db7-11eb-9a90-95e816c10a12.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985551-30360780-1db7-11eb-984c-3e5afc359761.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985559-31673480-1db7-11eb-8fa0-13e8d3643f4d.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985572-34fabb80-1db7-11eb-99e7-3dc7dae76c06.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985578-36c47f00-1db7-11eb-8448-c657c3c5e3e9.png)
##

* #### GIF


![GIF_caso_6](https://user-images.githubusercontent.com/43649125/97984666-d08b2c80-1db5-11eb-9268-374c02c491cf.gif)

##

### Caso 7
___

Se considera un periodo `T = 1 dia `.

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|:------------:|:---------:|
| a | 1 [m] |
| b | 1 [m] |
| Nx | 30 |
| Ny | 30 |
| T°_inicial | 20°C |
| T_S | Sinusoide con variación de 10° |
| T_IZ | @ |
| T_IN | @ |
| T_D | @ |
| G_S | @ |
| G_IZ | 0 |
| G_IN | 0 |
| G_D | 0 |

* #### Gráfico evolución T°

![Grafico_7](https://user-images.githubusercontent.com/43649125/97984683-d7b23a80-1db5-11eb-990e-176e19e4f2e4.png)

##

* #### Imágenes fijas T° en intervalos de tiempo

![frame_0000](https://user-images.githubusercontent.com/43649125/97985617-404de700-1db7-11eb-84de-884d98de8741.png)
![frame_0004](https://user-images.githubusercontent.com/43649125/97985621-42b04100-1db7-11eb-86ca-5886dc9f6e5c.png)
![frame_0012](https://user-images.githubusercontent.com/43649125/97985625-447a0480-1db7-11eb-880f-074ab8807a28.png)
![frame_0024](https://user-images.githubusercontent.com/43649125/97985630-4643c800-1db7-11eb-8f26-db15a9de4092.png)
![frame_0048](https://user-images.githubusercontent.com/43649125/97985633-480d8b80-1db7-11eb-88c8-0eb73262f2fe.png)
##

* #### GIF


![GIF_caso_7](https://user-images.githubusercontent.com/43649125/97984687-da149480-1db5-11eb-9015-1685e2905f6c.gif)

##

* ### Explique ¿como cambia el código para el caso 3-D? ¿Como se imponen las condiciones de borde?

Para el caso en 3D, lo primero que se debe hacer es definir la nueva dirección a considerar _(profundidad en este caso)_. A modo de ejemplificación se procederá a mencionar las variables que hipotéticamente deberían incluirse en el código para que este ejecute un caso en 3D. La  variable de la profundidad sería `c =`.
El segundo paso sería definir la variable `Nz` que posea el número de intervalos en la nueva dirección agregada.
Juntando lo anterior, se debería crear la variable `dz=` que sería la discretización para la nueva dirección considerada. Esta seria el cuociente entre la variable `c`y `Nz`.
Lo siguiente sería cambiar la función de conveniencia para que reciba 3 parámetros _(1 por cada dirección)_. De esta manera quedaría `coords = lambda i, j, k :(dx*i,dy*j, dz*k)`


Dado que es un objetivo fundamental de este código tanto el ser capaz de observar gráficamente el comportamiento de la temperatura en el hormigón, como el respectivo desarrollo de la temperatura en este, es que se debería cambiar la función `imshowbien` para que considere la direccion `c` en lo graficado. Los cambios aquí serían netamente de ploteo.

El código 2D solo considera el comportamiento de la temperatura en el plano XY. Debido a esto se deberían crear las variables auxiliares `u_km2` y `u_km3` que muestren cómo se comportará la temperatura en los planos XZ e YZ respectivamente.
Luego simplemente bastaría definir variables para las condiciones de borde del ejercicio. Para efectos de explicar cómo funciona un código en 3D, se asumirá que tanto las temperaturas como los gradientes son aplicados en las caras del cubo de hormigón  _(6 en total)_ en vez de en los bordes de este, por lo que las variables a agregar serían:
* `T_S`
* `T_IN`
* `T_IZ`
* `T_D`
* `T_FR`
* `T_TR`

Esto se replicará para los gradientes de temperatura, manteniendo los @ para los casos correspondientes.

Finalmente solo faltaría revisar las condiciones de borde del ejercicio a resolver.

