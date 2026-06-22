from github import Github
from dotenv import load_dotenv
import os

load_dotenv()


class GitHubClient:

    def __init__(self):

        token = os.getenv("GITHUB_TOKEN")

        if not token:
            raise ValueError(
                "GITHUB_TOKEN not found"
            )

        self.github = Github(token)

        self.user = self.github.get_user()