from agent.github_agent import GitHubAgent


class IntentService:

    def __init__(self):

        self.agent = GitHubAgent()

    def extract_intent(
        self,
        query: str
    ):

        return self.agent.get_intent(
            query
        )