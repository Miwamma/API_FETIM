import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { api } from '../API/api';
import './nomeCadastro.css';

function Login() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [mensagem, setMensagem] = useState({ texto: '', tipo: '' });

  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMensagem({ texto: 'Entrando...', tipo: 'info' });

    try {
      const resposta = await api.post('/users/login', {
        email,
        password: senha,
      });

      localStorage.setItem('access_token', resposta.data.access_token);

      setMensagem({
        texto: 'Login realizado com sucesso!',
        tipo: 'sucesso',
      });

      navigate('/dashboard');

    } catch (erro) {
      if (erro.response?.status === 401) {
        setMensagem({
          texto: erro.response.data.detail,
          tipo: 'erro'
        });
      } else if (erro.response) {
        setMensagem({
          texto: 'Erro ao fazer login.',
          tipo: 'erro'
        });
      } else {
        setMensagem({
          texto: 'Erro de conexão com o servidor.',
          tipo: 'erro'
        });
      }
    }
  };

  return (
    <div className="page-center">
      <div className="cadastro-container">

        <h2>Entrar</h2>

        <p className="subtitulo">
          Bem-vindo de volta.
        </p>

        <form onSubmit={handleSubmit}>

          <div className="form-group">
            <label>E-mail</label>
            <input
              type="email"
              placeholder="Digite seu e-mail"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Senha</label>
            <input
              type="password"
              placeholder="Digite sua senha"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              required
            />
          </div>

          <button type="submit">
            Entrar
          </button>

        </form>

        <p>
          Ainda não possui uma conta?{" "}
          <Link to="/register">
            Criar conta
          </Link>
        </p>

        {mensagem.texto && (
          <div className={`mensagem ${mensagem.tipo}`}>
            {mensagem.texto}
          </div>
        )}

      </div>
    </div>
  );
}

export default Login;