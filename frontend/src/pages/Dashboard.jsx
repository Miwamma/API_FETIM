import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../API/api';

function Dashboard() {
  const [usuario, setUsuario] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function carregarUsuario() {
      try {
        const resposta = await api.get('/users/me');
        setUsuario(resposta.data);
      } catch (erro) {
        console.error(erro);
      }
    }
    carregarUsuario();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  if (!usuario) {
    return <p>Carregando...</p>;
  }

  return (
    <div>
      <h2>Bem-vindo, {usuario.name}!</h2>
      <p>Email: {usuario.email}</p>
      <button onClick={handleLogout}>Sair</button>
    </div>
  );
}

export default Dashboard;