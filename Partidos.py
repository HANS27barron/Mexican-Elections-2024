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

print(c)
chart_Partidos = pd.DataFrame(c, columns=["Candidaturas"], index=partidoS)


chart_Partidos = pd.DataFrame(c, columns=["Candidaturas"], index=partidoS)

print(senadores_partidos)
print(chart_Partidos)


def sen_Partido(partido):
    candidato = df[df['Partido/Coalición'].str.contains(partido, na=False)][["Estado", "Nombre"]]
    return candidato

#print(senadores_partidos)
#print(c) 