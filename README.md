# Entrega 5

Para la presente entrega se generó una función llamada *`temperatura_hormigon`* la cual recibió los parámetros mencionados a continuación:

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
* `Titulo_carpeta`: variable que crea carpeta donde se almacenarán los archivos `.png`
* `Gráfico`: variable que crea el gráfico de la evolución de la temperatura c/r a los puntos de interés.

Los puntos de interés se muestran a continuación:

![image](https://user-images.githubusercontent.com/43649125/97931939-866e6080-1d4d-11eb-8b08-8bf8212bd9b1.png)

Junto a lo anterior, se presentarán imágenes de la distribución de la temperatura en tiempos específicos, siendo estos: `0h`, `2h`, `6h`, `12h` y `24h`. Y por último, se adjuntará un gráfico de la evolución de la temperatura en cada caso.

### Caso 1
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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

#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF


### Caso 2
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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
#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

### Caso 3
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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

#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

### Caso 4
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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

#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

### Caso 5
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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
#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

### Caso 6
___

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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

#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

### Caso 7
___

Se considera un periodo `T = 1 dia `.

Condiciones de borde:

| _**Variable**_ | _**Valor**_ |
|--------------|-----------|
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

#### Gráfico evolución T°

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF
