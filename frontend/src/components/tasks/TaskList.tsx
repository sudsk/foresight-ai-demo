import { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { RootState } from '@/store'
import { updateTask, removeTask } from '@/store/tasksSlice'
import { setActiveTab } from '@/store/uiSlice'
import { setSelectedSME } from '@/store/portfolioSlice'
import TaskCard from './TaskCard'
import { Button } from '../common/Button'
import { Plus } from 'lucide-react'

const TaskList = () => {
  const dispatch = useDispatch()
  const tasks = useSelector((state: RootState) => state.tasks.tasks)
  const [showAllUpcoming, setShowAllUpcoming] = useState(false)

  const overdueTasks = tasks.filter((t) => t.status === 'overdue')
  const dueTodayTasks = tasks.filter((t) => t.status === 'due_today')
  const upcomingTasks = tasks.filter((t) => t.status === 'upcoming')

  const displayedUpcoming = showAllUpcoming ? upcomingTasks : upcomingTasks.slice(0, 3)

  const handleCompleteTask = (taskId: string) => {
    const task = tasks.find((t) => t.id === taskId)
    if (task) {
      dispatch(
        updateTask({
          ...task,
          status: 'completed',
        })
      )
    }
  }

  const handleViewSME = (task: typeof tasks[0]) => {
    // Mock SME - in real app would fetch from API
    const sme = {
      id: task.smeId,
      name: task.smeName,
      riskScore: 68,
      riskCategory: 'critical' as const,
      exposure: task.exposure,
      sector: 'Software/Technology',
      geography: 'UK',
      trend: 'up' as const,
      trendValue: 14,
    }
    dispatch(setSelectedSME(sme))
    dispatch(setActiveTab('home'))
  }

  const handleViewSource = (task: typeof tasks[0]) => {
    // Navigate to source event
    if (task.source.includes('Predicted Event')) {
      dispatch(setActiveTab('news'))
    } else if (task.source.includes('News Intelligence')) {
      dispatch(setActiveTab('news'))
    }
  }

  return (
    <div className="space-y-6">
      {/* Overdue Tasks */}
      {overdueTasks.length > 0 && (
        <section>
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-lg font-semibold text-critical-60">
              ⚠️ Overdue Tasks ({overdueTasks.length})
            </h3>
          </div>
          <div className="space-y-3">
            {overdueTasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onComplete={() => handleCompleteTask(task.id)}
                onViewSME={() => handleViewSME(task)}
                onViewSource={() => handleViewSource(task)}
              />
            ))}
          </div>
        </section>
      )}

      {/* Due Today */}
      {dueTodayTasks.length > 0 && (
        <section>
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-lg font-semibold text-warning-60">
              📅 Due Today ({dueTodayTasks.length})
            </h3>
          </div>
          <div className="space-y-3">
            {dueTodayTasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onComplete={() => handleCompleteTask(task.id)}
                onViewSME={() => handleViewSME(task)}
                onViewSource={() => handleViewSource(task)}
              />
            ))}
          </div>
        </section>
      )}

      {/* Upcoming Tasks */}
      {upcomingTasks.length > 0 && (
        <section>
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-lg font-semibold text-primary-60">
              📋 Upcoming Tasks ({upcomingTasks.length})
            </h3>
          </div>
          <div className="space-y-3">
            {displayedUpcoming.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onComplete={() => handleCompleteTask(task.id)}
                onViewSME={() => handleViewSME(task)}
                onViewSource={() => handleViewSource(task)}
              />
            ))}
          </div>
          {upcomingTasks.length > 3 && !showAllUpcoming && (
            <div className="mt-3">
              <Button
                variant="secondary"
                size="md"
                fullWidth
                onClick={() => setShowAllUpcoming(true)}
              >
                Show All {upcomingTasks.length} Upcoming Tasks
              </Button>
            </div>
          )}
        </section>
      )}

      {/* Empty State */}
      {tasks.length === 0 && (
        <div className="text-center py-12 bg-white rounded-lg border border-neutral-300">
          <div className="text-4xl mb-3">📋</div>
          <p className="text-lg font-medium text-neutral-700">No tasks yet</p>
          <p className="text-sm text-neutral-500 mt-2">
            Create tasks from news events or scenarios
          </p>
          <div className="mt-6">
            <Button variant="primary" size="md">
              <Plus className="w-4 h-4" />
              Create New Task
            </Button>
          </div>
        </div>
      )}
    </div>
  )
}

export default TaskList
