import pytest

from src.jptext.width import to_half_width


@pytest.mark.parametrize(
    "data, expected",
    [
        ("タナカ", "ﾀﾅｶ"),
        ("タナカABCタナカ", "ﾀﾅｶABCﾀﾅｶ"),
        ("ABCタナカABC", "ABCﾀﾅｶABC"),
        ("１２３", "123"),
        ("１２３123１２３", "123123123"),
        ("123１２３123", "123123123"),
        ("田中", "田中"),
        ("田中ABC田中", "田中ABC田中"),
        ("ABC田中ABC", "ABC田中ABC"),
    ],
)
def test_to_half_width_success_behavior(data, expected):
    """
    全角文字列の半角変換のテスト

    Parameters
    -------
    data
        日本語文字列
    expected
        正しいテスト結果

    Returns
    -------
    None
        なし
    """

    assert expected == to_half_width(data)


@pytest.mark.parametrize(
    "data",
    [
        (-100),
        (0),
        (1000),
        (-0.5),
        (3.14),
        (2 + 3j),
        (True),
        (False),
        ([1, 2, 3]),
        (["a", "b", "c"]),
        ((1, 2, 3)),
        (("a", "b", "c")),
        ({"name": 10000}),
        ({"name": "aaa"}),
        (None),
    ],
)
def test_to_half_width_error_behavior(data):
    """
    全角文字列の半角変換のエラー発生テスト

    Parameters
    -------
    data
        エラー発生用データ

    Returns
    -------
    None
        なし

    Raises
    -------
    TypeError
        エラーメッセージ表示
    """

    with pytest.raises(TypeError, match="text must be str"):
        to_half_width(data)
