import pandas as pd
import re

def leer_log():
    resultados = []
    bloque_actual = []

    with open('datos/KsqlLog.txt', 'r', encoding='latin1') as archivo:
        for linea in archivo:
            if linea.strip().startswith("Fecha:") and bloque_actual:
                bloque_texto = "".join(bloque_actual)                    
                lineas_limpias = []
                for l in bloque_texto.splitlines():
                    lineas_limpias.append(l)
                resultados.append("\n".join(lineas_limpias).strip())
                bloque_actual = []
            bloque_actual.append(linea)

        if bloque_actual:
            bloque_texto = "".join(bloque_actual)
            lineas_limpias = []
            for l in bloque_texto.splitlines():
                lineas_limpias.append(l)
                resultados.append("\n".join(lineas_limpias).strip())
    return resultados

def orden_pd(resultados):
    filas = []
    for bloque in resultados:
        fila = {}

        m = re.search(r"Fecha:\s*(.*)", bloque)
        fila["fecha"] = m.group(1).strip() if m else None

        b_lower = bloque.lower()
        if "bulk" in b_lower:
            fila["tipo"] = "BULK"
        elif "merge" in b_lower:
            fila["tipo"] = "MERGE"
        elif "with" in b_lower:
            fila["tipo"] = "WITH"
        elif "insert" in b_lower:
            fila["tipo"] = "INSERT"
        elif "select" in b_lower:
            fila["tipo"] = "SELECT"
        elif "update" in b_lower:
            fila["tipo"] = "UPDATE"
        elif "delete" in b_lower:
            fila["tipo"] = "DELETE"
        else:
            fila["tipo"] = None

        m = re.search(r"Pagina:\s*(.*)", bloque)
        fila["pagina"] = m.group(1).strip() if m else None

        m = re.search(r"Usuario:\s*(.*)", bloque)
        fila["usuario"] = m.group(1).strip() if m else None

        m = re.search(
        r"\[SQL Server\](.*?)(?:El valor de la clave duplicada|Número de incidencia|$)",
        bloque,
        re.IGNORECASE | re.DOTALL)

        if m:
            fila["error"] = m.group(1).strip().replace("\n", " ")
        else:
            fila["error"] = None

        fila["texto"] = bloque

        filas.append(fila)
    return pd.DataFrame(filas)

def ordenar_fecha(df, fecha_inicio, fecha_termino):
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    df["anio"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month
    df['day'] = df['fecha'].dt.day
    df_rango = df[(df["fecha"] >= fecha_inicio) & (df["fecha"] <= fecha_termino)]
    return df_rango

def print_resultados(ordenado):
    #   Cuenta las OCURRENCIAS por PÁGINA
    agrupado = (ordenado.groupby(["pagina"]).size().reset_index(name="cantidad"))
    grupo_ord = agrupado.sort_values(by="cantidad", ascending=False)
    grupo_ord.to_csv("datos/conteo_por_pagina.csv", index=False, encoding="utf-8-sig")

    print('OCURRENCIA por pagina')
    print(grupo_ord)
    print('-------------------------------------------------------')
    #   Cuenta las OCURRENCIAS por SENTENCIA (SELECT, INSERT, UPDATE, DELETE)

    agrupado = (ordenado.groupby(["tipo"]).size().reset_index(name="cantidad"))
    grupo_ord = agrupado.sort_values(by="cantidad", ascending=False)
    grupo_ord.to_csv("datos/Ocurrencia_sentencia.csv", index=False, encoding="utf-8-sig")
    print('OCURRENCIA por SENTENCIA')
    print(grupo_ord)
    print('-------------------------------------------------------')
    #   Cuenta las OCURRENCIAS que tiene un USUARIO

    agrupado = (ordenado.groupby(["usuario"]).size().reset_index(name="cantidad"))
    grupo_ord = agrupado.sort_values(by="cantidad", ascending=False)
    grupo_ord.to_csv("datos/Ocurrencia_usuario.csv", index=False, encoding="utf-8-sig")
    print('OCURRENCIA por USUARIO')
    print(grupo_ord)
    print('-------------------------------------------------------')
    #   AGRUPA las OCURRENCIAS por AÑO, MES Y DIA

    agrupado = (ordenado.groupby(["anio", "mes", "pagina"]).size().reset_index(name="cantidad"))
    grupo_ord = agrupado.sort_values(by="cantidad", ascending=False)
    grupo_ord.to_csv("datos/Ocurrencia_yymm.csv", index=False, encoding="utf-8-sig")
    print('OCURRENCIAS agrupados (YY/MM) + pagina')
    print(grupo_ord)

    print('-------------------------------------------------------')
    #   GENERA UNA TABLA CON LAS OCURRENCIAS POR PAGINA, USUARIO, ERROR (MENSAJE), ENTREGA LA CANTIDAD DE OCURRENCIAS
    agrupado = (ordenado.groupby(["pagina", "usuario", "error"]).size().reset_index(name="cantidad"))
    grupo_ord = agrupado.sort_values(by="cantidad", ascending=False)
    grupo_ord.to_csv("datos/Ocurrencia_tipo_infraccion.csv", index=False, encoding="utf-8-sig")
    print('Tabla tipo ocurrencia, infracción, cantidad')
    print(grupo_ord)

resultados = leer_log()
df = orden_pd(resultados)

fecha_inicio = pd.to_datetime("2026-07-20 00:00:00") # fecha modificable // HORA NO
fecha_termino = pd.to_datetime("2026-07-20 23:59:59") # fecha modificable // HORA NO

ordenado = ordenar_fecha(df, fecha_inicio, fecha_termino)
print_resultados(ordenado)