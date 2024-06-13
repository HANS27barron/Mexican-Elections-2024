import pandas as pd
import numpy as np


file_path = r"C:\Users\hansv\Documents\Senadores.xlsx"
df = pd.read_excel(file_path)

col = ["Estado"]
select = df[col]

estadoS = [ 
 "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Ciudad De México",
    "Coahuila",
    "Colima",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "Estado De México",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas"
]


def sen_Ganador(estado):
    senadores = []
    count = 0
    for index, row in df.iterrows():
        if row["Estado"] == estado:
            senadores.append((row["Partido/Coalición"], row["Nombre"]))
            count += 1
            if count == 2:
                break
    return(pd.DataFrame(senadores, columns=["Partido/Coalición","Nombre"]))


def color_Sen_Ganador(estado):
    res = sen_Ganador(estado)
    partido = res.iloc[0]["Partido/Coalición"]
    if partido==("Movimiento Ciudadano" or "Partido De La Revolución Democrática"):
        return("orange")
    elif partido==("Morena" or "Sigamos Haciendo Historia"):
        return("violet")
    elif partido==("Partido Del Trabajo"):
        return("red")
    elif partido==("Partido Verde Ecologista de México" or "Partido Revolucionario Institucional"):
        return("green")
    elif partido=="Partido Acción Nacional" or "Fuerza y Corazón por México":
        return("blue")

counts = {search_string: 0 for search_string in estadoS}

for search_string in estadoS:
    counts[search_string] = select['Estado'].str.contains(search_string, na=False).sum()

sen = ""
c = []
for state, count in counts.items():
    sen += f"{state} tiene {int(count/2)} candidaturas \n"
    print(int(count/2))
    c.append(int(count/2))
    

chart_data = pd.DataFrame(c, columns=["Candidaturas"], index=estadoS)


def cand_Estado(estado):
    candidato = df[df['Estado'].str.contains(estado, na=False)][["Partido/Coalición", "Nombre"]]
    return candidato




print(cand_Estado("Aguascalientes"))

#print(cand_Estado("Aguascalientes"))

#print(sen)
#print(c)
