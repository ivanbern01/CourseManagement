import flet as ft
from components.sidebar import create_sidebar
from components.top_bar import create_top_bar
from pages.home import home_page
from pages.subjects import subjects_page
from pages.routine import routine_page
from pages.live_class import live_class_page
from pages.assignment import assignment_page
from pages.settings import settings_page
from pages.profile import profile_page

def main(page: ft.Page):
    # Content container
    content_container = ft.Column([], expand=True)
    
    # Dark mode state
    dark_mode = False

    # Callback for toggling dark mode
    def toggle_dark_mode(value):
        nonlocal dark_mode
        dark_mode = value

        # Update page background and text colors
        page.bgcolor = ft.colors.BLACK if dark_mode else ft.colors.WHITE
        page.color = ft.colors.WHITE if dark_mode else ft.colors.BLACK

        # Update sidebar and top bar dynamically
        sidebar.content = create_sidebar(navigate_to, dark_mode)
        top_bar.content = create_top_bar(dark_mode, navigate_to)
        
        page.update()

    # Callback for page navigation
    def navigate_to(page_name):
        print(f"Navigating to: {page_name}")
        content_container.controls.clear()
        if page_name == "Home":
            home_page(content_container)
        elif page_name == "Subjects":
            subjects_page(content_container, dark_mode)
        elif page_name == "Routine":
            routine_page(content_container, dark_mode)
        elif page_name == "Live Class":
            live_class_page(content_container)
        elif page_name == "Assignment":
            assignment_page(content_container, dark_mode)
        elif page_name == "Settings":
            settings_page(content_container, dark_mode, toggle_dark_mode)
        elif page_name == "Profile":
            profile_page(content_container)
        elif page_name == "Change Password":
            content_container.controls.append(
                ft.Text("Change Password Screen", size=20)
            )
        else:
            content_container.controls.append(
                ft.Text("Page not found", color="red", size=20)
            )
        page.update()

    # Sidebar
    sidebar = ft.Container(
        content=create_sidebar(navigate_to, dark_mode),  # Pass initial dark mode state
        width=260,  # Fixed width for the sidebar
        bgcolor="#FFFFFF",  # Background color for the sidebar
        expand=False,
    )

    # Top bar
    top_bar = ft.Container(
        content=create_top_bar(dark_mode, navigate_to),  # Pass initial dark mode state
        height=80,  # Fixed height for the top bar
        bgcolor="#FFFFFF",  # Background color for the top bar
        expand=False,
    )

    # Layout
    page.add(
        ft.Column(
            [
                # Top bar spans the full width
                top_bar,
                # Row for sidebar and content area
                ft.Row(
                    [
                        sidebar,
                        ft.Container(
                            content=ft.Column(
                                [content_container],  # Main content container
                                expand=True,
                            ),
                            expand=True,
                            padding=20,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

    # Set initial page appearance
    page.bgcolor = ft.colors.WHITE
    page.color = ft.colors.BLACK
    page.update()

    # Load the default page
    navigate_to("Home")

ft.app(target=main, view=ft.WEB_BROWSER)
