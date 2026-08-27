import './TopicCard.css';

function TopicCard({ title, description }) {
  return (
    <div className="topic-card">
      <h3 className="topic-card__title">{title}</h3>
      <p className="topic-card__description">{description}</p>
    </div>
  );
}

export default TopicCard;