file_path = r"C:\Users\hansv\Downloads\borrar\Téllez.txt"
newFile = ""

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            newFile+=(line+"\n")
            if 'str' in line:
             break
except FileNotFoundError:
    newFile = "File not found."
except Exception as e:
    newFile = f"An error occurred: {e}"