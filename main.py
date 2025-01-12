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
    
    # Dark mode state (use a plain boolean)
    dark_mode = False
    
    # Callback for toggling dark mode
    def toggle_dark_mode(value):
        nonlocal dark_mode
        dark_mode = value
        # Apply a dark mode theme by updating the background color and text color
        page.bgcolor = ft.colors.BLACK if dark_mode else ft.colors.WHITE
        page.color = ft.colors.WHITE if dark_mode else ft.colors.BLACK
        page.update()

    # Callback for page navigation
    def navigate_to(page_name):
        content_container.controls.clear()
        if page_name == "Home":
            home_page(content_container)
        elif page_name == "Subjects":
            subjects_page(content_container)
        elif page_name == "Routine":
            routine_page(content_container)
        elif page_name == "Live Class":
            live_class_page(content_container)
        elif page_name == "Assignment":
            assignment_page(content_container)
        elif page_name == "Settings":
            settings_page(content_container, dark_mode, toggle_dark_mode)
        elif page_name == "Profile":
            profile_page(content_container)
        page.update()

    # Sidebar
    sidebar = create_sidebar(navigate_to)

    # Top bar
    top_bar = create_top_bar()

    # Layout
    page.add(
        ft.Row(
            [
                sidebar,
                ft.Container(
                    content=ft.Column([top_bar, ft.Divider(), content_container], spacing=20, expand=True),
                    padding=25,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
