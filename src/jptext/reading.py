import re

from pykakasi import kakasi


# --------------------------------------------------
# 日本語文字列を読み仮名に変換
# --------------------------------------------------
def to_hiragana(text: str) -> str:
    """
    日本語文字列を読み仮名に変換する。
    - 漢字を平仮名に変換
    - 片仮名を平仮名に変換
    - 平仮名は平仮名のまま

    Parameters
    ----------
    text : str
        変換対象の文字列

    Returns
    -------
    str
        読み仮名に変換された文字列

    Raises
    ------
    TypeError
        - text が str 型でない場合
        - text に半角英数字が検出された場合
    """

    if not isinstance(text, str):
        raise TypeError("text must be str")

    _ASCII_PATTERN = re.compile(r"[A-Za-z0-9]")

    if _ASCII_PATTERN.search(text):
        raise TypeError("text must not contain ASCII letters or digits")

    kks = kakasi()
    result = kks.convert(text)

    return "".join(item["hira"] for item in result)
