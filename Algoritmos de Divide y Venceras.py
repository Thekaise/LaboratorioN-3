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
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Si el valor actual que estamos viendo es mayor que el pivote
        # está en el lugar correcto (lado derecho del pivote) y podemos movernos hacia la izquierda,
        # al siguiente elemento.
        # También debemos asegurarnos de no haber superado el puntero bajo, ya que
        # indica que ya hemos movido todos los elementos a su lado correcto del pivote
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Proceso opuesto al anterior
        while low <= high and array[low] <= pivot:
            low = low + 1

        
        # Encontramos un valor para alto y bajo que está fuera de servicio
        # o bajo es más alto que alto, en cuyo caso salimos del ciclo
        if low <= high:
            array[low], array[high] = array[high], array[low]
            #El bucle continua
        else:
            # Salimos del bucle
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
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
    print("[3] opcion 3: Encontrar el elemento máximo en un array")
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
        array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
        quick_sort(array, 0, len(array) - 1)
        print("Array ordenado: ", array)

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
