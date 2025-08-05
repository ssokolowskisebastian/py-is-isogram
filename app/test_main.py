from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert (is_isogram("seba"))
    assert (is_isogram("abcd"))
    assert (is_isogram(""))
    assert (is_isogram("qwertyuiop"))
    assert (is_isogram("zxcvbnm"))


def test_is_isogram_false() -> None:
    assert (not is_isogram("oppo"))
    assert (not is_isogram("dada"))
    assert (not is_isogram("bb"))
    assert (not is_isogram("abba"))
