import csv
from openpyxl import load_workbook
import pandas as pd

## https://joserzapata.github.io/courses/python-ciencia-datos/pandas/

CARPETA_DATOS = "z:\\RPA\\PRE\\DATAIN\\ROBI\\"
VERBOSE = False


def imprime_nulos(pd, campo):
    diferentes = []
    for ind in pd.index:
        exp = pd.loc[ind]
        if len(str(exp[campo])) < 5:
            diferentes.append(exp[campo])
    print("{}: {}".format(campo, set(diferentes)))       


# Listado de expedientes del procedimiento de DC de Sede Electrónica
def carga_sede_docuconta(eliminar_duplicados):
    print("Cargando datos de los expedientes de Sede de los DC de la carpeta {}".format(CARPETA_DATOS))
    pd_sede_docuconta = pd.read_excel(CARPETA_DATOS + "Sede_Docuconta.xlsx", engine="openpyxl")
    if VERBOSE:
        print(pd_sede_docuconta.info())
        print(pd_sede_docuconta.dtypes)
    if eliminar_duplicados:
        pd_sede_docuconta = pd_sede_docuconta.drop_duplicates(["Codigo Expediente"])
    pd_sede_docuconta.set_index(["Codigo Expediente"], inplace=True)
    pd_sede_docuconta.fillna(0, inplace=True)   # hacemos que todos los nulos valgan cero
    print("Cargados {} expedientes de DC de la sede".format(len(pd_sede_docuconta)))
    if VERBOSE:
        pd_sede_docuconta = pd_sede_docuconta.astype({'F Cierre Exp': 'object'})
        print(pd_sede_docuconta)
        print(pd_sede_docuconta.info())
        print(pd_sede_docuconta.dtypes)
        pd_sede_docuconta.describe()
        # Para chequeo de diferentes valores en columnas
        imprime_nulos(pd_sede_docuconta, "Tarea Start Date")
        imprime_nulos(pd_sede_docuconta, "Tarea End Date")
        imprime_nulos(pd_sede_docuconta, "F Cierre Exp")
    return(pd_sede_docuconta)

#VERBOSE=True
#carga_sede_docuconta(eliminar_duplicados=True)

# Listado de Documentos Contables de UXXI-EC de los años pasados como argumento
def carga_DC(anios, eliminar_duplicados):
    print("Cargando datos de DC de los años: ", anios, " de la carpeta {}".format(CARPETA_DATOS))
    pd_DC = pd.read_excel(CARPETA_DATOS + "Docuconta_" + anios[0] + ".xlsx", engine="openpyxl")
    for anio in anios[1:]:
        pd_DC2 = pd.read_excel(CARPETA_DATOS + "Docuconta_" + anio + ".xlsx")
        pd_DC = pd.concat([pd_DC, pd_DC2])
    if VERBOSE:
        print("Cargados {} DC".format(len(pd_DC)))
        print(pd_DC.info())
        print(pd_DC.dtypes)
    if eliminar_duplicados:
        pd_DC = pd_DC.drop_duplicates(["Strnumerodocumento"])
    pd_DC.set_index(["Strnumerodocumento"], inplace=True)
    print("Cargados {} DC".format(len(pd_DC)))
    if VERBOSE:
        print(pd_DC)
        print(pd_DC.info())
        print(pd_DC.dtypes)
        pd_DC.describe()
    return(pd_DC)


# Listado de detalle de tareas del procedimiento de DC de Sede Electrónica
def carga_sede_docuconta_tareas(eliminar_duplicados):
    print("Cargando datos de las tareas de los expedientes de Sede de la carpeta {}".format(CARPETA_DATOS))
    pd_sede_docuconta_tareas = pd.read_excel(CARPETA_DATOS + "Sede_Docuconta_Tareas.xlsx", engine="openpyxl")
    if VERBOSE:
        print(pd_sede_docuconta_tareas.info())
        print(pd_sede_docuconta_tareas.dtypes)
    if eliminar_duplicados:  # de momento no tiene sentido eliminar duplicados, se deja por compatibilidad y futuros usos
        pass
        #pd_sede_docuconta = pd_sede_docuconta.drop_duplicates(["Codigo Expediente"])
    #pd_sede_docuconta.set_index(["Codigo Expediente"], inplace=True)  # No existe un índica claro, se deja por compatibilidad y usos futuros
    print("Cargados {} expedientes de DC de la sede".format(len(pd_sede_docuconta_tareas)))
    if VERBOSE:
        print(pd_sede_docuconta_tareas)
        print(pd_sede_docuconta_tareas.info())
        print(pd_sede_docuconta_tareas.dtypes)
        pd_sede_docuconta_tareas.describe()
    return(pd_sede_docuconta_tareas)


# Listado de Justificantes de Gasto de UXXI-EC de los años pasados como argumento
def carga_JG(anios, eliminar_duplicados):
    print("Cargando datos de JG de los años: ", anios, " de la carpeta {}".format(CARPETA_DATOS))
    pd_JG = pd.read_excel(CARPETA_DATOS + "Datos_" + anios[0] + ".xlsx", engine="openpyxl" )
    for anio in anios[1:]:
        pd_JG2 = pd.read_excel(CARPETA_DATOS + "Datos_" + anio + ".xlsx" )
        pd_JG = pd.concat([pd_JG, pd_JG2])
    if VERBOSE:
        print("Cargados {} JG".format(len(pd_JG)))
        print(pd_JG.info())
        print(pd_JG.dtypes)

    if eliminar_duplicados:
        pd_JG.drop_duplicates(["Strnumerofactura"], inplace= True)
    
    pd_JG.set_index(["Strnumerofactura"], inplace=True)
    pd_JG.fillna(0, inplace=True)   # hacemos que todos los nulos valgan cero

    print("Número de JGs                     {}".format(len(pd_JG)))
    pd_JG.drop(pd_JG[pd_JG["Datfechaanulacion"] != 0].index, inplace= True) 
    print("Número de JGs borrados anulados   {}".format(len(pd_JG)))
    pd_JG.drop(pd_JG[pd_JG["Datfecharechazo"] != 0].index, inplace= True) 
    print("Número de JGs borrados rechazados {}".format(len(pd_JG)))


    if VERBOSE:
        print(pd_JG)
        print(pd_JG.info())
        print(pd_JG.dtypes)
        pd_JG.describe()
    return(pd_JG)

VERBOSE=False
carga_JG(["2022"], eliminar_duplicados= True)
