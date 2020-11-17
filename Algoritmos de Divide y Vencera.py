#Programa que despliega un menu con los diferentes algoritmos que resuelven problemas de Divide y venceras
#Realizado por
#Kaiser Obaldia / 8-898-703
#Yeny Ortega / 8-923-1263

#***********************************************************************************************************
#Funcion de busqueda binaria
def binarySearch(arr,low,high,x):
    if low<=high:
        #encontrar el índice medio de la matriz
        mid=int( (low+high)/2  )

        #comprobando si la x está en el medio o no
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            #si x is mayor que la mitad del elemento
            #entonces regresa mid+1 del indice e ignore los elementos de la izquierda
            #Llamando a la funcion de busqueda binaria nuevamente
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
#Fin de la funcion
#***********************************************************************************************************

#***********************************************************************************************************
#Inicio de la Funcion quickSort
def quickSort(arr , low , high):
    if low<high :
        #llamar a la función de partición 
        pi = partition( arr , low ,high )
        #quickSort(arr ,low ,pi-1)
        #quickSort(arr,pi+1,high)

# definición de la función de partición
# esta función toma 3 valores
# matriz, valor más bajo, valor más alto
def partition(arr , low ,high):
    #elegir el último valor como punto de pivote
    pivot = arr[high]

    # var i, se guarda el indice de elementos más pequeños que pivot
    i = (low - 1)
    print("[i][low],[high]-",i,low,high)

    # ahora atravesando la matriz de proporcionar desde el índice 0
    # ponemos elementos más pequeños que pivote al lado izquierdo
    # y elementos más grandes que el pivote al lado derecho del pivote
    # var j utilizado para recorrer la matriz, almacena el índice de la matriz
    
    for j in range(low ,high+1):

        if arr[j] <= pivot :
            #incremento del índice de i
            i=i+1
            print("----------------------")
            print("[loop]for = and i =:",j,i)
            #cambiar el valor más grande (índice i) con pivote
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
            print("------------------------")

   # para el último elemento, aumentamos i por 1 y realizamos swap
    arr[i+1],arr[j] = arr[j],arr[i+1]
    print("last element sort:",arr)
    return(i+1)
#********************************************************************************************************

#********************************************************************************************************
#Inicio de la Función de encuentra el maximo elemento de un array
def arraymax():
    numeros = [3, 5, 10, 8, 5, 45, 55, 100, 200, 2, 7, 8]
    mayor = 0

    for n in numeros:
     if n > mayor:
         mayor = n
    print(mayor)

#*******************************************************************************************************
#Inicio de la Función merge_sort
def merge_sort(lista):
 
   """
   Lo primero que se ve en el psudocódigo es un if que
   comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
   ¿Por que? Ya esta ordenada. 
   """
   if len(lista) < 2:
      return lista
    
    # De lo contrario, se divide en 2
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)
    
# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    # Retornamos el resultados
    return result
#********************************************************************************************************

#MENU De solucion de problemas utilizando algoritmos de divide y venceras
def menu():
    print("[1] opcion 1: Busqueda binaria ")
    print("[2] opcion 2: Método Quicksort.")
    print("[3] opcion 3: Encontrar el elemento máximoen un array")
    print("[4] opcion 4: Merge-Sort")
    print("[0] salir del programa")


menu()
opcion = int(input("Elige el problema a resolver: "))

while opcion != 0:
    if opcion == 1:
        #Resolver el primer problema usando el algoritmo de busqueda binaria
        arr=[10,12,14,19,45,50,55,56,59,60,39]
        size=len(arr)-1
        print(size)
        # tenemos búsqueda de x
        x=50
        #Llamada de función
        result = binarySearch(arr,0,size,x)
        #imprimir el resultado
        if result != -1:
            print("El elemento x se encuentra en el indice %d",result)
        else:
            print("El elemento no se encuentra en el array")

    elif opcion == 2:
        #Resolver el segundo problema usando el algoritmo de Quicksort
        arr=[10,80,80,10,30,90,40,50,70]
        low = 0 
        high = len(arr)
        print("Tamano del array:",high)

        #Llamando a la funcion de quicksort
        quickSort(arr , low , high-1)

        print("----Imprimiendo el arreglo ordenado----")
        print(arr)

    elif opcion == 3:
        #Resolver el tercer problema de encontrar el maximo de un arreglo
        arraymax()
    elif opcion == 4:
        #Resolver el cuarto problema usando el algoritmo de Merge-sort
        # Prueba del algoritmo
        lista = [31,3,88,1,4,2,42]
        merge_sort_result = merge_sort(lista)  
        print(merge_sort_result)
    else:
        print("Opcion invalida")

    print()
    menu()
    opcion = int(input("Ingresa tu opcion: "))

print("Saliendo del programa......")
