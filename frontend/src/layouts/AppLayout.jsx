import { useEffect, useState } from 'react';
import { api } from '../API/api';
import Sidebar from '../components/Sidebar';
import './AppLayout.css';

function AppLayout({ children }) {
  const [usuario, setUsuario] = useState(null);

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

  return (
    <div className="app-layout">
      <Sidebar usuario={usuario} />
      <main className="app-layout__content">
        {children}
      </main>
    </div>
  );
}

export default AppLayout;