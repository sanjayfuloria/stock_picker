import streamlit as st
from stock_picker.main import run
import json

# Static mapping of top 5 companies per sector
SECTOR_COMPANIES = {
    "Retail": ["Walmart", "Costco", "Target", "Home Depot", "Lowe's"],
    "Consumer Goods": ["Procter & Gamble", "Unilever", "Coca-Cola", "PepsiCo", "Nestle"],
    "Technology": ["Apple", "Microsoft", "Alphabet (Google)", "Amazon", "Meta Platforms (Facebook)"],
    "Energy": ["ExxonMobil", "Chevron", "Shell", "BP", "TotalEnergies"]
}

def detailed_analysis(company, sector):
    # This is a placeholder. In a real app, you would fetch and analyze real data.
    return {
        "name": company,
        "business_overview": f"{company} is a leading company in the {sector} sector.",
        "recent_performance": f"Recent performance data for {company}.",
        "competitive_landscape": f"Competitive landscape for {company} in {sector}.",
        "risks": f"Key risks for {company} in the current market.",
        "opportunities": f"Growth opportunities for {company} in {sector}.",
        "investment_thesis": f"Summary investment thesis for {company}."
    }

def pretty_print_research(research_list):
        for i, company in enumerate(research_list, 1):
                st.markdown(f"""
<div style='border:1px solid #ddd; border-radius:8px; padding:16px; margin-bottom:16px; background-color:#f9f9f9;'>
<h4 style='margin-bottom:8px;'> {i}. <b>{company['name']}</b></h4>
<ul style='margin-top:0;'>
    <li><b>Business Overview:</b> {company.get('business_overview', '')}</li>
    <li><b>Recent Performance:</b> {company.get('recent_performance', '')}</li>
    <li><b>Competitive Landscape:</b> {company.get('competitive_landscape', '')}</li>
    <li><b>Risks:</b> {company.get('risks', '')}</li>
    <li><b>Opportunities:</b> {company.get('opportunities', '')}</li>
    <li><b>Investment Thesis:</b> {company.get('investment_thesis', '')}</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.title("Stock Picker App")

sector = st.selectbox(
    "Select a sector for research:",
    ["Technology", "Consumer Goods", "Retail", "Energy"],
    key="sector_selectbox"
)

if st.button("Analyze Top 5 Companies", key="analyze_button"):
    with st.spinner(f"Analyzing companies in {sector}..."):
        # Use static mapping for top 5 companies in the selected sector
        companies = SECTOR_COMPANIES.get(sector, [])
        research_list = [detailed_analysis(company, sector) for company in companies]
        st.subheader("Research Output:")
        pretty_print_research(research_list)
