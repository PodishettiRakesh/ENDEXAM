import socket
import psycopg2

host = 'localhost'
port = 8080
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()

print(f'The server is listening on http://{host}:{port}')

# Database connection parameters
dbname = "postgres"
user = "postgres"
password = "Rakesh062"
host = "localhost"
port = "5432"

# Establish database connection
connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = connection.cursor()

# Static usernames and passwords for student and teacher logins
student_credentials = {'student1': 'password1', 'student2': 'password2'}
teacher_credentials = {'teacher1': 'password1', 'teacher2': 'password2'}

def handle_student_login(username, password):
    if username in student_credentials and student_credentials[username] == password:
        return "Student login successful!"
    else:
        return "Invalid username or password for student."

def handle_teacher_login(username, password):
    if username in teacher_credentials and teacher_credentials[username] == password:
        return "Teacher login successful!"
    else:
        return "Invalid username or password for teacher."

def handle_request(request):
    request_lines = request.split('\n')
    request_type = request_lines[0].split()[0]
    if request_type == 'GET':
        if 'student-login.html' in request:
            return open('student-login.html', 'rb').read()
        elif 'teacher-login.html' in request:
            return open('teacher-login.html', 'rb').read()
    elif request_type == 'POST':
        if 'student-login' in request:
            username = request.split('\n')[-1].split('=')[-1].split('&')[0]
            password = request.split('\n')[-1].split('=')[-1].split('&')[1]
            return handle_student_login(username, password)
        elif 'teacher-login' in request:
            username = request.split('\n')[-1].split('=')[-1].split('&')[0]
            password = request.split('\n')[-1].split('=')[-1].split('&')[1]
            return handle_teacher_login(username, password)
    return "404 Not Found"


while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    response = handle_request(request)
    client_socket.sendall(response.encode())
    client_socket.close()
