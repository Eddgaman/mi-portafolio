import os

runProgram = True
todolist = []

# Función para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("")
    print("Por favor seleccione una opción:")
    print("")
    print("")
    print("1. Crear un tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

# Función para mostrar todas las tareas
def showTodoList():
    global todolist
    print()
    print()
    print("************************************")
    for todo in todolist:
        print(f"{todolist.index(todo) + 1}. {todo}")
    print("************************************")
    print()
    print()

# Función para guardar las tareas en la variable "todolist"
def createTodo():
    os.system("clear") # Windows => os.system("cls")
    global todolist
    print("Crear un nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todolist.append(todo)
    # Mostrar la lista de tareas
    showTodoList()

# Función para marcar una tarea como realizada
def updateTodo():
    global todolist
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere marcar como hecha: "))
    todolist[todoId - 1] = todolist[todoId - 1] + "✅"
    showTodoList()

# Función que nos permite borrar una tarea
def deleteTodo():
    global todolist
    print("Borrar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere borrar: "))
    del todolist[todoId - 1]
    showTodoList()

def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST :.")
    flag = True

    while runProgram:
        while flag:
            showMenuOptions() # aquí invocamos la función para mostrar las opciones del menu.
            option = int(input("Ingresa el número de la opción: "))

            match option:
                case 1:
                    createTodo()
                case 2:
                    updateTodo()
                case 3:
                    deleteTodo()
                case 4:
                    print("Hasta Luego!!!")
                    runProgram = False
                    flag = False
                case _:
                    print("Opción no reconocida. Ingrese una opción válida.")
if __name__ == "__main__":
    main()
