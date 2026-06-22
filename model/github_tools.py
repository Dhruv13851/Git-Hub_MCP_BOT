class GitHubTools:

    def __init__(self, session):
        self.session = session

    async def list_repositories(self):

        print("CLIENT -> list_repositories")

        result = await self.session.call_tool(
            "list_repositories",
            {}
        )

        print("CLIENT <- response received")

        return result

    async def create_repository(
        self,
        repository_name: str
    ):

        print(f"CLIENT -> create_repository({repository_name})")

        return await self.session.call_tool(
            "create_repository",
            {
                "name": repository_name
            }
        )

    async def delete_repository(
        self,
        repository_name: str
    ):

        print(f"CLIENT -> delete_repository({repository_name})")

        return await self.session.call_tool(
            "delete_repository",
            {
                "name": repository_name
            }
        )

    async def list_issues(
        self,
        repository_name: str
    ):

        print(f"CLIENT -> list_issues({repository_name})")

        return await self.session.call_tool(
            "list_issues",
            {
                "repo_name": repository_name
            }
        )