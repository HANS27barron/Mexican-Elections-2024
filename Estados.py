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

print(sen)
print(c)
