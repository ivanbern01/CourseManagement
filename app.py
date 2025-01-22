from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import bcrypt

app = Flask(__name__)
CORS(app)  # Enable CORS

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",  # Database host
        database="CourseManagement",  # Database name
        user="postgres",  # Your PostgreSQL username
        password="123123"  # Your PostgreSQL password
    )
    return conn

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Get the JSON data from the request
    first_name = data.get('first_name')
    middle_name = data.get('middle_name', '')  # Middle name is optional
    last_name = data.get('last_name')
    age = data.get('age')
    course = data.get('course')
    email = data.get('email')
    password = data.get('password')

    # Validation checks
    if not first_name or not last_name or not age or not course or not email or not password:
        return jsonify({"message": "All fields (except middle name) are required."}), 400

    if not age.isdigit() or int(age) <= 0:
        return jsonify({"message": "Please enter a valid age."}), 400

    if not "@" in email or "." not in email:
        return jsonify({"message": "Please enter a valid email address."}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if the email already exists in the database
        cursor.execute("SELECT * FROM Students WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return jsonify({"message": "Email already exists!"}), 400
        
        # Insert the new student into the Students table
        cursor.execute("""
            INSERT INTO Students (first_name, middle_name, last_name, age, course, email, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, middle_name, last_name, int(age), course, email, hashed_password))

        # Commit the changes
        conn.commit()

        return jsonify({"message": "Registration successful!"}), 201

    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred during registration."}), 500

    finally:
        cursor.close()
        conn.close()

# Route for login (already present in your code)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get the JSON data from the request
    username = data.get('email')
    password = data.get('password')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database for the user by email
    cursor.execute("SELECT * FROM Students WHERE email = %s", (username,))
    user = cursor.fetchone()

    if user:
        # The password in the database is hashed, so we need to compare hashes
        stored_password = user[7]  # Assuming the password is at index 7
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            # Return user details in the response, e.g. first name and last name
            user_details = {
                "first_name": user[1],  # Assuming the first name is at index 1
                "last_name": user[3],   # Assuming the last name is at index 3
                "email": user[6],       # Assuming the email is at index 6
                "message": "Login successful!"
            }
            return jsonify(user_details), 200
        else:
            return jsonify({"message": "Invalid password!"}), 401
    else:
        return jsonify({"message": "User not found!"}), 404
    
        cursor.close()
        conn.close()
    
    
@app.route('/profile', methods=['GET'])
def get_profile():
    email = request.args.get('email')
    
    if not email:
        return jsonify({"message": "Email is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Query the database for the user
        cursor.execute("SELECT first_name, middle_name, last_name, age, course, email FROM Students WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            user_data = {
                "first_name": user[0],
                "middle_name": user[1],
                "last_name": user[2],
                "age": user[3],
                "course": user[4],
                "email": user[5],
            }
            return jsonify(user_data), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        print("Error fetching user data:", e)
        return jsonify({"message": "An error occurred"}), 500
    finally:
        cursor.close()
        conn.close()


    


if __name__ == '__main__':
    app.run(debug=True)
