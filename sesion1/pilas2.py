stack = []
size = 0

def push(item, stack, size):
    if len(stack) < size:
        stack.append(item)
    else:
        return "Pila llena..."

def show(stack):
    if isEmpty(stack):
        print("Pila vacía...")
    else:
        for item in reversed(stack):
            print(item)

def peek(stack):
    if isEmpty(stack):
        return "La pila está vacía..."
    return stack[-1]

def isEmpty(stack):
    return not stack

def pop(stack):
    if isEmpty(stack):
        return "La pila está vacía..."
    return stack.pop()

def len_stack(stack):
    if isEmpty(stack):
        return "La pila está vacía..."
    return len(stack)

# Pedir tamaño inicial de la pila
while True:
    try:
        size = int(input("Dime el tamaño de la pila: "))
        break
    except ValueError:
        print("Valor no válido. Ingrese un valor entero.")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Push (Apilar)")
    print("2. Pop (Desapilar)")
    print("3. Peek (Ver elemento superior)")
    print("4. Mostrar pila")
    print("5. Tamaño de la pila")
    print("6. Salir")
    
    opc = input("Seleccione una opción: ")

    if opc == "1":
        item = input("Ingrese el elemento: ")
        res = push(item, stack, size)
        if res:
            print(res)
    elif opc == "2":
        print("Resultado:", pop(stack))
    elif opc == "3":
        print("Elemento superior:", peek(stack))
    elif opc == "4":
        show(stack)
    elif opc == "5":
        print("Cantidad de elementos:", len_stack(stack))
    elif opc == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")