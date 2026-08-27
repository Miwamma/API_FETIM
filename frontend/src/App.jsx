import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Medicoes from './pages/Medicoes';
import Consumo from './pages/Consumo';
import Custo from './pages/Custo';
import Perfil from './pages/Perfil';
import ProtectedRoute from './routes/ProtectedRoute';
import AppLayout from './layouts/AppLayout';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/register" />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

        <Route path="/dashboard" element={
          <ProtectedRoute><AppLayout><Dashboard /></AppLayout></ProtectedRoute>
        } />
        <Route path="/medicoes" element={
          <ProtectedRoute><AppLayout><Medicoes /></AppLayout></ProtectedRoute>
        } />
        <Route path="/consumo" element={
          <ProtectedRoute><AppLayout><Consumo /></AppLayout></ProtectedRoute>
        } />
        <Route path="/custo" element={
          <ProtectedRoute><AppLayout><Custo /></AppLayout></ProtectedRoute>
        } />
        <Route path="/perfil" element={
          <ProtectedRoute><AppLayout><Perfil /></AppLayout></ProtectedRoute>
        } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;