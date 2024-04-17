document.getElementById("teacherLoginForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent the default form submission
    const formData = new FormData(this);

    try {
        const response = await fetch('/teacher-login', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            alert('Login Successful');
        } else {
            alert('Invalid credentials');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
