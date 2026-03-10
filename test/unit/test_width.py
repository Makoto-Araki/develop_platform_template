import pytest
from src.jptext.width import to_half_width

@pytest.mark.parametrize(
    'a, expected',
    [
        ('タナカ', 'ﾀﾅｶ'),
        ('タナカABCタナカ', 'ﾀﾅｶABCﾀﾅｶ'),
        ('ABCタナカABC', 'ABCﾀﾅｶABC'),
        ('１２３', '123'),
        ('１２３123１２３', '123123123')
    ]
)
def test_to_half_width(a, expected):
    assert expected == to_half_width(a)

