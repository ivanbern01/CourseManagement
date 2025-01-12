import flet as ft

def home_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Text("Welcome to Home Page", size=24, weight="bold"),
            alignment=ft.alignment.center,
            padding=20,
        )
    )
