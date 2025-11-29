import { Loader } from 'lucide-react'
import { formatRelativeTime } from '@/utils/formatters'
import type { Scenario } from '@/services/types'

interface ScenarioProgressProps {
  scenario: Scenario
}

const ScenarioProgress = ({ scenario }: ScenarioProgressProps) => {
  const progress = scenario.progress || 0

  return (
    <div className="bg-white border-2 border-primary-60 rounded-lg p-4">
      <div className="flex items-start justify-between mb-3">
        <div className="flex-1">
          <h4 className="text-base font-bold text-neutral-800 mb-1">{scenario.name}</h4>
          <div className="text-xs text-neutral-500">
            Started {formatRelativeTime(scenario.createdAt)}
          </div>
        </div>
        <div className="flex items-center gap-2 text-primary-60">
          <Loader className="w-5 h-5 animate-spin" />
          <span className="text-sm font-semibold">{progress}%</span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-neutral-200 rounded-full h-2 overflow-hidden">
        <div
          className="bg-primary-60 h-full transition-all duration-500"
          style={{ width: `${progress}%` }}
        />
      </div>

      <div className="mt-2 text-xs text-neutral-600">
        Processing {Math.floor((progress / 100) * 1284)} / 1,284 SMEs...
      </div>
    </div>
  )
}

export default ScenarioProgress
