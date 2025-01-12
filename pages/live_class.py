import flet as ft

def live_class_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Live Classes", size=24, weight="bold"),
                    ft.Text("Upcoming Classes:", size=18),
                    ft.Text("1. Math - 10:00 AM", size=16),
                    ft.Text("2. Physics - 2:00 PM", size=16),
                    ft.Text("3. Chemistry - 5:00 PM", size=16),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
