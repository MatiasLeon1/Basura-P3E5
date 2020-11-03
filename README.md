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

![Grafico_1](https://user-images.githubusercontent.com/43649125/97984325-64102d80-1db5-11eb-8efd-6194b03479f4.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

![GIF_caso_1](https://user-images.githubusercontent.com/43649125/97984342-6a060e80-1db5-11eb-8064-c9e210c8af1e.gif)

##

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

![Grafico_2](https://user-images.githubusercontent.com/43649125/97984498-9cb00700-1db5-11eb-9be2-3cc00abca490.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

![GIF_caso_2](https://user-images.githubusercontent.com/43649125/97984506-9faaf780-1db5-11eb-802b-b99abd967577.gif)

##

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

![Grafico_3](https://user-images.githubusercontent.com/43649125/97984545-a9ccf600-1db5-11eb-8e5f-569183ccca82.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

![GIF_caso_3](https://user-images.githubusercontent.com/43649125/97984551-acc7e680-1db5-11eb-889d-84ae6614a458.gif)

##

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

![Grafico_4](https://user-images.githubusercontent.com/43649125/97984574-b3565e00-1db5-11eb-9354-c1acbf9cabcd.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

![GIF_caso_4](https://user-images.githubusercontent.com/43649125/97984584-b6e9e500-1db5-11eb-8807-2b66ec447f08.gif)

##

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

![Grafico_5](https://user-images.githubusercontent.com/43649125/97984622-c5380100-1db5-11eb-8202-63a67790dca8.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF

![GIF_caso_5](https://user-images.githubusercontent.com/43649125/97984630-c79a5b00-1db5-11eb-8c1a-c19790b04151.gif)

##

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

![Grafico_6](https://user-images.githubusercontent.com/43649125/97984655-ce28d280-1db5-11eb-8882-f75e03f67ee8.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF


![GIF_caso_6](https://user-images.githubusercontent.com/43649125/97984666-d08b2c80-1db5-11eb-9268-374c02c491cf.gif)

##

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

![Grafico_7](https://user-images.githubusercontent.com/43649125/97984683-d7b23a80-1db5-11eb-990e-176e19e4f2e4.png)

##

#### Imágenes fijas T° en intervalos de tiempo

##

#### GIF


![GIF_caso_7](https://user-images.githubusercontent.com/43649125/97984687-da149480-1db5-11eb-9015-1685e2905f6c.gif)

##
