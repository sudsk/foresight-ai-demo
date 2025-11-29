import { Calendar, TrendingUp, Eye } from 'lucide-react'
import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { setActiveTab } from '@/store/uiSlice'
import { addScenario } from '@/store/scenariosSlice'
import { addTask } from '@/store/tasksSlice'
import { Button } from '../common/Button'
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card'

// Mock data
const predictedEvents = [
  {
    id: 'evt_001',
    date: '2024-12-01',
    daysUntil: 17,
    title: 'UK Hemp Products Ban',
    probability: 75,
    affects: { smes: 8, exposure: '€12M' },
    impact: '+12 to +18 avg score increase',
    keySMEs: ['#0445 GreenLeaf Products', '#0672 Natural Wellness Ltd'],
    source: 'UK Parliament Calendar',
    description: 'Parliamentary vote expected Dec 1. 75% probability of ban passing based on committee support.',
  },
  {
    id: 'evt_002',
    date: '2024-12-15',
    daysUntil: 31,
    title: 'BoE Interest Rate Decision',
    probability: 60,
    affects: { smes: 487, exposure: '€142M' },
    impact: 'Expected +0.25% increase',
    keySMEs: [],
    source: 'Bank of England Schedule',
    description: 'MPC meeting Dec 15. Market pricing in 60% chance of 25bps hike to combat inflation.',
  },
  {
    id: 'evt_003',
    date: '2025-01-10',
    daysUntil: 57,
    title: 'EU Data Privacy Regulation',
    probability: 40,
    affects: { smes: 34, exposure: '€18M' },
    impact: 'Compliance costs €50K-200K per SME',
    keySMEs: ['#0142 TechStart Solutions'],
    source: 'EU Commission Filings',
    description: 'New GDPR enforcement rules. Tech companies face increased compliance burden.',
  },
]

const PredictedEvents = () => {
  const dispatch = useDispatch()
  const [expandedEvent, setExpandedEvent] = useState<string | null>(null)

  const handleRunScenario = (event: typeof predictedEvents[0]) => {
    // Create scenario
    const scenario = {
      id: `scenario_${Date.now()}`,
      name: `${event.title} Impact`,
      status: 'in_progress' as const,
      progress: 0,
      createdAt: new Date().toISOString(),
    }
    dispatch(addScenario(scenario))
    dispatch(setActiveTab('scenarios'))
  }

  const handleCreateTask = (event: typeof predictedEvents[0]) => {
    // Create task
    const task = {
      id: `task_${Date.now()}`,
      title: `Review Impact: ${event.title}`,
      smeId: event.keySMEs[0]?.split(' ')[0] || '',
      smeName: event.keySMEs[0] || 'Multiple SMEs',
      exposure: event.affects.exposure,
      assignee: 'Unassigned',
      priority: 'high' as const,
      dueDate: event.date,
      status: 'upcoming' as const,
      description: `Predicted event: ${event.title}. ${event.description}`,
      source: `Predicted Event - ${event.title}`,
      createdAt: new Date().toISOString(),
    }
    dispatch(addTask(task))
    dispatch(setActiveTab('tasks'))
  }

  const toggleExpand = (eventId: string) => {
    setExpandedEvent(expandedEvent === eventId ? null : eventId)
  }

  return (
    <Card className="h-[calc(100vh-200px)] flex flex-col">
      <CardHeader className="flex-shrink-0">
        <CardTitle>
          <div className="flex items-center gap-2">
            <span className="text-2xl">🔮</span>
            <div>
              <div className="text-lg font-semibold">Predicted Events</div>
              <div className="text-xs font-normal text-neutral-500">
                AI-Predicted Future Events (Next 90 Days)
              </div>
            </div>
          </div>
        </CardTitle>
      </CardHeader>

      <CardContent className="flex-1 overflow-y-auto">
        <div className="space-y-4">
          {predictedEvents.map((event) => (
            <div
              key={event.id}
              className="border-2 border-warning-60 bg-warning-50 rounded-lg overflow-hidden"
            >
              {/* Event Header */}
              <div className="p-4 bg-white border-b border-warning-60">
                <div className="flex items-start justify-between mb-2">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <Calendar className="w-4 h-4 text-warning-60" />
                      <span className="text-sm font-semibold text-warning-70">
                        {event.date} ({event.daysUntil} days)
                      </span>
                      <span className="px-2 py-0.5 bg-warning-60 text-white text-xs font-bold rounded">
                        {event.probability}% Probability
                      </span>
                    </div>
                    <h4 className="text-base font-bold text-neutral-800">
                      {event.title}
                    </h4>
                  </div>
                </div>

                <div className="text-xs text-neutral-600 space-y-1">
                  <div>
                    <strong>Affects:</strong> {event.affects.smes} SMEs | {event.affects.exposure} exposure
                  </div>
                  <div>
                    <strong>Impact:</strong> {event.impact}
                  </div>
                  {event.keySMEs.length > 0 && (
                    <div>
                      <strong>Key SMEs:</strong> {event.keySMEs.join(', ')}
                    </div>
                  )}
                </div>

                {/* Expanded Description */}
                {expandedEvent === event.id && (
                  <div className="mt-3 pt-3 border-t border-neutral-200">
                    <p className="text-sm text-neutral-700 mb-2">{event.description}</p>
                    <div className="text-xs text-neutral-500">
                      <strong>Source:</strong> {event.source}
                    </div>
                  </div>
                )}

                {/* Actions */}
                <div className="flex items-center gap-2 mt-3">
                  <Button
                    variant="primary"
                    size="sm"
                    onClick={() => handleRunScenario(event)}
                  >
                    🎯 Run Scenario
                  </Button>
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() => handleCreateTask(event)}
                  >
                    📋 Create Task
                  </Button>
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() => toggleExpand(event.id)}
                  >
                    <Eye className="w-3.5 h-3.5" />
                    {expandedEvent === event.id ? 'Less' : 'More'}
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Empty State */}
        {predictedEvents.length === 0 && (
          <div className="text-center py-12 text-neutral-500">
            <div className="text-4xl mb-3">🔮</div>
            <p className="text-sm">No predicted events in the next 90 days</p>
          </div>
        )}
      </CardContent>
    </Card>
  )
}

export default PredictedEvents
