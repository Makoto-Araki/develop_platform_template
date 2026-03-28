import json

import pytest

from src.json_utils.json_loader import load_json_to_dict, load_jsons_from_directory


def test_load_json_to_dict_success(tmp_path):
    """
    JSONファイルを作成後に辞書に変換するテスト

    Parameters
    -------
    tmp_path
        JSONファイルのパス

    Returns
    -------
    None
        なし
    """

    test_data = {"name": "Alice", "age": 30}
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(test_data), encoding="utf-8")
    result = load_json_to_dict(file_path)

    assert result == test_data


def test_load_json_to_dict_file_not_found():
    """
    存在しないJSONファイルを指定してエラー発生テスト

    Parameters
    -------
    None
        なし

    Returns
    -------
    None
        なし

    Raises
    -------
    FileNotFoundError
        エラーメッセージ表示
    """

    with pytest.raises(FileNotFoundError):
        load_json_to_dict("not_exist.json")


def test_load_json_to_dict_invalid_json(tmp_path):
    """
    不正なJSONファイルを指定してエラー発生テスト

    Parameters
    -------
    tmp_path
        不正なJSONファイルのパス

    Returns
    -------
    None
        なし

    Raises
    -------
    ValueError
        エラーメッセージ表示
    """

    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(ValueError):
        load_json_to_dict(file_path)


def test_load_jsons_from_directory_success(tmp_path):
    """
    ディレクトリ内のJSONファイルを辞書リストに変換するテスト

    Parameters
    -------
    tmp_path
        ディレクトリのパス

    Returns
    -------
    None
        なし
    """

    data1 = {"name": "Alice", "age": 30}
    data2 = {"name": "Bob", "age": 25}
    file1 = tmp_path / "a.json"
    file2 = tmp_path / "b.json"
    file1.write_text(json.dumps(data1), encoding="utf-8")
    file2.write_text(json.dumps(data2), encoding="utf-8")
    result = load_jsons_from_directory(tmp_path)

    assert data1 in result
    assert data2 in result
    assert len(result) == 2


def test_load_jsons_from_directory_not_found():
    """
    存在しないディレクトリを指定してエラー発生テスト

    Parameters
    -------
    None
        なし

    Returns
    -------
    None
        なし

    Raises
    -------
    FileNotFoundError
        エラーメッセージ表示
    """

    with pytest.raises(FileNotFoundError):
        load_jsons_from_directory("not_exist_dir")


def test_load_jsons_from_directory_ignore_non_json(tmp_path):
    """
    ディレクトリ内のJSONファイルのみを辞書リストに変換するテスト

    Parameters
    -------
    tmp_path
        ディレクトリのパス

    Returns
    -------
    None
        なし
    """

    data = {"name": "Alice", "age": 30}
    json_file = tmp_path / "data.json"
    txt_file = tmp_path / "data.txt"
    json_file.write_text(json.dumps(data), encoding="utf-8")
    txt_file.write_text("text file", encoding="utf-8")
    result = load_jsons_from_directory(tmp_path)

    assert result == [data]
