from mcp.server.fastmcp import FastMCP
from clients.github_client import GitHubClient


def register_issue_tools(
    mcp: FastMCP,
    github: GitHubClient,
):

    @mcp.tool()
    def list_issues(
        repo_name: str
    ):

        repo = github.user.get_repo(
            repo_name
        )

        return [
            {
                "title": issue.title,
                "number": issue.number,
                "state": issue.state,
            }
            for issue in repo.get_issues()
        ]