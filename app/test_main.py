from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("b") is True


def test_isogram() -> None:
    assert is_isogram("word") is True
    assert is_isogram("isogram") is True


def test_not_isogram() -> None:
    assert is_isogram("hello") is False
    assert is_isogram("test") is False


def test_mixed_case() -> None:
    assert is_isogram("Isogram") is True
    assert is_isogram("Hello") is False
    assert is_isogram("Test") is False
