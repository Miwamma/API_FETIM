export function formatDuration(seconds) {
  if (seconds == null) return '--';
  if (seconds < 60) return `${seconds}s`;
  const minutes = Math.floor(seconds / 60);
  const rest = seconds % 60;
  return `${minutes}min ${rest}s`;
}

export function formatDateTime(dateValue) {
  if (!dateValue) return '--';
  return new Date(dateValue).toLocaleString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}

export function calcInicio(timestamp, intervalSeconds) {
  if (!timestamp) return null;
  const fimMs = new Date(timestamp).getTime();
  const inicioMs = fimMs - (intervalSeconds || 0) * 1000;
  return new Date(inicioMs).toISOString();
}