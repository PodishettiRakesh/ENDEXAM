function submitForm() {
    const form = document.getElementById("studentLoginForm");
    const formData = new FormData(form);

    fetch('/student-login', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('Login Successful');
        } else {
            alert('Invalid credentials');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
