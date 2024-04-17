import socket

host = 'localhost'
port = 8080
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()

print(f'The server is listening on http://{host}:{port}')

# Static usernames and passwords for student and teacher
student_credentials = {'username': 'student', 'password': 'studentpass'}
teacher_credentials = {'username': 'teacher', 'password': 'teacherpass'}

def render_page(page_name):
    with open(f'{page_name}.html', 'r') as file:
        html_content = file.read()
    headers = "HTTP/1.1 200 OK\r\n"
    headers += "Content-Type: text/html\r\n\r\n"
    headers += html_content
    return headers

def handle_request(client_socket):
    data = client_socket.recv(1024).decode()
    request = data.split('\r\n')
    request_line = request[0].split()
    request_type = request_line[0]
    request_msg = request_line[1]

    if request_msg == '/' and request_type == 'GET':
        response = render_page('student_login')
        client_socket.send(response.encode())
    
    elif request_msg == '/student-login' and request_type == 'POST':
        # Extract username and password from request body
        body = request[-1]
        username = body.split('=')[1].split('&')[0]
        password = body.split('=')[2]
        
        # Check if credentials match student credentials
        if username == student_credentials['username'] and password == student_credentials['password']:
            response = "HTTP/1.1 200 OK\r\n\r\nLogin Successful"
        else:
            response = "HTTP/1.1 401 Unauthorized\r\n\r\nInvalid credentials"
        client_socket.send(response.encode())

    elif request_msg == '/teacher-login' and request_type == 'GET':
        response = render_page('teacher_login')
        client_socket.send(response.encode())

    elif request_msg == '/teacher-login' and request_type == 'POST':
        # Extract username and password from request body
        body = request[-1]
        username = body.split('=')[1].split('&')[0]
        password = body.split('=')[2]
        
        # Check if credentials match teacher credentials
        if username == teacher_credentials['username'] and password == teacher_credentials['password']:
            response = "HTTP/1.1 200 OK\r\n\r\nLogin Successful"
        else:
            response = "HTTP/1.1 401 Unauthorized\r\n\r\nInvalid credentials"
        client_socket.send(response.encode())

while True:
    client_socket, client_address = server_socket.accept()
    handle_request(client_socket)
