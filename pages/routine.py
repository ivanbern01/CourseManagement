import flet as ft

def routine_page(container, dark_mode):
    # Define color schemes
    bg_color = "#333333" if dark_mode else "#f3f4f6"  # Dark grey for dark mode, light grey for light mode
    text_color = "#ffffff" if dark_mode else "#000000"  # White for dark mode, black for light mode
    card_bg_color = "#424242" if dark_mode else "#ffffff"  # Dark card for dark mode, white for light mode
    header_color = "#90caf9" if dark_mode else "#1e88e5"  # Light blue for dark mode, vibrant blue for light mode
    divider_color = "#90caf9" if dark_mode else "#1e88e5"

    # Add the school-themed routine layout
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "My School Routine",
                        size=30,
                        weight="bold",
                        color=header_color,
                        text_align="center",
                    ),
                    ft.Divider(height=5, thickness=2, color=divider_color),
                    ft.GridView(
                        expand=True,
                        max_extent=300,  # Allows up to 3 columns, adjusts based on space
                        spacing=20,
                        padding=10,
                        controls=[
                            create_day_card(
                                "Monday",
                                [
                                    "8:00 AM - Math Class",
                                    "10:00 AM - History Class",
                                    "1:00 PM - Science Lab",
                                ],
                                card_bg_color,
                                text_color,
                                divider_color,
                            ),
                            create_day_card(
                                "Tuesday",
                                [
                                    "9:00 AM - English Class",
                                    "11:00 AM - Art Workshop",
                                    "3:00 PM - Music Class",
                                ],
                                card_bg_color,
                                text_color,
                                divider_color,
                            ),
                            create_day_card(
                                "Wednesday",
                                [
                                    "8:30 AM - Physics Class",
                                    "12:00 PM - PE Class",
                                    "4:00 PM - Computer Lab",
                                ],
                                card_bg_color,
                                text_color,
                                divider_color,
                            ),
                            create_day_card(
                                "Thursday",
                                [
                                    "9:00 AM - Chemistry Class",
                                    "11:30 AM - Geography Class",
                                    "2:30 PM - Debate Club",
                                ],
                                card_bg_color,
                                text_color,
                                divider_color,
                            ),
                            create_day_card(
                                "Friday",
                                [
                                    "8:00 AM - Biology Class",
                                    "10:00 AM - Literature Class",
                                    "1:30 PM - Sports Practice",
                                ],
                                card_bg_color,
                                text_color,
                                divider_color,
                            ),
                        ],
                    ),
                ],
                spacing=20,
                alignment="center",
            ),
            padding=20,
            border_radius=15,
            bgcolor=bg_color,
        )
    )

def create_day_card(day, tasks, bg_color, text_color, divider_color):
    # Helper function to create a card for each day
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    day,
                    size=22,
                    weight="bold",
                    color=text_color,
                ),
                ft.Divider(height=3, color=divider_color),
                ft.Column(
                    controls=[
                        ft.Text(task, size=16, color=text_color) for task in tasks
                    ],
                    spacing=5,
                ),
            ],
            spacing=10,
        ),
        padding=15,
        width=250,
        border_radius=10,
        bgcolor=bg_color,
        shadow=ft.BoxShadow(
            blur_radius=10,
            spread_radius=1,
            color="#b0bec5" if not bg_color.startswith("#4") else "#000000",
        ),
    )
