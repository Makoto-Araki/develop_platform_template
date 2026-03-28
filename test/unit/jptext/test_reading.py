import pytest

from src.jptext.reading import to_hiragana


@pytest.mark.parametrize(
    "data, expected",
    [
        ("祇園精舎の鐘の声", "ぎおんしょうじゃのかねのこえ"),
        ("ユーラシア大陸", "ゆーらしあたいりく"),
        ("神聖ローマ帝国", "しんせいろーまていこく"),
        ("ティラノサウルス", "てぃらのさうるす"),
        ("貸借対照表", "たいしゃくたいしょうひょう"),
        ("パース造幣局", "ぱーすぞうへいきょく"),
        ("ポルトガル", "ぽるとがる"),
    ],
)
def test_to_hiragana_success_behavior(data, expected):
    """
    日本語文字列の平仮名変換のテスト

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

    assert expected == to_hiragana(data)


@pytest.mark.parametrize(
    "data",
    [
        (100),
        (3.4),
        (True),
        (["月", "火", "水"]),
        (("月", "火", "水")),
        ({"名前": "田中"}),
        (None),
    ],
)
def test_to_hiragana_type_error_behavior(data):
    """
    日本語文字列の平仮名変換でエラー発生テスト

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
        to_hiragana(data)


@pytest.mark.parametrize(
    "data", [("100回"), ("素振り100回"), ("アップル100"), ("0.5キロ"), ("円周率3.14")]
)
def test_to_hiragana_contain_error_behavior(data):
    """
    日本語文字列の平仮名変換でエラー発生テスト

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

    with pytest.raises(
        TypeError, match="text must not contain ASCII letters or digits"
    ):
        to_hiragana(data)
