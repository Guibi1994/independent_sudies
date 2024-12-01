# Las listas se crean con []
lista = [1,2,3,"s"]
lista

# Se acceden como en R, pero la indexación arranca en "0"
lista[0] # Accede al primer elemento
lista[0:3] # Accede los perimeros 3
lista[-1] # Accede al ultimo

# A una lista se pueden agregar elementos con appen y remover con remove
lista2 = lista.append(["HOLA",2])
lista
print(lista2)
#OJO: append y remove, no necesitan declarse como un nuevo objeto para modificar
#   el objeto existente
len(lista+["adios"])
lista