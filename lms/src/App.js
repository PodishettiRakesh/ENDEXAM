import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StudentLoginComponent from './StudentLoginComponent'; // Import the StudentLoginPage component
import TeacherPage from './TeacherPage'; // Import the TeacherPage component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<StudentLoginComponent />} /> {/* Route for student login */}
        <Route path="/teacher" element={<TeacherPage />} /> {/* Route for teacher dashboard */}
      </Routes>
    </Router>
  );
}

export default App;
