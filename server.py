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

from urllib.parse import urlparse, parse_qs, unquote

def handle_request(client_socket):
    data = client_socket.recv(1024).decode()
    # print("Received data:", data)  # Debugging: Print received data
    request_lines = data.split('\r\n')
    if len(request_lines) > 0:
        request_line = request_lines[0].split()
        if len(request_line) > 1:
            request_type = request_line[0]
            request_url = request_line[1]
        else:
            print("Malformed request line:", request_lines[0])
            return
    else:
        print("Empty request received")
        return

    # Parse request URL to extract path and query parameters
    parsed_url = urlparse(request_url)
    request_path = parsed_url.path
    query_params = parse_qs(parsed_url.query)

    if request_path == '/' and request_type == 'GET':
        response = render_page('student_login')
        client_socket.send(response.encode())
    elif request_path == '/student-login' and request_type == 'POST':
        # Extract username and password from query parameters
        username = unquote(query_params['username'][0])
        password = unquote(query_params['password'][0])
        # Handle student login
        pass
    elif request_path == '/teacher-login' and request_type == 'GET':
        response = render_page('teacher_login')
        client_socket.send(response.encode())
    elif request_path == '/teacher-login' and request_type == 'POST':
        # Extract username and password from query parameters
        username = unquote(query_params['username'][0])
        password = unquote(query_params['password'][0])
        # Handle teacher login
        pass
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"
        client_socket.send(response.encode())

while True:
    client_socket, client_address = server_socket.accept()
    handle_request(client_socket)
