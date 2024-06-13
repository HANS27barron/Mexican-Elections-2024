import pandas as pd
import numpy as np

file_path = r"C:\Users\hansv\Downloads\PRES.xlsx"
df = pd.read_excel(file_path)

estados = ["AGUASCALIENTES", "BAJA CALIFORNIA"]

sums = {estado: {"PRI": 0, "PAN": 0, "PRD": 0, "PAN_PRI_PRD":0, "PAN_PRI":0, "PAN_PRD":0, "PRI_PRD":0, 
                 "MORENA":0, "PT":0, "PVEM":0, "PVEM_PT_MORENA":0, "PVEM_PT":0, "PVEM_MORENA":0, "PT_MORENA":0,
                 "MC":0, "NULOS":0, "TOTAL_VOTOS_SACADOS":0} for estado in estados}

for i, row in df.iterrows():
    estado = row["ENTIDAD"]
    if estado in estados:

        sums[estado]["PRI"] += row['PRI'] if isinstance(row['PRI'], (int, float)) else 0
        sums[estado]["PAN"] += row['PAN'] if isinstance(row['PAN'], (int, float)) else 0
        sums[estado]["PRD"] += row['PRD'] if isinstance(row['PRD'], (int, float)) else 0
        sums[estado]["PAN_PRI_PRD"] += row['PAN_PRI_PRD'] if isinstance(row['PAN_PRI_PRD'], (int, float)) else 0
        sums[estado]["PAN_PRI"] += row['PAN_PRI'] if isinstance(row['PAN_PRI'], (int, float)) else 0
        sums[estado]["PAN_PRD"] += row['PAN_PRD'] if isinstance(row['PAN_PRD'], (int, float)) else 0
        sums[estado]["PRI_PRD"] += row['PRI_PRD'] if isinstance(row['PRI_PRD'], (int, float)) else 0

        sums[estado]["MORENA"] += row['MORENA'] if isinstance(row['MORENA'], (int, float)) else 0
        sums[estado]["PT"] += row['PT'] if isinstance(row['PT'], (int, float)) else 0
        sums[estado]["PVEM"] += row['PVEM'] if isinstance(row['PVEM'], (int, float)) else 0
        sums[estado]["PVEM_PT_MORENA"] += row['PVEM_PT_MORENA'] if isinstance(row['PVEM_PT_MORENA'], (int, float)) else 0
        sums[estado]["PVEM_PT"] += row['PVEM_PT'] if isinstance(row['PVEM_PT'], (int, float)) else 0
        sums[estado]["PVEM_MORENA"] += row['PVEM_MORENA'] if isinstance(row['PVEM_MORENA'], (int, float)) else 0
        sums[estado]["PT_MORENA"] += row['PT_MORENA'] if isinstance(row['PT_MORENA'], (int, float)) else 0

        sums[estado]["MC"] += row['MC'] if isinstance(row['MC'], (int, float)) else 0
        sums[estado]["NULOS"] += row['NULOS'] if isinstance(row['NULOS'], (int, float)) else 0
        sums[estado]["TOTAL_VOTOS_SACADOS"] += row['TOTAL_VOTOS_SACADOS'] if isinstance(row['TOTAL_VOTOS_SACADOS'], (int, float)) else 0

for estado in sums:
    Xochitl = sums[estado]["PRI"] + sums[estado]["PAN"] + sums[estado]["PRD"] + sums[estado]["PAN_PRI_PRD"] + sums[estado]["PAN_PRI"] + sums[estado]["PAN_PRD"] + sums[estado]["PRI_PRD"]
    Sheinbaum = sums[estado]["MORENA"] + sums[estado]["PT"] + sums[estado]["PVEM"] + sums[estado]["PVEM_PT_MORENA"] + sums[estado]["PVEM_PT"] + sums[estado]["PVEM_MORENA"] + sums[estado]["PT_MORENA"]
    Maynez = sums[estado]["MC"]
    votos = sums[estado]["TOTAL_VOTOS_SACADOS"]

    Xochitl_POR = Xochitl/votos*100
    Sheinbaum_POR = Xochitl/votos*100
    Maynez_POR = Xochitl/votos*100
    print(f"{estado} --- (Xochitl): {Xochitl} = {Xochitl_POR}%, (Sheinbaum): {Sheinbaum}= {Sheinbaum_POR}%, (Maynez): {Maynez}= {Maynez_POR}%")