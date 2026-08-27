import './PageHeader.css';

function PageHeader({ title, description }) {
  return (
    <div className="page-header">
      <h2 className="page-header__title">{title}</h2>
      {description && <p className="page-header__description">{description}</p>}
    </div>
  );
}

export default PageHeader;