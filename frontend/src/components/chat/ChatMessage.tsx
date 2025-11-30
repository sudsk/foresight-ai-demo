import { formatRelativeTime } from '@/utils/formatters'
import type { ChatMessage as ChatMessageType } from '@/services/types'

interface ChatMessageProps {
  message: ChatMessageType
}

const ChatMessage = ({ message }: ChatMessageProps) => {
  const isUser = message.role === 'user'

  return (
    <div className={`flex items-start gap-3 ${isUser ? 'flex-row-reverse' : ''}`}>
      {/* Avatar */}
      <div
        className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
          isUser ? 'bg-neutral-300' : 'bg-primary-60'
        }`}
      >
        <span className="text-sm">{isUser ? '👤' : '🤖'}</span>
      </div>

      {/* Message Bubble */}
      <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} max-w-[85%]`}>
        <div
          className={`rounded-lg px-4 py-3 ${
            isUser
              ? 'bg-primary-60 text-white'
              : 'bg-white text-neutral-800 border border-neutral-200'
          }`}
        >
          <p className="text-sm whitespace-pre-wrap">{message.content}</p>
        </div>
        <span className="text-xs text-neutral-500 mt-1">
          {formatRelativeTime(message.timestamp)}
        </span>
      </div>
    </div>
  )
}

export default ChatMessage
