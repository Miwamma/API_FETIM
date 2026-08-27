import { useNavigate } from 'react-router-dom';

function NavCard({ title, description, to }) {
  const navigate = useNavigate();

  return (
    <button className="nav-card" onClick={() => navigate(to)}>
      <span className="nav-card__title">{title}</span>
      {description && <span className="nav-card__description">{description}</span>}
    </button>
  );
}

export default NavCard;