from mcp.server.fastmcp import FastMCP
from clients.github_client import GitHubClient


def register_repository_tools(
    mcp: FastMCP,
    github: GitHubClient,
):

    @mcp.tool()
    def list_repositories():

        repos = github.user.get_repos()

        return [
            {
                "name": repo.name,
                "private": repo.private,
                "stars": repo.stargazers_count,
                "language": repo.language,
            }
            for repo in repos
        ]

    @mcp.tool()
    def create_repository(
        name: str,
        private: bool = False
    ):

        repo = github.user.create_repo(
            name=name,
            private=private
        )

        return {
            "name": repo.name,
            "url": repo.html_url
        }

    @mcp.tool()
    def delete_repository(
        name: str
    ):

        repo = github.user.get_repo(name)

        repo.delete()

        return {
            "message": f"Repository '{name}' deleted successfully"
        }