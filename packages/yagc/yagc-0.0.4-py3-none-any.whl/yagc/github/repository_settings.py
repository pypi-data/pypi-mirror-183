from os import environ

from github import Github


class RepositorySettings:
    def __init__(
        self,
        organization: str,
        repository: str,
        github_url=environ.get("GITHUB_URL", None),
        github_pat=environ.get("GITHUB_TOKEN"),
    ) -> None:
        self.github_client = self.__create_github_client(
            github_url=github_url, github_pat=github_pat
        )
        self.client = self.github_client.get_repo(f"{organization}/{repository}")

    def sync(self) -> bool:
        self.client.edit(
            allow_squash_merge=True,
            allow_merge_commit=False,
            allow_rebase_merge=False,
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            delete_branch_on_merge=True,
        )

    def update_description(self, description: str) -> bool:
        self.client.edit(description=description)

    def __create_github_client(self, github_url, github_pat) -> Github:
        if github_url:
            return Github(base_url=github_url, login_or_token=github_pat)
        else:
            return Github(login_or_token=github_pat)
