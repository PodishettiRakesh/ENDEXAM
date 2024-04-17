import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function StudentLoginComponent() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
    
        const response = await fetch('http://localhost:5000/verify_login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });
    
        const data = await response.json();
    
        if (data.success && data.role === 'student') {
            sessionStorage.setItem('username', username);
            navigate('/courses');
        } else {
            // Handle login error
            console.log('Login failed');
        }
    };

    return (
        <div>
            <h2>Student Login</h2>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default StudentLoginComponent;
