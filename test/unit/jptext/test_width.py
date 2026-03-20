"""
width モジュールの単体テスト

to_half_width
1. 正常系テスト
    日本語文字列のみ半角に変換
2. 異常系テスト
    引数の text がstr型でない場合にTypeError例外発生
"""

import pytest

from src.jptext.width import to_half_width

# --------------------------------------------------
# to_half_widthテスト
# --------------------------------------------------


@pytest.mark.parametrize(
    "a, expected",
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
def test_to_half_width_success_behavior(a, expected):
    assert expected == to_half_width(a)


@pytest.mark.parametrize(
    "a",
    [
        (-100),  # int
        (0),  # int
        (1000),  # int
        (-0.5),  # float
        (3.14),  # float
        (2 + 3j),  # complex
        (True),  # bool
        (False),  # bool
        ([1, 2, 3]),  # list
        (["a", "b", "c"]),  # list
        ((1, 2, 3)),  # tuple
        (("a", "b", "c")),  # tuple
        ({"name": 10000}),  # dict
        ({"name": "aaa"}),  # dict
        (None),
    ],
)
def test_to_half_width_error_behavior(a):
    with pytest.raises(TypeError, match="text must be str"):
        to_half_width(a)
