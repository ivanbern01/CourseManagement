import flet as ft

def assignment_page(container):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Assignments", size=24, weight="bold"),
                    ft.Text("1. Math Homework - Due: 10th Jan", size=18),
                    ft.Text("2. Physics Lab Report - Due: 12th Jan", size=18),
                    ft.Text("3. Chemistry Project - Due: 15th Jan", size=18),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
