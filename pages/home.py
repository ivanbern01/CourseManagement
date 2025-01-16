import flet as ft

def home_page(container):
    container.controls.append(
        ft.Column(
            [
                ft.Text("Welcome, Bokbok", size=36, weight="bold", color=ft.colors.DEEP_PURPLE),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.icons.SCHOOL, size=40, color=ft.colors.BLUE),
                            ft.Text("Total Class", weight="bold"),
                            ft.Text("40", size=24, weight="bold")
                        ], alignment="center", spacing=5),
                        padding=20,
                        bgcolor=ft.colors.LIGHT_BLUE_100,
                        width=180,
                        height=140,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.icons.BOOK, size=40, color=ft.colors.GREEN),
                            ft.Text("Total Subject", weight="bold"),
                            ft.Text("12", size=24, weight="bold")
                        ], alignment="center", spacing=5),
                        padding=20,
                        bgcolor=ft.colors.LIGHT_GREEN_100,
                        width=180,
                        height=140,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.icons.ASSIGNMENT, size=40, color=ft.colors.BLUE),
                            ft.Text("Assignments", weight="bold"),
                            ft.Text("18", size=24, weight="bold")
                        ], alignment="center", spacing=5),
                        padding=20,
                        bgcolor=ft.colors.BLUE_100,
                        width=180,
                        height=140,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.icons.PERSON, size=40, color=ft.colors.PURPLE),
                            ft.Text("Teachers", weight="bold"),
                            ft.Text("12", size=24, weight="bold")
                        ], alignment="center", spacing=5),
                        padding=20,
                        bgcolor=ft.colors.PURPLE_100,
                        width=180,
                        height=140,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                ], alignment="center", spacing=20),
                ft.Container(
                    content=ft.Text("Upcoming Live Class's Timeline", size=24, weight="bold", color=ft.colors.DEEP_PURPLE),
                    padding=15,
                    alignment=ft.alignment.center_left
                ),
                ft.Container(
                    content=ft.Text("Previous Class Records", size=24, weight="bold", color=ft.colors.DEEP_PURPLE),
                    padding=15,
                    alignment=ft.alignment.center_left
                )
            ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START
        )
    )