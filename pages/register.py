import flet as ft
import requests

# URL of the backend registration endpoint
REGISTER_URL = 'http://localhost:5000/register'



def register_page(container, set_register_state, navigate_to):
    print("Displaying register view")
    container.controls.clear()  # Clear existing controls in the container

    # Fields for user registration
    first_name_field = ft.TextField(label="First Name", autofocus=True)
    middle_name_field = ft.TextField(label="Middle Name")
    last_name_field = ft.TextField(label="Last Name")
    age_field = ft.TextField(label="Age", keyboard_type=ft.KeyboardType.NUMBER)
    course_dropdown = ft.Dropdown(
        label="Course",
        options=[ft.dropdown.Option("BSCS"), ft.dropdown.Option("BSIT")],
    )
    email_field = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
    password_field = ft.TextField(label="Password", password=True)

    # Error or success message
    message = ft.Text("", color="red", visible=False)  # Initially hidden

    def on_register_click(e):
        # Collect the values from the fields
        first_name = first_name_field.value
        middle_name = middle_name_field.value
        last_name = last_name_field.value
        age = age_field.value
        course = course_dropdown.value
        email = email_field.value
        password = password_field.value

        # Prepare the payload for the registration API
        payload = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "age": age,
            "course": course,
            "email": email,
            "password": password
        }

        # Make a POST request to the backend
        try:
            response = requests.post(REGISTER_URL, json=payload)

            # Handle the API response
            if response.status_code == 201:
                message.value = "Registration successful!"
                message.color = "green"
                message.visible = True
                set_register_state(True)  # Set register state to True

                # Redirect to login page after successful registration
                from pages.login_page import login_page
                container.controls.clear()  # Clear current register page
                login_page(container, lambda state: None, navigate_to)  # Show login page
            else:
                message.value = response.json().get("message", "Registration failed")
                message.color = "red"
                message.visible = True

        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            message.value = "Error occurred while connecting to the server"
            message.color = "red"
            message.visible = True

        container.update()

    container.update()

    def redirect_to_login(e):
        print("Redirecting to login page...")
        container.controls.clear()  # Clear the current register page
        # Import and display the login page
        from pages.login_page import login_page
        login_page(container, lambda state: None, navigate_to)


    # Add a clickable button for going back to the login page
    login_link = ft.TextButton(
        text="Already have an account? Login here.",
        on_click=redirect_to_login,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(color=ft.colors.BLUE, size=14, weight=ft.FontWeight.BOLD),
        ),
    )

    container.controls.append(
        ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=100),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Register", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.DEEP_PURPLE),
                        first_name_field,
                        middle_name_field,
                        last_name_field,
                        age_field,
                        course_dropdown,
                        email_field,
                        password_field,
                        message,
                        ft.ElevatedButton(
                            "Register",
                            on_click=on_register_click,
                            width=150,
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                        ),
                        login_link,  # Add the login link below the register button
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
