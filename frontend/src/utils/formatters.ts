export const formatCurrency = (value: number | string): string => {
  const num = typeof value === 'string' ? parseFloat(value.replace(/[€,]/g, '')) : value;
  return `€${num.toLocaleString('en-GB', { maximumFractionDigits: 0 })}`;
};

export const formatPercent = (value: number): string => {
  return `${value.toFixed(1)}%`;
};

export const formatDate = (dateString: string): string => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-GB', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  });
};

export const formatRelativeTime = (dateString: string): string => {
  const date = new Date(dateString);
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);

  if (diffMins < 1) return 'Just now';
  if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  if (diffDays === 1) return 'Yesterday';
  if (diffDays < 7) return `${diffDays} days ago`;
  
  return formatDate(dateString);
};

export const getRiskCategory = (score: number): 'critical' | 'medium' | 'stable' => {
  if (score >= 80) return 'critical';
  if (score >= 50) return 'medium';
  return 'stable';
};

export const cn = (...classes: (string | undefined | null | false)[]): string => {
  return classes.filter(Boolean).join(' ');
};
