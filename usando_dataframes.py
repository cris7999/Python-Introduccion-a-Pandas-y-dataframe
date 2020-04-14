import pandas as pd

paises = ["Espannnnnna","China", "India", "Peru"]
poblaciones = [0.45,1.6,1.2,0.22]
mi_diccionario = {"Paises":paises, "Poblacion":poblaciones}

poblacion = pd.DataFrame(mi_diccionario)


poblacion.index = ["ES","CH","IN","PE"]

print(poblacion)

#loc utiliza la etiqueta
#iloc utiliza la posicion
print(poblacion.loc["IN"])