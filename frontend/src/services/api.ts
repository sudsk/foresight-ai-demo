import axios from 'axios';
import { API_BASE_URL } from '@/utils/constants';
import type {
  PortfolioMetrics,
  SME,
  PredictedEvent,
  NewsItem,
  Task,
  Scenario,
  Activity,
  ChatMessage,
} from './types';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptors for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

// Portfolio API
export const portfolioAPI = {
  getMetrics: async (): Promise<PortfolioMetrics> => {
    const { data } = await api.get('/api/v1/portfolio/metrics');
    return data;
  },

  getSMEs: async (): Promise<SME[]> => {
    const { data } = await api.get('/api/v1/portfolio/smes');
    return data;
  },

  getSMEById: async (id: string): Promise<SME> => {
    const { data } = await api.get(`/api/v1/portfolio/smes/${id}`);
    return data;
  },

  getBreakdownData: async (riskLevel: string): Promise<any> => {
    const { data } = await api.get(`/api/v1/portfolio/breakdown/${riskLevel}`);
    return data;
  },
};

// News & Events API
export const newsAPI = {
  getPredictedEvents: async (): Promise<PredictedEvent[]> => {
    const { data } = await api.get('/api/v1/news/predicted-events');
    return data;
  },

  getNewsIntelligence: async (): Promise<NewsItem[]> => {
    const { data } = await api.get('/api/v1/news/intelligence');
    return data;
  },
};

// Tasks API
export const tasksAPI = {
  getTasks: async (): Promise<Task[]> => {
    const { data } = await api.get('/api/v1/tasks');
    return data;
  },

  createTask: async (task: Partial<Task>): Promise<Task> => {
    const { data } = await api.post('/api/v1/tasks', task);
    return data;
  },

  updateTask: async (id: string, updates: Partial<Task>): Promise<Task> => {
    const { data } = await api.patch(`/api/v1/tasks/${id}`, updates);
    return data;
  },

  deleteTask: async (id: string): Promise<void> => {
    await api.delete(`/api/v1/tasks/${id}`);
  },

  completeTask: async (id: string): Promise<Task> => {
    const { data } = await api.post(`/api/v1/tasks/${id}/complete`);
    return data;
  },
};

// Scenarios API
export const scenariosAPI = {
  getScenarios: async (): Promise<Scenario[]> => {
    const { data } = await api.get('/api/v1/scenarios');
    return data;
  },

  createScenario: async (description: string): Promise<Scenario> => {
    const { data } = await api.post('/api/v1/scenarios', { description });
    return data;
  },

  getScenarioById: async (id: string): Promise<Scenario> => {
    const { data } = await api.get(`/api/v1/scenarios/${id}`);
    return data;
  },

  deleteScenario: async (id: string): Promise<void> => {
    await api.delete(`/api/v1/scenarios/${id}`);
  },
};

// Activities API
export const activitiesAPI = {
  getActivities: async (): Promise<Activity[]> => {
    const { data } = await api.get('/api/v1/activities');
    return data;
  },
};

// Chat API
export const chatAPI = {
  sendMessage: async (message: string): Promise<ChatMessage> => {
    const { data } = await api.post('/api/v1/chat/message', { message });
    return data;
  },

  getHistory: async (): Promise<ChatMessage[]> => {
    const { data } = await api.get('/api/v1/chat/history');
    return data;
  },
};

export default api;
