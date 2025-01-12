import flet as ft

def create_top_bar():
    return ft.Row(
        [
            ft.Container(
                content=ft.TextField(
                    hint_text="Search here...",
                    width=300,
                    on_change=lambda e: print(f"Searching for: {e.control.value}"),
                ),
                expand=False,
            ),
            ft.Row(
                [
                    ft.Icon(ft.icons.PHONE, size=18, color="#4A4A4A"),
                    ft.Text("(1234) 567 890", size=14, color="#4A4A4A"),
                    ft.Icon(ft.icons.NOTIFICATIONS, size=20, color="#6C63FF"),
                    ft.Icon(ft.icons.MESSAGE, size=20, color="#6C63FF"),
                    ft.CircleAvatar(
                        content=ft.Text("S", color="white"),
                        bgcolor="#6C63FF",
                        radius=18,
                    ),
                    ft.Text("S", size=14, color="#4A4A4A"),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=10,
                expand=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )
