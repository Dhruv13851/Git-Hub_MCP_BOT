from model.github_tools import GitHubTools


class ExecutionService:

    def __init__(
        self,
        github_tools: GitHubTools
    ):
        self.github_tools = github_tools

    async def execute(self, intent):

        print(f"\nExecuting action: {intent.action}")

        if intent.action == "create_repository":

            return await self.github_tools.create_repository(
                intent.repository_name
            )

        elif intent.action == "delete_repository":

            return await self.github_tools.delete_repository(
                intent.repository_name
            )

        elif intent.action == "list_repositories":

            return await self.github_tools.list_repositories()

        elif intent.action == "list_issues":

            return await self.github_tools.list_issues(
                intent.repository_name
            )

        return f"Unsupported action: {intent.action}"