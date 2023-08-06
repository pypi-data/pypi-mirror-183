import requests
import pandas as pd
import datetime

def select_sprint():

    folder_id = "121685777"
    url = "https://api.clickup.com/api/v2/folder/" + folder_id + "/list"
    
    query = {"archived": "false"}

    headers = {"Authorization": "pk_49672506_V0621PT86LKNHBNGNSU536XZ3OKXHBLC"}

    response = requests.get(url, headers=headers, params=query)

    lists = response.json()["lists"]

    # Muestra al usuario el nombre de cada lista y pide que seleccione una
    print("Selecciona una lista:")
    for i, l in enumerate(lists):
      print(f"{i+1}: {l['name']}")
    index = int(input()) - 1

    # Devuelve el ID de la lista seleccionada
    return lists[index]["id"]


def get_tasks(list_id):

    list_id = str(list_id)
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"
    
    query = {
      "archived": "false",  
      "reverse": "true",
      "subtasks": "true",  
      "include_closed": "true"}
    
    headers = {
      "Content-Type": "application/json",
      "Authorization": "pk_49672506_V0621PT86LKNHBNGNSU536XZ3OKXHBLC"
    }
    
    response = requests.get(url, headers=headers, params=query)
    
    tasks = response.json()
    
    # Convierte el JSON en un DataFrame
    df = pd.json_normalize(tasks, ["tasks"])[["assignees", "time_spent"]]

    # Crea una nueva columna con el username del primer elemento de la lista de assignees
    df["Asignado a"] = df["assignees"].apply(lambda x: x[0]["username"] if x else None)

    # Elimina la columna original de assignees
    df = df.drop("assignees", axis=1)
    
    # Reemplaza los valores NaN por cero
    df["time_spent"] = df["time_spent"].fillna(0)
    
    return df

def select_dev():

    import requests

    list_id = "900800093232"
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/member"

    headers = {"Authorization": "pk_49672506_V0621PT86LKNHBNGNSU536XZ3OKXHBLC"}

    response = requests.get(url, headers=headers)

    data = response.json()["members"]
    
    print("Selecciona un dev:")
    for i, l in enumerate(data):
      print(f"{i+1}: {l['username']}")
    index = int(input()) - 1

    # Devuelve el ID de la lista seleccionada
    return data[index]["username"]



def obtener_tiempo_total():
    
    sprint = select_sprint()
    dev = select_dev()
    
    tasks = get_tasks(sprint)
    
    tasks_filtrado = tasks.loc[tasks["Asignado a"] == dev]
    
    tiempo_total = tasks_filtrado.time_spent.sum()
    
    # Convierte el tiempo total en milisegundos a un objeto timedelta
    tiempo_total = datetime.timedelta(milliseconds=tiempo_total)

    horas, resto = divmod(tiempo_total.total_seconds(), 3600)
    minutos, segundos = divmod(resto, 60)

    # Formatea el tiempo total en horas, minutos y segundos
    tiempo_total_formateado = "{:02d}:{:02d}:{:02d}".format(int(horas), int(minutos), int(segundos))

    tiempo_total_formateado

    return tiempo_total_formateado   

def main():
  data = obtener_tiempo_total()
  print (data)

if __name__ == "__main__":
  main()