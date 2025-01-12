import flet as ft

def profile_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Profile", size=24, weight="bold"),
                    ft.Text("Name: John Doe", size=18),
                    ft.Text("Email: john.doe@example.com", size=18),
                    ft.Text("Phone: +1 123-456-7890", size=18),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
