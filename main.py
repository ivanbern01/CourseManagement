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
from pages.login_page import login_page  # Import the login page function
from pages.register import register_page

def main(page: ft.Page):
    # Content container
    content_container = ft.Column([], expand=True)

    # Dark mode state
    dark_mode = False

    # Login state
    logged_in = False
    
    # Register state
    registered = False

    # Logged-in user's email
    logged_in_user_email = None  # Initialize as None

    # Logout function
    def logout():
        print("Logging out...")
        nonlocal logged_in_user_email
        logged_in_user_email = None  # Clear the logged-in user's email
        content_container.controls.clear()
        # Clear session and update UI
        page.session.clear()
        set_login_state(False)  # Log the user out by setting login state to False
        page.go("/login")  # Redirect to login page
        login_page(page, set_login_state, navigate_to)

    # Callback for toggling dark mode
    def toggle_dark_mode(value):
        nonlocal dark_mode
        dark_mode = value

        # Update page background and text colors
        page.bgcolor = ft.colors.BLACK if dark_mode else ft.colors.WHITE
        page.color = ft.colors.WHITE if dark_mode else ft.colors.BLACK

        # Update sidebar and top bar dynamically
        sidebar.content = create_sidebar(navigate_to, dark_mode)
        top_bar.content = create_top_bar(dark_mode, navigate_to, page, logout)

        page.update()

    # Callback for page navigation
    def navigate_to(page_name, user_name=None):
        if not user_name:
            user_name = page.session.get("user_name")  # Retrieve user from session storage

        print(f"Navigating to: {page_name} as {user_name}")
        content_container.controls.clear()
        
        if page_name == "Home":
            if user_name:
                home_page(content_container, user_name)
            else:
                content_container.controls.append(
                    ft.Text("Error: No username provided for the Home page.", color="red")
                )
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
            profile_page(content_container, logout, user_email=logged_in_user_email)
        elif page_name == "Change Password":
            content_container.controls.append(
                ft.Text("Change Password Screen", size=20)
            )
        elif page_name == "Register":
            register_page(content_container, set_register_state, navigate_to)
        else:
            content_container.controls.append(
                ft.Text("Page not found", color="red", size=20)
            )

        # Update the page without re-adding the container
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
        content=create_top_bar(dark_mode, navigate_to, page, logout),  # Pass the logout function here
        height=80,  # Fixed height for the top bar
        bgcolor="#FFFFFF",  # Background color for the top bar
        expand=False,
    )

    # Callback for setting login state
    def set_login_state(state, user_name=None, user_email=None):
        nonlocal logged_in, logged_in_user_email
        logged_in = state
        if user_email:
            logged_in_user_email = user_email  # Store the email globally

        if logged_in:
            # Ensure page is cleared and main layout is displayed
            page.controls.clear()
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

            # Store user name in session to persist between page switches
            page.session.set("user_name", user_name)
            navigate_to("Home", user_name=user_name)


    # Callback for setting register state
    def set_register_state(state):
        print(f"Register state set to: {state}")
        nonlocal registered
        registered = state
        if registered:
            print("User registered successfully!")
            # Redirect to login page
            page.controls.clear()
            login_page(page, set_login_state, navigate_to)
            page.update()



    # Initially show the login page
    login_page(page, set_login_state, navigate_to)
    

ft.app(target=main, view=ft.WEB_BROWSER)
