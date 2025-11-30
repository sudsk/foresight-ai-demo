import { useEffect, useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { X, Send } from 'lucide-react'
import { RootState } from '@/store'
import { setIsOpen, addMessage, setIsTyping } from '@/store/chatSlice'
import { chatAPI } from '@/services/api'
import ChatMessage from './ChatMessage'
import ChatInput from './ChatInput'
import { cn } from '@/utils/formatters'

const ChatModal = () => {
  const dispatch = useDispatch()
  const { messages, isTyping } = useSelector((state: RootState) => state.chat)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Auto-scroll to bottom when new messages arrive
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isTyping])

  useEffect(() => {
    // Add initial AI greeting if no messages
    if (messages.length === 0) {
      dispatch(
        addMessage({
          id: 'initial',
          role: 'assistant',
          content: `Hello! I'm your Credit Risk AI Assistant. I have access to your portfolio of 1,284 SMEs and can help you with:

- Analyzing specific SME health and risk factors
- Running what-if scenarios on your portfolio
- Collecting news and sentiment for any SME
- Creating tasks and investigations
- Answering questions about your portfolio metrics

What would you like to know?`,
          timestamp: new Date().toISOString(),
        })
      )
    }
  }, [])

  const handleClose = () => {
    dispatch(setIsOpen(false))
  }

  const handleSendMessage = async (content: string) => {
    // Add user message
    const userMessage = {
      id: `user_${Date.now()}`,
      role: 'user' as const,
      content,
      timestamp: new Date().toISOString(),
    }
    dispatch(addMessage(userMessage))

    // Show typing indicator
    dispatch(setIsTyping(true))

    try {
      // Send to API (mock response for demo)
      await new Promise((resolve) => setTimeout(resolve, 2000)) // Simulate API delay

      // Mock AI response based on user query
      let aiResponse = ''
      const lowerContent = content.toLowerCase()

      if (lowerContent.includes('techstart')) {
        aiResponse = `✅ Analyzing TechStart Solutions Ltd (#0142)...

📰 **NEWS INTELLIGENCE:**
- CTO departure confirmed (LinkedIn detection: 2 hours ago)
- Sales Director also left (within 2-week window)
- No replacement hires detected
- Web traffic: -42% QoQ decline
- Lost 2 major clients in past 30 days

📊 **IMPACT ASSESSMENT:**
- Current Risk Score: 54 → 68 (+14 points)
- Status: MEDIUM → CRITICAL
- Exposure: €250K

😟 **SENTIMENT:** NEGATIVE
- Employee reviews declining (Glassdoor)
- Customer sentiment: concerns about delivery delays
- Industry chatter: leadership vacuum

🎯 **RUNNING SCENARIO ANALYSIS...**
Calculating impact if situation continues for 90 days.

Processing complete! Click the '🎯 Scenarios' tab at the top to see full results.

Would you like me to create a task for immediate follow-up?`
      } else if (lowerContent.includes('interest rate') || lowerContent.includes('rate')) {
        aiResponse = `✅ Scenario submitted!

**"What if interest rates go up 1%?"**

Analyzing all 1,284 SMEs with variable rate exposure...

Estimated time: 15-30 seconds

🔄 Processing:
- Identified 487 SMEs with variable rate loans
- Recalculating debt service coverage for each
- Running ML risk model with +1% interest shock

**Switch to the Scenarios tab to see real-time progress!**

I'll notify you when the analysis is complete.`
      } else if (lowerContent.includes('portfolio') || lowerContent.includes('metrics')) {
        aiResponse = `📊 **Current Portfolio Snapshot:**

**Risk Distribution:**
- Critical Risk (80-100): 23 SMEs | €42M exposure | 12.8%
- Medium Risk (50-79): 142 SMEs | €98M exposure | 29.9%
- Low Risk (0-49): 1,119 SMEs | €188M exposure | 57.3%

**Key Metrics:**
- Total Portfolio: 1,284 SMEs | €328M exposure
- Average Risk Score: 64
- Default Probability: 2.8%
- Portfolio Trend: ↑ Slightly deteriorating

**Recent Changes (This Quarter):**
- +5 SMEs moved to Critical
- +8 SMEs moved to Medium
- -13 SMEs moved to Low Risk

Would you like me to drill down into any specific category or sector?`
      } else {
        aiResponse = `I understand you're asking about: "${content}"

I can help you with:
- **Analyzing specific SMEs** - Just mention the company name or ID
- **Running scenarios** - Ask "what if" questions about your portfolio
- **Portfolio insights** - Ask about metrics, trends, or specific segments
- **Creating tasks** - I can help you create follow-up tasks

Could you provide more details about what you'd like to explore?`
      }

      const assistantMessage = {
        id: `assistant_${Date.now()}`,
        role: 'assistant' as const,
        content: aiResponse,
        timestamp: new Date().toISOString(),
      }
      dispatch(addMessage(assistantMessage))
    } catch (error) {
      console.error('Failed to send message:', error)
      const errorMessage = {
        id: `error_${Date.now()}`,
        role: 'assistant' as const,
        content: 'Sorry, I encountered an error processing your request. Please try again.',
        timestamp: new Date().toISOString(),
      }
      dispatch(addMessage(errorMessage))
    } finally {
      dispatch(setIsTyping(false))
    }
  }

  return (
    <div className="fixed bottom-24 right-6 z-50 w-[480px] h-[640px] bg-white rounded-lg shadow-2xl border border-neutral-300 flex flex-col">
      {/* Header */}
      <div className="px-4 py-3 bg-primary-60 text-white rounded-t-lg flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-white bg-opacity-20 flex items-center justify-center">
            <span className="text-lg">🤖</span>
          </div>
          <div>
            <h3 className="font-semibold">Credit Risk AI Assistant</h3>
            <p className="text-xs text-white text-opacity-90">Always here to help</p>
          </div>
        </div>
        <button
          onClick={handleClose}
          className="w-8 h-8 rounded hover:bg-white hover:bg-opacity-20 flex items-center justify-center transition-colors"
        >
          <X className="w-5 h-5" />
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-neutral-50">
        {messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))}
        {isTyping && (
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 rounded-full bg-primary-60 flex items-center justify-center flex-shrink-0">
              <span className="text-sm">🤖</span>
            </div>
            <div className="bg-white rounded-lg px-4 py-3 max-w-[85%]">
              <div className="flex gap-1">
                <span className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                <span className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                <span className="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <ChatInput onSend={handleSendMessage} disabled={isTyping} />
    </div>
  )
}

export default ChatModal
