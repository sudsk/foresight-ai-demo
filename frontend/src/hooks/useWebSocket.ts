import { useEffect } from 'react';
import { wsService } from '@/services/websocket';

export const useWebSocket = (
  type: string,
  handler: (data: any) => void,
  deps: any[] = []
) => {
  useEffect(() => {
    wsService.on(type, handler);

    return () => {
      wsService.off(type, handler);
    };
  }, deps);
};
