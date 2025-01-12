import flet as ft

def routine_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Routine", size=24, weight="bold"),
                    ft.Text("1. Morning: 9:00 AM - Math Class", size=18),
                    ft.Text("2. Afternoon: 1:00 PM - Physics Class", size=18),
                    ft.Text("3. Evening: 4:00 PM - Chemistry Class", size=18),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
