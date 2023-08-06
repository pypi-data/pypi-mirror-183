from yagc.github.repository_settings import RepositorySettings


def valid_repository_settings(settings: RepositorySettings) -> bool:
    assert settings.client.allow_squash_merge
    assert not settings.client.allow_merge_commit
    assert not settings.client.allow_rebase_merge
    assert settings.client.has_issues
    assert not settings.client.has_projects
    assert not settings.client.has_wiki
    assert settings.client.delete_branch_on_merge

    # TODO, not enabled yet assert settings.enable_auto_merge

    return True


def test_sample_repository_settings():
    settings = RepositorySettings("neon-law", "yagc")

    assert valid_repository_settings(settings)
