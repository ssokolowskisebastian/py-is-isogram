from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("seba") is True
    assert is_isogram("abcd") is True
    assert is_isogram("qwertyuiop") is True
    assert is_isogram("zxcvbnm") is True


def test_is_isogram_false() -> None:
    assert is_isogram("oppo") is False
    assert is_isogram("look") is False
    assert is_isogram("pineapple") is False


def test_is_isogram_case_sensitive() -> None:
    assert is_isogram("OpPo") is False
    assert is_isogram("LOok") is False
    assert is_isogram("pineapPle") is False


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True
