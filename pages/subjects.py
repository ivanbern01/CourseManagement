import flet as ft

def subjects_page(container, dark_mode):
    # Clear the container before adding new content
    container.controls.clear()

    # Subject data
    subjects = [
        {"name": "Mathematics", "color": "blue600", "icon": ft.icons.CALCULATE, "details": "Learn about algebra, calculus, geometry, and more."},
        {"name": "Physics", "color": "green600", "icon": ft.icons.SCIENCE, "details": "Explore mechanics, thermodynamics, and modern physics."},
        {"name": "Chemistry", "color": "red600", "icon": ft.icons.BOOK, "details": "Dive into organic, inorganic, and physical chemistry."},
        {"name": "Biology", "color": "yellow600", "icon": ft.icons.ECO, "details": "Understand genetics, evolution, and ecosystems."},
        {"name": "History", "color": "purple600", "icon": ft.icons.HISTORY, "details": "Study ancient, medieval, and modern world history."},
        {"name": "Geography", "color": "orange600", "icon": ft.icons.PUBLIC, "details": "Learn about physical and human geography, maps, and environments."},
    ]

    # Function to create a flip card layout
    def create_flip_card(subj):
        # Colors based on mode
        front_bg = subj["color"]
        back_bg = "gray800" if dark_mode else "gray300"
        text_color = "white" if dark_mode else "black"

        # Create front and back containers
        front = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(subj["icon"], size=70, color="white"),  # Increased icon size
                    ft.Text(subj["name"], size=20, weight="bold", color="white"),  # Increased text size
                ],
                alignment=ft.alignment.center,
                spacing=15,
            ),
            bgcolor=front_bg,
            border_radius=15,
            padding=25,
            alignment=ft.alignment.center,
        )

        back = ft.Container(
            content=ft.Column(
                [
                    ft.Text(subj["name"], size=22, weight="bold", color=text_color),
                    ft.Text(
                        subj["details"],
                        size=18,
                        color=text_color,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.alignment.center,
                spacing=20,
            ),
            bgcolor=back_bg,
            border_radius=15,
            padding=25,
            alignment=ft.alignment.center,
            opacity=0,  # Initially hidden using opacity
        )

        # Stack to layer the front and back
        flip_card = ft.Stack(
            [
                front,  # Bottom layer
                back,   # Top layer
            ],
            width=220,  # Increased card width
            height=300,  # Increased card height
        )

        # Function to toggle visibility of front and back
        def toggle_flip(e):
            # Toggle opacity for flip effect
            if back.opacity == 0:
                back.opacity = 1
                front.opacity = 0
            else:
                back.opacity = 0
                front.opacity = 1

            # Update the flip card
            front.update()
            back.update()

        # GestureDetector to handle tap action
        gesture_detector = ft.GestureDetector(
            content=flip_card,
            on_tap=toggle_flip,  # Trigger the toggle function on tap
        )

        return gesture_detector

    # Grid-based layout for subjects
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Subjects",
                        size=35,
                        weight="bold",
                        color="white" if dark_mode else "blue600",
                    ),
                    ft.GridView(
                        expand=True,
                        runs_count=3,  # Limit to 3 subjects per row
                        max_extent=300,  # Max extent to control the card size
                        spacing=20,  # Increased spacing between cards
                        run_spacing=20,
                        controls=[create_flip_card(subj) for subj in subjects],
                    ),
                ],
                spacing=30,
            ),
            padding=20,
        )
    )
    container.update()
