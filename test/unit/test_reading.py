"""
reading モジュールの単体テスト

to_hiragana
1. 正常系テスト
    日本語文字列が正しく平仮名へ変換されること
2. 異常系テスト
    引数の text がstr型でない場合にTypeError例外発生
3. 異常系テスト
    引数の text にASCII文字が含まれている場合にTypeError例外発生
"""

import pytest
from src.jptext.reading import to_hiragana

# --------------------------------------------------
# to_hiraganaテスト
# --------------------------------------------------

@pytest.mark.parametrize(
    'a, expected',
    [
        ('祇園精舎の鐘の声', 'ぎおんしょうじゃのかねのこえ'),
        ('ユーラシア大陸', 'ゆーらしあたいりく'),
        ('神聖ローマ帝国', 'しんせいろーまていこく'),
        ('ティラノサウルス', 'てぃらのさうるす'),
        ('貸借対照表', 'たいしゃくたいしょうひょう'),
        ('パース造幣局', 'ぱーすぞうへいきょく'),
        ('ポルトガル', 'ぽるとがる'),
    ]
)
def test_to_hiragana_success_behavior(a, expected):
    assert expected == to_hiragana(a)

@pytest.mark.parametrize(
    'a',
    [
        (100),
        (3.4),
        (True),
        (['月', '火', '水']),
        (('月', '火', '水')),
        ({"名前": '田中'}),
        (None)
    ]
)
def test_to_hiragana_type_error_behavior(a):
    with pytest.raises(TypeError, match='text must be str'):
        to_hiragana(a)

@pytest.mark.parametrize(
    'a',
    [
        ('100回'),
        ('素振り100回'),
        ('アップル100'),
        ('0.5キロ'),
        ('円周率3.14')
    ]
)
def test_to_hiragana_contain_error_behavior(a):
    with pytest.raises(TypeError, match='text must not contain ASCII letters or digits'):
        to_hiragana(a)
