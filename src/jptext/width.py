import jaconv

# --------------------------------------------------
# 日本語文字列を半角に正規化
# --------------------------------------------------
def to_half_width(text: str) -> str:
    """
    日本語文字列を半角に正規化する。
    - 全角カナを半角カナに変換
    - 全角英数字を半角英数字に変換

    Parameters
    -------
    text : str
        変換対象の文字列

    Returns
    -------
    str
        半角化された文字列

    Raises
    -------
    TypeError
        text が str 型でない場合
    """

    if not isinstance(text, str):
        raise TypeError('text must be str')

    return jaconv.z2h(text, kana=True, ascii=True, digit=True)