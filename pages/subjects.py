import flet as ft

def subjects_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Subjects", size=24, weight="bold"),
                    ft.Text("1. Mathematics", size=18),
                    ft.Text("2. Physics", size=18),
                    ft.Text("3. Chemistry", size=18),
                    ft.Text("4. Biology", size=18),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
