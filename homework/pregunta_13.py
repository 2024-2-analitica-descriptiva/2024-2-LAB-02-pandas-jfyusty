"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    import pandas as pd

    # Cargar el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Cargar el archivo tbl2.tsv
    tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='\t')

    # Realizar un merge entre tbl0 y tbl2 en la columna 'c0'
    merged_tbl = pd.merge(tbl0, tbl2, on='c0')

    # Calcular la suma de 'c5b' agrupada por 'c1' de tbl0
    suma_c5b_por_c1 = merged_tbl.groupby('c1')['c5b'].sum()

    return suma_c5b_por_c1

# Llamar a la función y obtener los resultados
pg_13 = pregunta_13()
print(pg_13)
