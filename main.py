from agents.apollo_agent import ApolloLeadAgent

agent = ApolloLeadAgent()

filters = {
    "person_titles": ["Founder", "CTO"],
    "person_locations": ["United States"],
    "organization_num_employees_ranges": ["11,50"]
}

leads = agent.find_leads(filters)

for lead in leads[:5]:
    print(lead.model_dump())