"""
News service - news intelligence logic
"""
from typing import List
from datetime import datetime, timedelta
from app.models.news import PredictedEvent, NewsItem


class NewsService:
    """News intelligence service"""
    
    def __init__(self):
        # Mock data
        self._predicted_events = self._generate_mock_events()
        self._news_items = self._generate_mock_news()
    
    def get_predicted_events(self) -> List[PredictedEvent]:
        """Get predicted events"""
        return self._predicted_events
    
    def get_news_intelligence(self) -> List[NewsItem]:
        """Get news intelligence items"""
        return self._news_items
    
    def _generate_mock_events(self) -> List[PredictedEvent]:
        """Generate mock predicted events"""
        return [
            PredictedEvent(
                id="evt_001",
                date="2024-12-01",
                days_until=17,
                title="UK Hemp Products Ban",
                probability=75,
                affects={"smes": 8, "exposure": "€12M"},
                impact="+12 to +18 avg score increase",
                key_smes=["#0445 GreenLeaf Products", "#0672 Natural Wellness Ltd"],
                source="UK Parliament Calendar",
                description="Parliamentary vote expected Dec 1. 75% probability of ban passing based on committee support."
            ),
            PredictedEvent(
                id="evt_002",
                date="2024-12-15",
                days_until=31,
                title="BoE Interest Rate Decision",
                probability=60,
                affects={"smes": 487, "exposure": "€142M"},
                impact="Expected +0.25% increase",
                key_smes=[],
                source="Bank of England Schedule",
                description="MPC meeting Dec 15. Market pricing in 60% chance of 25bps hike to combat inflation."
            ),
            PredictedEvent(
                id="evt_003",
                date="2025-01-10",
                days_until=57,
                title="EU Data Privacy Regulation",
                probability=40,
                affects={"smes": 34, "exposure": "€18M"},
                impact="Compliance costs €50K-200K per SME",
                key_smes=["#0142 TechStart Solutions"],
                source="EU Commission Filings",
                description="New GDPR enforcement rules. Tech companies face increased compliance burden."
            )
        ]
    
    def _generate_mock_news(self) -> List[NewsItem]:
        """Generate mock news intelligence"""
        return [
            NewsItem(
                id="news_001",
                timestamp="2024-11-16T14:32:17Z",
                sme_id="#0142",
                sme_name="TechStart Solutions Ltd",
                exposure="€250K",
                type="departure",
                severity="critical",
                title="CTO Departure Detected",
                summary="LinkedIn activity shows CTO Sarah Johnson departed 2 hours ago. No replacement hire detected. Sales Director also left within 2-week window.",
                signals=[
                    {"source": "LinkedIn", "detail": "CTO profile updated: 'Open to new opportunities'"},
                    {"source": "Web Traffic", "detail": "-42% QoQ decline"},
                    {"source": "Client Data", "detail": "2 major clients lost in past 30 days"}
                ],
                recommendation="Immediate management meeting recommended. High risk of further deterioration."
            ),
            NewsItem(
                id="news_002",
                timestamp="2024-11-16T11:15:43Z",
                sme_id="#0287",
                sme_name="Urban Fashion Ltd",
                exposure="€180K",
                type="payment_delay",
                severity="warning",
                title="Payment Delays to Suppliers",
                summary="Alternative data shows 3 suppliers reporting late payments (avg 47 days vs normal 30 days). Cash flow stress indicator.",
                signals=[
                    {"source": "Trade Data", "detail": "3 suppliers flagged payment delays"},
                    {"source": "Banking", "detail": "Overdraft facility 85% utilized"},
                    {"source": "Companies House", "detail": "No recent capital injection"}
                ],
                recommendation="Review cash flow forecasts. Consider covenant breach risk."
            ),
            NewsItem(
                id="news_003",
                timestamp="2024-11-16T08:22:11Z",
                sme_id="#0531",
                sme_name="Digital Marketing Hub",
                exposure="€140K",
                type="churn",
                severity="warning",
                title="Client Churn Alert",
                summary="Website testimonials reduced by 40%. LinkedIn shows 2 account managers left. Review scores declining (4.2 → 3.1 in 90 days).",
                signals=[
                    {"source": "Reviews", "detail": "Trustpilot: 4.2 → 3.1 stars"},
                    {"source": "LinkedIn", "detail": "2 account managers departed"},
                    {"source": "Web Traffic", "detail": "Case studies page views -60%"}
                ],
                recommendation="Monitor closely. Service quality deterioration pattern."
            )
        ]
