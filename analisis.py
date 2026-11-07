import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)
    ventas_por_mes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # TODO 8: calcular e imprimir los ingresos por categoría y la categoría que más ingresa.
    print("\n===== Pregunta 1: ingresos por categoría =====")
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print(ingresos)
    print(f"Respuesta: la categoría con más ingresos es {ingresos.index[0]} "
          f"con ${ingresos.iloc[0]:,.0f} (criterio: suma de la columna total).")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # TODO 9: calcular e imprimir ventas e ingresos por canal.
    print("\n===== Pregunta 2: ventas e ingresos por canal =====")
    por_canal = df.groupby("canal").agg(
        ventas=("id_venta", "count"),
        ingresos=("total", "sum"),
    ).sort_values("ingresos", ascending=False)
    print(por_canal)

    canal_ingresos = por_canal["ingresos"].idxmax()
    canal_ventas = por_canal["ventas"].idxmax()
    print(f"Por ingresos vende más: {canal_ingresos} | Por cantidad de ventas: {canal_ventas}")
    print(f"Respuesta: el canal que más vende es {canal_ingresos} (criterio: ingresos totales).")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # TODO 10: calcular e imprimir compras y gasto promedio por cliente según segmento_cliente.
    print("\n===== Pregunta 3: VIP vs Regular =====")
    resumen = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto=("total", "sum"),
    )
    resumen["compras_por_cliente"] = (resumen["compras"] / resumen["clientes"]).round(2)
    resumen["gasto_por_cliente"] = (resumen["gasto"] / resumen["clientes"]).round(0)
    print(resumen)

    # Línea propia con .loc: tomar el gasto por cliente de cada segmento
    gasto_vip = resumen.loc["VIP", "gasto_por_cliente"]
    gasto_regular = resumen.loc["Regular", "gasto_por_cliente"]
    compras_vip = resumen.loc["VIP", "compras_por_cliente"]
    compras_regular = resumen.loc["Regular", "compras_por_cliente"]

    if gasto_vip > gasto_regular:
        respuesta = "Sí, los clientes VIP gastan más por cliente que los Regulares"
    else:
        respuesta = "No, los clientes VIP no gastan más por cliente que los Regulares"
    print(f"Respuesta: {respuesta} (${gasto_vip:,.0f} vs ${gasto_regular:,.0f}; "
          f"compras por cliente {compras_vip} vs {compras_regular}). "
          f"Criterio: promedio por cliente, no totales.")


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # TODO 11: calcular e imprimir el conteo por método de pago y cuál es el más usado.
    print("\n===== Pregunta 4: método de pago =====")
    conteo = df["metodo_pago"].value_counts()
    print(conteo)
    print(f"Respuesta: el método más usado es {conteo.index[0]} con {conteo.iloc[0]} ventas "
          f"(criterio: número de ventas).")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # TODO 12: calcular e imprimir el top 5.
    print("\n===== Pregunta 5: top 5 clientes =====")
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=[False, False])
        .head(5)
    )
    print(top)
    print("Criterio: número de compras; si hay empate, mayor gasto total.")


def ventas_por_mes(df):
    """Bonus: ventas por mes usando to_period("M")."""
    print("\n===== Bonus: ventas por mes =====")
    df = df.copy()
    df["mes"] = df["fecha_venta"].dt.to_period("M")
    por_mes = df.groupby("mes")["total"].sum()
    print(por_mes)
    print(f"Respuesta: el mes que más vendió fue {por_mes.idxmax()} con ${por_mes.max():,.0f}.")

    # Línea propia con concat: separar por canal y volver a unir para comprobar que no se pierden filas
    online = df.loc[df["canal"] == "Online"]
    tienda = df.loc[df["canal"] == "Tienda"]
    juntas = pd.concat([online, tienda], ignore_index=True)
    print(f"Comprobación con concat: Online {len(online)} + Tienda {len(tienda)} = "
          f"{len(juntas)} filas (merge original: {len(df)}).")
