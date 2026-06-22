from typing import Literal, Optional

from pydantic import BaseModel


class GitHubIntent(BaseModel):

    action: Literal[
        "create_repository",
        "list_repositories",
        "delete_repository",
        "create_issue",
        "create_file"
    ]
    repository_name: Optional[str] = None

    issue_title: Optional[str] = None

    file_path: Optional[str] = None

    content: Optional[str] = None