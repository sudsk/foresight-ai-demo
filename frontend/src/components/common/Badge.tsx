import { cn } from '@/utils/formatters'

interface BadgeProps {
  children: React.ReactNode
  variant?: 'critical' | 'warning' | 'info' | 'success'
  className?: string
}

export const Badge = ({ children, variant = 'info', className }: BadgeProps) => {
  return (
    <span
      className={cn(
        'px-2 py-1 text-xs font-semibold rounded',
        variant === 'critical' && 'bg-critical-50 text-critical-70',
        variant === 'warning' && 'bg-warning-50 text-warning-70',
        variant === 'info' && 'bg-primary-50 text-primary-70',
        variant === 'success' && 'bg-success-50 text-success-70',
        className
      )}
    >
      {children}
    </span>
  )
}
