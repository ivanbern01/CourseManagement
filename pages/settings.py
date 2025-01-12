import flet as ft

def settings_page(container, dark_mode, toggle_dark_mode):
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Settings", size=24, weight="bold"),
                    ft.Switch(label="Enable Notifications"),
                    ft.Switch(label="Dark Mode", value=dark_mode, on_change=lambda e: toggle_dark_mode(e.control.value)),
                    ft.Switch(label="Auto Updates"),
                ],
                spacing=15,
            ),
            padding=20,
        )
    )
