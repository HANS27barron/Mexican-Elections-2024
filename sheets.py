import pandas as pd

file_path = r"C:\Users\hansv\Documents\Senadores.xlsx"

try:
    df = pd.read_excel(file_path)
    col = ["Estado", "Partido/Coalición", "Nombre"]  
    select = df[col]
    print(select)

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")