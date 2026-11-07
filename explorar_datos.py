"""Entregable 1: exploración de la estructura de ventas.csv y cliente.csv."""
import pandas as pd

from carga import cargar_datos

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 20)

clientes, ventas = cargar_datos()

for nombre, df in [("VENTAS", ventas), ("CLIENTES", clientes)]:
    print(f"\n========== {nombre} ==========")
    print(f"\n{nombre.lower()}.shape:")
    print(df.shape)
    print(f"\n{nombre.lower()}.info():")
    df.info()
    print(f"\n{nombre.lower()}.describe():")
    print(df.describe())

# 4.2 Leer solo algunas columnas con usecols
ventas_reducido = pd.read_csv("Data/raw/ventas.csv", usecols=["producto", "total"])
print("\n========== usecols ==========")
print(ventas_reducido.head())
