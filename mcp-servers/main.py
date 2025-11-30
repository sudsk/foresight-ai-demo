"""
Main MCP Server Runner
Runs all MCP servers on single FastAPI instance
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all MCP servers
from mcp_servers.data_sources.linkedin_server import mcp as linkedin_mcp
from mcp_servers.data_sources.companies_house_server import mcp as companies_house_mcp
from mcp_servers.data_sources.google_analytics_server import mcp as analytics_mcp
from mcp_servers.data_sources.news_intelligence_server import mcp as news_mcp
from mcp_servers.storage.bigquery_server import mcp as bigquery_mcp
from mcp_servers.storage.vertex_ai_server import mcp as vertex_ai_mcp

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create main FastAPI app
app = FastAPI(
    title="Foresight AI MCP Servers",
    description="Mock MCP servers for SME credit risk data",
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all MCP servers
logger.info("Mounting MCP servers...")

# LinkedIn server
app.mount("/linkedin", linkedin_mcp.app)
logger.info("✓ LinkedIn MCP Server mounted at /linkedin")

# Companies House server
app.mount("/companies-house", companies_house_mcp.app)
logger.info("✓ Companies House MCP Server mounted at /companies-house")

# Google Analytics server
app.mount("/google-analytics", analytics_mcp.app)
logger.info("✓ Google Analytics MCP Server mounted at /google-analytics")

# News Intelligence server
app.mount("/news-intelligence", news_mcp.app)
logger.info("✓ News Intelligence MCP Server mounted at /news-intelligence")

# BigQuery server
app.mount("/bigquery", bigquery_mcp.app)
logger.info("✓ BigQuery MCP Server mounted at /bigquery")

# Vertex AI server
app.mount("/vertex-ai", vertex_ai_mcp.app)
logger.info("✓ Vertex AI MCP Server mounted at /vertex-ai")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Foresight AI MCP Servers",
        "version": "1.0.0",
        "servers": [
            {"name": "linkedin", "path": "/linkedin"},
            {"name": "companies_house", "path": "/companies-house"},
            {"name": "google_analytics", "path": "/google-analytics"},
            {"name": "news_intelligence", "path": "/news-intelligence"},
            {"name": "bigquery", "path": "/bigquery"},
            {"name": "vertex_ai", "path": "/vertex-ai"},
        ]
    }


@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}


@app.get("/servers")
async def list_servers():
    """List all available MCP servers"""
    return {
        "servers": [
            {
                "name": "linkedin_server",
                "description": "Employee data and company activity",
                "tools": ["get_employee_count", "get_recent_departures", "get_job_postings"]
            },
            {
                "name": "companies_house_server",
                "description": "UK company filings and directors",
                "tools": ["get_company_info", "get_directors", "get_filing_history", "check_insolvency"]
            },
            {
                "name": "google_analytics_server",
                "description": "Website traffic and engagement",
                "tools": ["get_traffic_metrics", "get_conversion_metrics", "get_traffic_sources"]
            },
            {
                "name": "news_intelligence_server",
                "description": "News and sentiment analysis",
                "tools": ["get_sme_news", "get_sentiment_analysis"]
            },
            {
                "name": "bigquery_server",
                "description": "Portfolio data warehouse",
                "tools": [
                    "get_sme_data",
                    "get_portfolio_metrics",
                    "filter_smes_by_criteria",
                    "get_sme_financials",
                    "get_peer_comparison"
                ]
            },
            {
                "name": "vertex_ai_server",
                "description": "ML model inference",
                "tools": [
                    "predict_risk_score",
                    "get_risk_drivers",
                    "predict_default_probability",
                    "batch_score_portfolio"
                ]
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting MCP Servers...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        log_level="info"
    )
