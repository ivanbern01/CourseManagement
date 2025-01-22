import flet as ft
import requests  # Ensure you have the requests module installed


def login_page(container, set_login_state, navigate_to):
    print("Displaying login view")
    container.controls.clear()  # Clear existing controls in the container

    # Username and password fields
    username_field = ft.TextField(label="Username", autofocus=True)
    password_field = ft.TextField(label="Password", password=True)

    # Create an error message control
    error_message = ft.Text("", color="red", visible=False)  # Initially hidden

    def on_login_click(e):
        username = username_field.value
        password = password_field.value

        # Validate the username and password by sending a request to the backend
        response = requests.post("http://localhost:5000/login", json={"email": username, "password": password})
        
        if response.status_code == 200:
            print(f"User {username} logged in.")
            # Extract user details from the backend response
            response_data = response.json()
            user_email = response_data["email"]
            user_name = f"{response_data['first_name']} {response_data['last_name']}"

            print(f"User Email: {user_email}")  # Debugging log for user_email
            print(f"User Name: {user_name}")  # Debugging log for user_name

            set_login_state(True, user_name=user_name, user_email=user_email)
            navigate_to("Home", user_name=user_name)

        else:
            print("Invalid credentials, please try again.")
            error_message.value = "Invalid username or password."
            error_message.visible = True  
            container.update()  # Update the container to reflect changes




    def redirect_to_register(e):
        print("Redirecting to register page...")
        container.controls.clear()  # Clear the current login page
        from pages.register import register_page
        register_page(container, set_register_state=None, navigate_to=navigate_to)  # Pass navigate_to here

    # Add a clickable button for registering
    register_link = ft.TextButton(
        text="Don't have an account? Register here.",
        on_click=redirect_to_register,  # Now passes the correct function
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(color=ft.colors.BLUE, size=14, weight=ft.FontWeight.BOLD),
        ),
    )

    container.controls.append(
        ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=250),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Login", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.DEEP_PURPLE),
                        username_field,
                        password_field,
                        error_message,
                        ft.ElevatedButton(
                            "Login",
                            on_click=on_login_click,
                            width=150,
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                        ),
                        register_link,  # Add the register link below the login button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Vertical centering
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontal centering
                    spacing=20,
                ),
                width=400,  # Set width to control form size
                bgcolor=ft.colors.WHITE,
                border_radius=12,
                shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.BLACK, spread_radius=2),
                padding=20,
            ),
        )
    )
    container.update()
