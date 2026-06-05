import {useState} from 'react';
import './Cadastro.css';

function Register() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [mensagem, setMensagem] = useState({ texto: '', tipo: '' });

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMensagem({ texto: 'Carregando...', tipo: 'info' });

    try {
      const resposta = await fetch('http://localhost:8000/users/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, email, senha })
      });

      const dados = await resposta.json();

      if (resposta.status === 201) {
        setMensagem({ texto: 'Cadastro realizado com sucesso!', tipo: 'sucesso' });
        setNome('');
        setEmail('');
        setSenha('');
      } else if (resposta.status === 409) {
        setMensagem({ texto: dados.detail, tipo: 'erro' });
      } else {
        setMensagem({ texto: 'Erro ao realizar cadastro.', tipo: 'erro' });
      }
    } catch (erro) {
      setMensagem({ texto: 'Erro de conexão com o servidor.', tipo: 'erro' });
      console.error(erro);
    }
  };

  return (
    <div className="cadastro-container">
      <h2>Criar Conta</h2>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="nome">Nome Completo</label>
          <input 
            type="text" 
            id="nome" 
            placeholder="Ex: João da Silva" 
            required 
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="email">E-mail</label>
          <input 
            type="email" 
            id="email" 
            placeholder="joao@email.com" 
            required 
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="senha">Senha</label>
          <input 
            type="password" 
            id="senha" 
            placeholder="Mínimo 6 caracteres" 
            required 
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </div>
        
        <button type="submit">Cadastrar</button>
      </form>

      {mensagem.texto && (
        <div className={`mensagem ${mensagem.tipo}`}>
          {mensagem.texto}
        </div>
      )}
    </div>
  );
}

export default Register;