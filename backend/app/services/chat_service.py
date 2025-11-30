"""
Chat service - AI assistant logic
"""
from typing import List
import time
from app.models.chat import ChatMessage


class ChatService:
    """AI chat assistant service"""
    
    def __init__(self):
        # In-memory chat history
        self._messages: List[ChatMessage] = []
    
    async def process_message(self, user_message: str) -> ChatMessage:
        """
        Process user message and generate AI response
        In production, this would call the Agent Orchestrator
        """
        # Store user message
        user_msg = ChatMessage(
            id=f"user_{int(time.time() * 1000)}",
            role="user",
            content=user_message,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        )
        self._messages.append(user_msg)
        
        # Generate AI response (mock - would call agent in production)
        ai_content = self._generate_mock_response(user_message)
        
        ai_msg = ChatMessage(
            id=f"assistant_{int(time.time() * 1000)}",
            role="assistant",
            content=ai_content,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        )
        self._messages.append(ai_msg)
        
        return ai_msg
    
    def get_history(self) -> List[ChatMessage]:
        """Get chat history"""
        return self._messages
    
    def _generate_mock_response(self, user_message: str) -> str:
        """
        Generate mock AI response
        In production, this would call:
        - Agent Orchestrator (ADK)
        - Which routes to appropriate agents
        - Which call MCP servers for data
        """
        lower_msg = user_message.lower()
        
        if "techstart" in lower_msg:
            return """✅ Analyzing TechStart Solutions Ltd (#0142)...

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

Would you like me to create a task or run a scenario?"""
        
        elif "interest rate" in lower_msg or "rate" in lower_msg:
            return """✅ Scenario submitted!

**"What if interest rates go up 1%?"**

Analyzing all 1,284 SMEs with variable rate exposure...

🔄 Processing:
- Identified 487 SMEs with variable rate loans
- Recalculating debt service coverage
- Running ML risk model with +1% shock

**Switch to the Scenarios tab to see progress!**"""
        
        elif "portfolio" in lower_msg or "metrics" in lower_msg:
            return """📊 **Current Portfolio Snapshot:**

**Risk Distribution:**
- Critical: 23 SMEs | €42M | 12.8%
- Medium: 142 SMEs | €98M | 29.9%
- Stable: 1,119 SMEs | €188M | 57.3%

**Key Metrics:**
- Total: 1,284 SMEs | €328M
- Avg Risk Score: 64
- Default Probability: 2.8%

What would you like to explore further?"""
        
        else:
            return f"""I understand you're asking about: "{user_message}"

I can help you with:
- **Analyzing SMEs** - Mention company name or ID
- **Running scenarios** - Ask "what if" questions
- **Portfolio insights** - Ask about metrics or trends
- **Creating tasks** - I can help create follow-up tasks

Could you provide more details?"""
