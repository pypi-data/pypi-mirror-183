from semver import Version


class BranchValidator:
    def __init__(self, branch: str) -> None:
        self.branch = branch

    def valid_branch(self) -> bool:
        return any(
            [
                self.__valid_main_branch(),
                self.__valid_feature_branch(),
                self.__valid_bugfix_branch(),
                self.__valid_hotfix_branch(),
                self.__valid_release_branch(),
            ]
        )

    def __valid_main_branch(self) -> bool:
        return self.branch == "main"

    def __valid_feature_branch(self) -> bool:
        return self.branch.startswith("feature/")

    def __valid_bugfix_branch(self) -> bool:
        return self.branch.startswith("bugfix/")

    def __valid_hotfix_branch(self) -> bool:
        return self.branch.startswith("hotfix/")

    def __valid_release_branch(self) -> bool:
        if self.branch.startswith("release/"):
            try:
                Version.parse(self.branch.replace("release/", ""))
                return True
            except ValueError:
                return False
        else:
            return False
