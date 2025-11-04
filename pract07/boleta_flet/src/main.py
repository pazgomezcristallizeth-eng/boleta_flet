import flet as ft


def main(page: ft.Page):
    page.title = "Boleta de Calificaciones"
    page.bgcolor = ft.Colors.AMBER_ACCENT_700
    
    #lista de los nombres de los alumnos 
    lista_alumnos = ft.Dropdown(
        width = 300,
        label = "Alumno",
        options = [
            ft.dropdown.Option("Valeria Hernandez Garcia"),
            ft.dropdown.Option("Angel Adrian Martinez Torres"),
            ft.dropdown.Option("Andrea Perez Guzman"),
            ft.dropdown.Option("Maria Fernanda Martinez Lopez"),
            ft.dropdown.Option("Rocio Castillo Nuñez"),
            ft.dropdown.Option("Carla Espinosa Hernandez"),
        ],
    )
    
    #dropwrons de las materias
    ing = ft.Dropdown(
        width = 200,
        label = "Ingles",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    mat = ft.Dropdown(
        width = 200,
        label = "Matematicas",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    esp = ft.Dropdown(
        width = 200,
        label = "Español",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    his = ft.Dropdown(
        width = 200,
        label = "Historia",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    emp = ft.Dropdown(
        width = 200,
        label = "Emplea Frameworsks",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    qui = ft.Dropdown(
        width = 200,
        label = "Quimica",
        options = [ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    label_promedio = ft.Text(value="", size=20, width=100, color=ft.Colors.BLACK45)
    
    tabla_calificaciones = ft.DataTable(
        columns= [
            ft.DataColumn(label=ft.Text("Alumno")),
            ft.DataColumn(label=ft.Text("Ingles")),
            ft.DataColumn(label=ft.Text("Matematicas")),
            ft.DataColumn(label=ft.Text("Español")),
            ft.DataColumn(label=ft.Text("Historia")),
            ft.DataColumn(label=ft.Text("Emplea Frameworks")),
            ft.DataColumn(label=ft.Text("Quimica")),
            ft.DataColumn(label=ft.Text("Promedio")),
        ],
        rows=[]
    )
    
def calcular_promedio(e):
    notas = []
    
    
ft.app(main)
