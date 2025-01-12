import flet as ft

def create_sidebar(on_click):
    return ft.Container(
        width=260,
        bgcolor="#FFFFFF",
        padding=20,
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(blur_radius=15, spread_radius=5, color="#D3D3D3"),
        content=ft.Column(
            [
                ft.Text("Course Management", size=28, weight="bold", color="#4A4A4A"),
                ft.Divider(),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.HOME, color="#6C63FF"),
                    title=ft.Text("Home"),
                    on_click=lambda e: on_click("Home"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.BOOK, color="#6C63FF"),
                    title=ft.Text("Subjects"),
                    on_click=lambda e: on_click("Subjects"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.SCHEDULE, color="#6C63FF"),
                    title=ft.Text("Routine"),
                    on_click=lambda e: on_click("Routine"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.VIDEO_CALL, color="#6C63FF"),
                    title=ft.Text("Live Class"),
                    on_click=lambda e: on_click("Live Class"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.ASSIGNMENT, color="#6C63FF"),
                    title=ft.Text("Assignment"),
                    on_click=lambda e: on_click("Assignment"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.SETTINGS, color="#6C63FF"),
                    title=ft.Text("Settings"),
                    on_click=lambda e: on_click("Settings"),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.PERSON, color="#6C63FF"),
                    title=ft.Text("Profile"),
                    on_click=lambda e: on_click("Profile"),
                ),
            ],
            spacing=15
        ),
    )
