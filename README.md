# Taller práctico: análisis de datos con Pandas

Programa de consola que lee datos de ventas y clientes, los limpia, los une y los analiza. Se ejecuta desde un menú en la terminal, y cada opción corresponde a un módulo que vas a completar paso a paso.

Recuerda consultar la guía adjunta en PDF donde se te dará el paso a paso del trabajo.

## Requisitos

- Python 3.10 o superior
- Git (para clonar el repositorio)
- Conocimientos básicos de variables, listas y funciones

## Cómo empezar

1. Clona el repositorio y entra a la carpeta del proyecto:

   ```
   git clone <URL-DEL-REPOSITORIO>
   cd <NOMBRE-DE-LA-CARPETA>
   ```

2. Crea y activa un ambiente virtual. Las instrucciones completas, para Windows y Mac/Linux, están en `LEEME_ambiente.txt`.

3. Instala las librerías:

   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```
   python main.py
   ```

Ejecuta siempre los comandos desde la carpeta del proyecto. Los módulos buscan los archivos a partir de su ubicación.

## Estructura del proyecto

```
├── main.py            Menú principal. No lo modifiques.
├── carga.py           Lee los CSV. Ya está completo.
├── limpieza.py        Limpia clientes y ventas. TODO 1 a 5.
├── merge.py           Valida y une las tablas. TODO 6 y 7.
├── analisis.py        Responde las preguntas de negocio. TODO 8 a 12.
├── graficos.py        Dibuja dos gráficos sencillos. TODO 13 y 14.
├── exploracion.py     Ejemplos de indexación, .loc, .iloc y concat. Se ejecuta por separado.
├── requirements.txt   Versiones de las librerías.
├── LEEME_ambiente.txt Pasos para crear el ambiente virtual.
└── Data/
    ├── raw/           Datos originales (cliente.csv, ventas.csv). No los modifiques.
    └── processed/     Resultados que genera el programa.
```

## Menú

| Opción | Qué hace |
|---|---|
| 1 | Carga los archivos CSV |
| 2 | Limpia los datos |
| 3 | Valida y une las tablas con merge |
| 4 | Muestra el análisis y las respuestas del desafío |
| 5 | Dibuja los gráficos de introducción |
| 6 | Sale del programa |

Las opciones se usan en orden: primero cargar (1), luego limpiar (2), después unir (3) y finalmente analizar (4) o graficar (5).

## Cómo completar el taller

1. Abre el archivo indicado en cada TODO. Cada función tiene un docstring con pistas.
2. Completa el TODO y ejecuta `python main.py` para probar la opción correspondiente.
3. Usa `exploracion.py` para practicar indexación, `.loc`, `.iloc` y `concat()` antes de aplicarlos en tu código.

Las funciones que aún no completaste no dan error: devuelven los datos sin cambios, así que el menú siempre funciona.

## Entregables

Consulta el documento del taller (`guia_Taller_Pandas.pdf`) para ver el detalle de cada entregable y la rúbrica. En resumen:

- Entregable 0: pantallazo del ambiente virtual activo y de la instalación.
- Entregable 1: pantallazos de `.shape`, `.info()` y `.describe()`, y salida de `exploracion.py`.
- Entregable 2: limpieza, con pantallazos antes y después y explicación.
- Entregable 3: validación, merge y análisis, con pantallazos de las opciones 3 y 4.
- Entregable 4: los dos gráficos (`.png`) y el código de `graficos.py`.
- Desafío final: respuestas a las cinco preguntas, con el criterio usado en cada una.

Para entregar, agrega al final de este `README.md` una sección con tu nombre y tus respuestas a las preguntas del desafío. Sube tus cambios al repositorio y envía el enlace por el formulario de entrega. La entrega es individual.

## Preguntas de negocio

1. ¿Qué categoría genera más ingresos?
2. ¿Qué canal vende más?
3. ¿Los clientes VIP compran más que los Regulares?
4. ¿Qué método de pago es el más usado?
5. ¿Cuáles son los cinco clientes con más compras?

---

## Entrega

**Estudiante:** Simón Guarín

### Respuestas del desafío

Los resultados salen de la opción 4 del menú (`python main.py`), después de ejecutar las opciones 1, 2 y 3.

#### 1. ¿Qué categoría genera más ingresos?

```
categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
Name: total, dtype: int64
```

**Respuesta:** Tecnología es la categoría que más ingresos genera, con $14.290.000.
**Criterio:** suma de la columna `total` por categoría, ordenada de mayor a menor.

#### 2. ¿Qué canal vende más?

```
        ventas  ingresos
canal                   
Online      35  14669000
Tienda      33   4507000
```

**Respuesta:** Online es el canal que más vende, con $14.669.000 en ingresos.
**Criterio:** ingresos totales por canal. Online también gana en cantidad de ventas (35 contra 33), así que la respuesta es la misma con los dos criterios.

#### 3. ¿Los clientes VIP compran más que los Regulares?

```
                  clientes  compras     gasto  compras_por_cliente  gasto_por_cliente
segmento_cliente                                                                     
Regular                 36       39  11110000                 1.08           308611.0
VIP                     24       29   8066000                 1.21           336083.0
```

**Respuesta:** Sí. Cada cliente VIP gasta en promedio $336.083 contra $308.611 de un cliente Regular, y hace 1,21 compras contra 1,08.
**Criterio:** promedio por cliente (total dividido entre el número de clientes distintos de cada segmento). No se usan los totales porque hay 36 clientes Regular y solo 24 VIP, y por eso los Regulares suman más aunque cada uno compre menos.

#### 4. ¿Qué método de pago es el más usado?

```
metodo_pago
Efectivo         30
Tarjeta          25
Transferencia    13
Name: count, dtype: int64
```

**Respuesta:** Efectivo es el método de pago más usado, con 30 ventas.
**Criterio:** número de ventas por método de pago (`value_counts()`).

#### 5. ¿Cuáles son los cinco clientes con más compras?

```
                             compras  gasto_total
id_cliente nombre_cliente                        
21         Nicolas Cardona         2      2515000
35         Matias Rodriguez        2      1278000
52         Mia Quintero            2      1090000
58         Luna Montoya            2      1007000
3          Luis Perez              2       730000
```

**Respuesta:** Nicolás Cardona, Matías Rodríguez, Mía Quintero, Luna Montoya y Luis Pérez.
**Criterio:** número de compras de mayor a menor. Como todos tienen 2 compras, el desempate es el gasto total.

### Bonus: ventas por mes

```
mes
2026-04    18234000
2026-05      942000
Freq: M, Name: total, dtype: int64
```

**Respuesta:** abril de 2026 fue el mes que más vendió, con $18.234.000.

### Explicaciones de los entregables

- **¿Por qué `.iloc[2, 6]` devuelve el total de V003?** Después de `set_index("id_venta")`, `id_venta` deja de ser columna. Contando desde 0, las columnas quedan así: id_cliente (0), fecha_venta (1), producto (2), categoria (3), cantidad (4), precio_unitario (5) y total (6). La fila en la posición 2 es V003, así que `.iloc[2, 6]` es su total.
- **Limpieza:** los datos venían casi limpios. Solo había un nulo, en el `producto` de la venta V004, y ninguna fila duplicada en las dos tablas. Además, `fecha_venta` venía como texto. Se quitaron los espacios sobrantes de los textos, la ciudad se puso en formato título, el producto vacío se rellenó con "Sin especificar", la fecha se convirtió a datetime con formato `%Y-%m-%d` y se eliminaron duplicados por si los hubiera.
- **¿Por qué `fillna` y no `dropna`?** La venta V004 no tiene nombre de producto, pero sí tiene un total real de $780.000. Con `dropna` se habría perdido ese dinero y los ingresos quedarían mal calculados.
- **Columnas del merge:** ventas tiene 10 columnas y clientes 5. La columna en común (`id_cliente`) aparece una sola vez en el resultado, así que quedan 10 + 5 − 1 = 14. Las filas siguen siendo 68 porque `how="left"` conserva todas las ventas y `validate="m:1"` garantiza que cada venta se une con un solo cliente.

### Evidencias (carpeta `images/`)

Cada pantallazo muestra la terminal con el ambiente `(venv)` activo, el comando ejecutado y su resultado. Cuando la salida no cabe en una pantalla, se divide en varias partes.

- [entregable0_venv_activo_instalacion_librerias](images/entregable0_venv_activo_instalacion_librerias.png)
- [entregable1_salida_exploracion_py](images/entregable1_salida_exploracion_py.png)
- [entregable1_shape_info_describe_ventas_clientes_parte1](images/entregable1_shape_info_describe_ventas_clientes_parte1.png)
- [entregable1_shape_info_describe_ventas_clientes_parte2](images/entregable1_shape_info_describe_ventas_clientes_parte2.png)
- [entregable2_opcion2_limpieza_antes_despues_parte1](images/entregable2_opcion2_limpieza_antes_despues_parte1.png)
- [entregable2_opcion2_limpieza_antes_despues_parte2](images/entregable2_opcion2_limpieza_antes_despues_parte2.png)
- [entregable3_opcion3_validacion_merge_parte1](images/entregable3_opcion3_validacion_merge_parte1.png)
- [entregable3_opcion3_validacion_merge_parte2](images/entregable3_opcion3_validacion_merge_parte2.png)
- [entregable3_opcion4_analisis_completo_parte1](images/entregable3_opcion4_analisis_completo_parte1.png)
- [entregable3_opcion4_analisis_completo_parte2](images/entregable3_opcion4_analisis_completo_parte2.png)
- [entregable3_opcion4_analisis_completo_parte3](images/entregable3_opcion4_analisis_completo_parte3.png)
- [entregable3_opcion4_analisis_completo_parte4](images/entregable3_opcion4_analisis_completo_parte4.png)
- [ventas_por_canal](images/ventas_por_canal.png)
- [ventas_por_categoria](images/ventas_por_categoria.png)
