document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const errorDiv = document.getElementById('error');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        // Simulating login request (replace with actual API call)
        // For demonstration purposes, hardcoding username and password
        if (username === 'student' && password === 'studentpassword') {
            // Redirect student to dashboard (replace with actual URL)
            window.location.href = 'student-dashboard.html';
        } else if (username === 'teacher' && password === 'teacherpassword') {
            // Redirect teacher to dashboard (replace with actual URL)
            window.location.href = 'teacher-dashboard.html';
        } else {
            errorDiv.textContent = 'Invalid username or password. Please try again.';
        }
    });
});
