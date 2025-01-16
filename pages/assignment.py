import flet as ft

def assignment_page(container, dark_mode):
    # Define theme colors
    card_bg = "blue100" if not dark_mode else "blue800"
    text_color = "black" if not dark_mode else "white"
    subtitle_color = "gray600" if not dark_mode else "white"

    # Assignment data
    assignments = [
        {"title": "Math Homework", "due_date": "10th Jan", "completed": False},
        {"title": "Physics Lab Report", "due_date": "12th Jan", "completed": False},
        {"title": "Chemistry Project", "due_date": "15th Jan", "completed": False},
    ]

    # Function to toggle the completion status of assignments
    def toggle_complete(e, assignment):
        assignment["completed"] = not assignment["completed"]
        update_assignments_view()

    # Function to filter assignments
    def filter_assignments(e):
        selected_filter = filter_dropdown.value
        if selected_filter == "All":
            filtered_assignments = assignments
        elif selected_filter == "Completed":
            filtered_assignments = [a for a in assignments if a["completed"]]
        elif selected_filter == "Pending":
            filtered_assignments = [a for a in assignments if not a["completed"]]
        update_assignments_view(filtered_assignments)

    # Function to create assignment cards
    def create_assignment_card(assignment):
        checkbox = ft.Checkbox(
            value=assignment["completed"],
            on_change=lambda e: toggle_complete(e, assignment),
        )
        return ft.Container(
            content=ft.Row(
                [
                    checkbox,
                    ft.Column(
                        [
                            ft.Text(
                                assignment["title"],
                                size=18,
                                weight="bold",
                                color=text_color if not assignment["completed"] else subtitle_color,
                                italic=assignment["completed"],
                            ),
                            ft.Text(
                                f"Due: {assignment['due_date']}",
                                size=16,
                                color=subtitle_color,
                            ),
                        ],
                        spacing=5,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=card_bg,
            padding=15,
            border_radius=10,
            margin=ft.margin.symmetric(vertical=5),
            shadow=ft.BoxShadow(blur_radius=5, spread_radius=1, color="gray400"),
        )

    # Function to update the assignments view
    def update_assignments_view(filtered_assignments=None):
        if filtered_assignments is None:
            filtered_assignments = assignments

        assignment_list.controls.clear()
        for assignment in filtered_assignments:
            assignment_list.controls.append(create_assignment_card(assignment))
        container.update()

    # Filter dropdown
    filter_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("All"),
            ft.dropdown.Option("Completed"),
            ft.dropdown.Option("Pending"),
        ],
        value="All",
        on_change=filter_assignments,
        label="Filter",
    )

    # Assignment list container
    assignment_list = ft.Column(spacing=10)

    # Add components to the main container
    container.controls.clear()
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Assignments",
                        size=30,
                        weight="bold",
                        color=text_color,
                    ),
                    ft.Text(
                        "Stay on top of your assignments. Mark tasks as complete when you're done!",
                        size=16,
                        color=subtitle_color,
                    ),
                    filter_dropdown,
                    ft.Divider(color="gray400"),
                    assignment_list,
                ],
                spacing=20,
            ),
            padding=20,
        )
    )

    # Initialize the assignments view
    update_assignments_view()
    container.update()
