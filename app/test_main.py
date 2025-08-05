from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_single_character() -> None:
    assert is_isogram("a")
    assert is_isogram("b")


def test_isogram() -> None:
    assert is_isogram("word")
    assert is_isogram("isogram")


def test_not_isogram() -> None:
    assert not is_isogram("hello")
    assert not is_isogram("test")


def test_mixed_case() -> None:
    assert is_isogram("Isogram") is True
    assert is_isogram("Hello") is False
    assert is_isogram("Test") is False
