"""
Companies House MCP Server - Mock Implementation
Provides UK company filings and director data
"""
from fastmcp import FastMCP
from datetime import datetime, timedelta

from mcp_servers.shared.mock_data import mock_data

mcp = FastMCP("Companies House Data Server")


@mcp.tool()
async def get_company_info(sme_id: str) -> dict:
    """
    Get company information from Companies House
    
    Args:
        sme_id: SME identifier
        
    Returns:
        Company registration and filing information
    """
    sme = mock_data.get_sme_by_id(sme_id)
    
    if not sme:
        return {"error": f"SME {sme_id} not found"}
    
    return {
        "sme_id": f"#{sme['id']}",
        "company_name": sme["name"],
        "company_number": f"0{sme['id']}4567",
        "incorporation_date": "2015-03-12",
        "company_status": "Active",
        "company_type": "Private Limited Company",
        "registered_address": {
            "line1": "123 Business Park",
            "city": "London",
            "postcode": "EC1A 1BB",
            "country": "United Kingdom"
        },
        "sic_codes": ["62011", "62012"],
        "last_accounts_date": "2023-12-31",
        "next_accounts_due": "2024-12-31",
        "source": "companies_house_api",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@mcp.tool()
async def get_directors(sme_id: str) -> list:
    """
    Get company directors
    
    Args:
        sme_id: SME identifier
        
    Returns:
        List of current directors
    """
    sme = mock_data.get_sme_by_id(sme_id)
    
    if not sme:
        return []
    
    return [
        {
            "name": "John Smith",
            "role": "Director",
            "appointed_on": "2015-03-12",
            "nationality": "British",
            "date_of_birth": {"month": 6, "year": 1975}
        },
        {
            "name": "Emily Johnson",
            "role": "Director",
            "appointed_on": "2018-07-20",
            "nationality": "British",
            "date_of_birth": {"month": 3, "year": 1982}
        }
    ]


@mcp.tool()
async def get_filing_history(sme_id: str, limit: int = 10) -> list:
    """
    Get recent filing history
    
    Args:
        sme_id: SME identifier
        limit: Maximum number of filings to return
        
    Returns:
        List of recent filings
    """
    sme = mock_data.get_sme_by_id(sme_id)
    
    if not sme:
        return []
    
    return [
        {
            "type": "Annual Accounts",
            "date": "2024-03-15",
            "description": "Annual accounts made up to 31 December 2023"
        },
        {
            "type": "Confirmation Statement",
            "date": "2024-03-12",
            "description": "Confirmation statement made on 12 March 2024"
        },
        {
            "type": "Annual Accounts",
            "date": "2023-03-20",
            "description": "Annual accounts made up to 31 December 2022"
        }
    ]


@mcp.tool()
async def check_insolvency(sme_id: str) -> dict:
    """
    Check for insolvency proceedings
    
    Args:
        sme_id: SME identifier
        
    Returns:
        Insolvency status
    """
    sme = mock_data.get_sme_by_id(sme_id)
    
    if not sme:
        return {"error": f"SME {sme_id} not found"}
    
    return {
        "sme_id": f"#{sme['id']}",
        "sme_name": sme["name"],
        "insolvency_proceedings": False,
        "ccjs": 0,  # County Court Judgments
        "status": "Clear",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
