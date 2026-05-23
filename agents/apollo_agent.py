from services.apollo_client import ApolloClient
from schemas.lead import Lead


class ApolloLeadAgent:
    def __init__(self):
        self.client = ApolloClient()

    def find_leads(self, filters: dict):
        raw = self.client.search_people(filters)

        leads = []

        for person in raw.get("people", []):
            lead = Lead(
                name=person.get("name"),
                title=person.get("title"),
                company=person.get("organization", {}).get("name"),
                linkedin_url=person.get("linkedin_url"),
                email=person.get("email"),
                apollo_id=person.get("id")
            )
            leads.append(lead)

        return leads