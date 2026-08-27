import { api } from '../API/api';
import { DEVICE_ID } from '../config/device';

export const medicaoService = {
  getConsumoTotal: (deviceId = DEVICE_ID) =>
    api.get(`/medicoes/consumption/${deviceId}`),

  getConsumoCubicMeters: (deviceId = DEVICE_ID) =>
    api.get(`/medicoes/consumption/${deviceId}/cubic-meters`),

  getCusto: (deviceId = DEVICE_ID) =>
    api.get(`/medicoes/consumption/${deviceId}/cost`),

  getUltimaMedicao: (deviceId = DEVICE_ID) =>
    api.get('/medicoes/latest', { params: { deviceId } }),

  listMedicoes: (params = {}) =>
    api.get('/medicoes', { params: { deviceId: DEVICE_ID, ...params } }),
};