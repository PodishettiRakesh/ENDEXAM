import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StudentLoginPage from './StudentLoginPage'; // Import the StudentLoginPage component
import TeacherPage from './TeacherPage'; // Import the TeacherPage component
import WelcomePage from './WelcomePage';
import CoursesPage from './CoursesPage';
import ErrorPage from './ErrorPage';
import ProtectedRoute from './ProtectedRoute'; // Import the ProtectedRoute component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<StudentLoginPage />} /> {/* Route for student login */}
        <Route path="/teacher" element={<TeacherPage />} /> {/* Route for teacher dashboard */}
        <Route path="/welcome" element={<WelcomePage />} />
        <Route 
            path="/admin" 
            element={
                <ProtectedRoute>
                    <TeacherPage /> {/* Teacher dashboard is protected */}
                </ProtectedRoute>
            } 
        />
        <Route 
            path="/courses" 
            element={
                <ProtectedRoute>
                    <CoursesPage /> {/* Courses page is protected */}
                </ProtectedRoute>
            } 
        />
        <Route path="/error" element={<ErrorPage />} />
      </Routes>
    </Router>
  );
}

export default App;
