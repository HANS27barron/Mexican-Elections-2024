import pandas as pd
import numpy as np

file_path = r"C:\Users\hansv\Documents\Senadores.xlsx"
df = pd.read_excel(file_path)

col = ["Partido/Coalición"]
select = df[col]

partidoS = [ 
    "Movimiento Ciudadano",
    "Fuerza Y Corazon Por Mexico",
    "Sigamos Haciendo Historia",
    "Morena",
    "Partido Verde Ecologista De México",
    "Partido Del Trabajo",
    "Partido Acción Nacional",
    "Partido Revolucionario Institucional",
    "Partido De La Revolución Democrática"
]

cand_MC = (df["Nombre"])
cand_Fuerza = (df["Nombre"])
cand_Historia = (df["Nombre"])
cand_PT = (df["Nombre"])
cand_PV = (df["Nombre"])
cand_PRI = (df["Nombre"])
cand_PAN = (df["Nombre"])
cand_PRD = (df["Nombre"])

if select.equals("Morena"):
    print[33]

counts = {search_string: 0 for search_string in partidoS}

for search_string in partidoS:
    counts[search_string] = select['Partido/Coalición'].str.contains(search_string, na=False).sum()

senadores_partidos = ""
c = []
for partidO, count in counts.items():
    senadores_partidos += f"{partidO} tiene {int(count/2)} candidaturas \n"
    #print(int(count/2))
    c.append(int(count/2))
    #print(partidO)

chart_Partidos = pd.DataFrame(c, columns=["Candidaturas"], index=partidoS)


chart_Partidos = pd.DataFrame(c, columns=["Candidaturas"], index=partidoS)

print(senadores_partidos)
print(chart_Partidos)


cand_Morena = df[df['Partido/Coalición'].str.contains("Morena", na=False)][["Estado", "Nombre"]]
can_MC = df[df['Partido/Coalición'].str.contains("Movimiento Ciudadano", na=False)][["Estado", "Nombre"]]
cand_Fuerza = df[df['Partido/Coalición'].str.contains("Fuerza Y Corazon Por Mexico", na=False)][["Estado", "Nombre"]]
cand_Historia = df[df['Partido/Coalición'].str.contains("Sigamos Haciendo Historia", na=False)][["Estado", "Nombre"]]
cand_PT = df[df['Partido/Coalición'].str.contains("Partido Del Trabajo", na=False)][["Estado", "Nombre"]]
cand_PV = df[df['Partido/Coalición'].str.contains("Partido Verde Ecologista De México", na=False)][["Estado", "Nombre"]]
cand_PAN = df[df['Partido/Coalición'].str.contains("Partido Acción Nacional", na=False)][["Estado", "Nombre"]]
cand_PRI = df[df['Partido/Coalición'].str.contains("Partido Revolucionario Institucional", na=False)][["Estado", "Nombre"]]
cand_PRD = df[df['Partido/Coalición'].str.contains("Partido De La Revolución Democrática", na=False)][["Estado", "Nombre"]]

#print(senadores_partidos)
#print(c) 