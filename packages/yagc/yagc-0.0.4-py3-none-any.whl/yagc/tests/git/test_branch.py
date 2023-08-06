from yagc.git.branch_validator import BranchValidator


def test_feature_branch():
    correct_feature_branch_examples = [
        "feature/feature-1",
        "feature/yes",
    ]
    for branch in correct_feature_branch_examples:
        branch_validator = BranchValidator(branch)
        assert branch_validator.valid_branch()

    wrong_feature_branch_examples = [
        "fature/feature-1",
        "feaure/yes",
    ]
    for branch in wrong_feature_branch_examples:
        branch_validator = BranchValidator(branch)
        assert not branch_validator.valid_branch()


def test_bugfix_branch():
    correct_bugfix_branch_examples = [
        "bugfix/feature-1",
        "bugfix/yes",
    ]
    for branch in correct_bugfix_branch_examples:
        branch_validator = BranchValidator(branch)
        assert branch_validator.valid_branch()

    wrong_bugfix_branch_examples = [
        "buugfix/feature-1",
        "boe/yes",
    ]
    for branch in wrong_bugfix_branch_examples:
        branch_validator = BranchValidator(branch)
        assert not branch_validator.valid_branch()


def test_hotfix_branch():
    correct_hotfix_branch_examples = [
        "hotfix/feature-1",
        "hotfix/yes",
    ]
    for branch in correct_hotfix_branch_examples:
        branch_validator = BranchValidator(branch)
        assert branch_validator.valid_branch()

    wrong_hotfix_branch_examples = [
        "hoatfix/feature-1",
    ]
    for branch in wrong_hotfix_branch_examples:
        branch_validator = BranchValidator(branch)
        assert not branch_validator.valid_branch()


def test_release_branch():
    correct_release_branch_examples = [
        "release/1.0.0",
        "release/0.0.1",
    ]
    for branch in correct_release_branch_examples:
        branch_validator = BranchValidator(branch)
        assert branch_validator.valid_branch()

    wrong_release_branch_examples = [
        "release/1.0",
        "release/2.2",
        "realease/2.2",
    ]
    for branch in wrong_release_branch_examples:
        branch_validator = BranchValidator(branch)
        assert not branch_validator.valid_branch()
