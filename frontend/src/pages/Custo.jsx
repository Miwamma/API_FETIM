import { useEffect, useState } from 'react';
import { medicaoService } from '../services/medicaoService';
import InfoCard from '../components/InfoCard';
import PageHeader from '../components/PageHeader';
import '../styles/cards.css';

function Custo() {
  const [custo, setCusto] = useState({ data: null, loading: true, error: false });

  useEffect(() => {
    medicaoService.getCusto()
      .then((res) => setCusto({ data: res.data, loading: false, error: false }))
      .catch(() => setCusto({ data: null, loading: false, error: true }));
  }, []);

  return (
    <div>
      <PageHeader
        title="Custo de água"
        description="Estimativa de quanto o consumo registrado representa em reais, com base na tarifa por metro cúbico configurada no sistema."
      />
      <div className="info-grid" style={{ maxWidth: 260 }}>
        <InfoCard
          title="Custo estimado"
          value={custo.data ? `R$ ${custo.data.totalCost.toFixed(2).replace('.', ',')}` : '--'}
          loading={custo.loading}
          error={custo.error}
          highlight
        />
      </div>
      {custo.data && !custo.loading && (
        <p style={{ marginTop: 16, color: '#64748b', fontSize: 14 }}>
          Baseado em {custo.data.totalCubicMeters.toFixed(3)} m³ e tarifa de{' '}
          R$ {custo.data.waterTariffPerCubicMeter.toFixed(2)}/m³.
        </p>
      )}
    </div>
  );
}

export default Custo;