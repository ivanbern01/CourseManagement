import flet as ft

def create_top_bar(dark_mode, navigate_to):
    # Colors based on dark mode
    bg_color = "#1E1E1E" if dark_mode else "#FFFFFF"
    text_color = "#FFFFFF" if dark_mode else "#000000"
    dropdown_bg_color = "#2D2D2D" if dark_mode else "#FFFFFF"
    item_text_color = "#FFFFFF" if dark_mode else "#000000"

    # Ref for dropdown container
    dropdown_container = ft.Container(visible=False)

    def toggle_dropdown(e):
        dropdown_container.visible = not dropdown_container.visible
        dropdown_container.update()

    # Dropdown content
    dropdown_container.content = ft.Column(
        [
            # Profile Header
            ft.Container(
                content=ft.Row(
                    [
                        ft.CircleAvatar(
                            content=ft.Text("S", color="white"),
                            bgcolor="#6C63FF",
                            radius=20,
                        ),
                        ft.Column(
                            [
                                ft.Text("Your Name", size=16, color=item_text_color),
                                ft.Text(
                                    "View profile",
                                    size=12,
                                    color="#888888" if not dark_mode else "#CCCCCC",
                                ),
                            ],
                            spacing=2,
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                padding=10,
            ),
            ft.Divider(height=1, thickness=1, color="#555555"),
            # Dropdown Items
            ft.Column(
                [
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=20, color=item_text_color),
                                ft.Text("Profile", size=14, color=item_text_color),
                            ],
                            spacing=10,
                        ),
                        padding=10,
                        on_click=lambda _: navigate_to("profile"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.LOCK, size=20, color=item_text_color),
                                ft.Text("Change Password", size=14, color=item_text_color),
                            ],
                            spacing=10,
                        ),
                        padding=10,
                        on_click=lambda _: navigate_to("change_password"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.LOGOUT, size=20, color=item_text_color),
                                ft.Text("Logout", size=14, color=item_text_color),
                            ],
                            spacing=10,
                        ),
                        padding=10,
                        on_click=lambda _: print("Logged out"),
                    ),
                ],
            ),
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
    )

    # Wrap in a Stack for proper overlay
    return ft.Container(
        content=ft.Row(
            [
                ft.Container(expand=True),  # Placeholder for alignment
                ft.Row(
                    [
                        ft.Icon(ft.icons.NOTIFICATIONS, size=22, color="#6C63FF"),
                        ft.Icon(ft.icons.MESSAGE, size=22, color="#6C63FF"),
                        # Avatar with dropdown toggle
                        ft.Stack(
                            [
                                ft.Container(
                                    content=ft.CircleAvatar(
                                        content=ft.Text("S", color="white"),
                                        bgcolor="#6C63FF",
                                        radius=18,
                                    ),
                                    on_click=toggle_dropdown,
                                ),
                                ft.Container(
                                    content=dropdown_container,
                                    alignment=ft.alignment.top_right,  # Position dropdown correctly
                                    margin=ft.margin.only(top=30),  # Adjust dropdown spacing
                                ),
                            ],
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=15,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=bg_color,
        padding=ft.padding.all(15),
    )
