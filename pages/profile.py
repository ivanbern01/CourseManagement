import flet as ft
import requests  # To make HTTP requests to the backend

def profile_page(container, logout, user_email):
    print(f"Fetching profile for email: {user_email}")  # Debugging log for user_email

    api_url = "http://127.0.0.1:5000/profile"
    try:
        response = requests.get(f"{api_url}?email={user_email}")
        if response.status_code == 200:
            user_data = response.json()
        else:
            print(f"Failed to fetch profile: {response.status_code}, {response.text}")
            user_data = {"first_name": "N/A", "middle_name": "N/A", "last_name": "N/A", "age": "N/A", "course": "N/A", "email": "N/A"}
    except Exception as e:
        print(f"Error fetching profile data: {e}")
        user_data = {"first_name": "Error", "middle_name": "Error", "last_name": "Error", "age": "Error", "course": "Error", "email": "Error"}
    
    ...



    # Update the profile UI
    container.controls.clear()  # Clear existing content
    container.controls.append(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Profile", size=24, weight="bold"),
                    ft.Text(f"Name: {user_data.get('first_name', 'N/A')} {user_data.get('middle_name', 'N/A')} {user_data.get('last_name', 'N/A')}", size=18),
                    ft.Text(f"Age: {user_data.get('age', 'N/A')}", size=18),
                    ft.Text(f"Course: {user_data.get('course', 'N/A')}", size=18),
                    ft.Text(f"Email: {user_data.get('email', 'N/A')}", size=18),
                    # Logout button with larger size and text
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Logout", 
                            on_click=lambda _: logout(),  # Call logout function when clicked
                            style=ft.ButtonStyle(
                                text_style=ft.TextStyle(size=20),  # Increase text size
                                color=ft.colors.DEEP_PURPLE,
                                padding=ft.padding.symmetric(horizontal=30, vertical=15)  # Increase button size via padding
                            )
                        ),
                        padding=10,
                        alignment=ft.alignment.center_left
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        )
    )
