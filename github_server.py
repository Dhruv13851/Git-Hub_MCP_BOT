from mcp.server.fastmcp import FastMCP

from clients.github_client import (
    GitHubClient
)

from tools.repository_tool import (
    register_repository_tools
)

from tools.issue_tool import (
    register_issue_tools
)


print("Starting server...")

mcp = FastMCP("GitHub Assistant")

print("Creating GitHub client...")

github = GitHubClient()

print("Registering repository tools...")
register_repository_tools(mcp, github)

print("Registering issue tools...")
register_issue_tools(mcp, github)

print("Server ready")

if __name__ == "__main__":
    mcp.run()