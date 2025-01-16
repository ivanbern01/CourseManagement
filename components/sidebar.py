import flet as ft

# Sidebar Component
def create_sidebar(on_click, dark_mode):
    # Define colors for dark mode and light mode
    sidebar_bg = "#1F1F1F" if dark_mode else "#FFFFFF"
    text_color = "#36013F" if dark_mode else "#4A4A4A"
    icon_color = "#36013F" if dark_mode else "#6C63FF"
    shadow_color = "#000000" if dark_mode else "#D3D3D3"
    divider_color = "#2A2A2A" if dark_mode else "#D3D3D3"
    list_tile_hover_color = "#333333" if dark_mode else "#F0F0F0"

    return ft.Container(
        width=260,
        bgcolor=sidebar_bg,
        padding=20,
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2, color=shadow_color),
        content=ft.Column(
            [
                ft.Text(
                    "Course Management",
                    size=28,
                    weight="bold",
                    color=text_color,
                ),
                ft.Divider(color=divider_color),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.HOME, color=icon_color),
                    title=ft.Text("Home", color=text_color),
                    on_click=lambda e: on_click("Home"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.BOOK, color=icon_color),
                    title=ft.Text("Subjects", color=text_color),
                    on_click=lambda e: on_click("Subjects"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.SCHEDULE, color=icon_color),
                    title=ft.Text("Routine", color=text_color),
                    on_click=lambda e: on_click("Routine"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.VIDEO_CALL, color=icon_color),
                    title=ft.Text("Live Class", color=text_color),
                    on_click=lambda e: on_click("Live Class"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.ASSIGNMENT, color=icon_color),
                    title=ft.Text("To-do", color=text_color),
                    on_click=lambda e: on_click("Assignment"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.SETTINGS, color=icon_color),
                    title=ft.Text("Settings", color=text_color),
                    on_click=lambda e: on_click("Settings"),
                    hover_color=list_tile_hover_color,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.icons.PERSON, color=icon_color),
                    title=ft.Text("Profile", color=text_color),
                    on_click=lambda e: on_click("Profile"),
                    hover_color=list_tile_hover_color,
                ),
            ],
            spacing=15,
        ),
    )
