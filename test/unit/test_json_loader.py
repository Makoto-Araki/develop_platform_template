"""
json_loader モジュールの単体テスト

load_json_to_dict
1. 正常系テスト
    JSONファイルを辞書に変換
2. 異常系テスト
    JSONファイルが存在しない
3. 異常系テスト
    JSONファイルの解析に失敗

load_jsons_from_directory
1. 正常系テスト
    フォルダ内のJSONファイルを全て読み込み
2. 異常系テスト
    フォルダが存在しない
3. 正常系テスト
    フォルダ内のJSONファイル以外は無視
"""

import json
import pytest
from src.json_utils.json_loader import (
    load_json_to_dict,
    load_jsons_from_directory
)

# --------------------------------------------------
# load_json_to_dictテスト
# --------------------------------------------------

def test_load_json_to_dict_success(tmp_path):

    test_data = {
        "name": "Alice",
        "age": 30
    }

    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(test_data), encoding="utf-8")
    result = load_json_to_dict(file_path)

    assert result == test_data

def test_load_json_to_dict_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_json_to_dict("not_exist.json")

def test_load_json_to_dict_invalid_json(tmp_path):

    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(ValueError):
        load_json_to_dict(file_path)

# --------------------------------------------------
# load_jsons_from_directoryテスト
# --------------------------------------------------

def test_load_jsons_from_directory_success(tmp_path):
    data1 = {
        "name": "Alice",
        "age": 30
    }
    data2 = {
        "name": "Bob",
        "age": 25
    }

    file1 = tmp_path / "a.json"
    file2 = tmp_path / "b.json"

    file1.write_text(json.dumps(data1), encoding="utf-8")
    file2.write_text(json.dumps(data2), encoding="utf-8")

    result = load_jsons_from_directory(tmp_path)

    assert data1 in result
    assert data2 in result
    assert len(result) == 2

def test_load_jsons_from_directory_not_found():
    with pytest.raises(FileNotFoundError):
        load_jsons_from_directory("not_exist_dir")

def test_load_jsons_from_directory_ignore_non_json(tmp_path):
    data = {
        "name": "Alice",
        "age": 30
    }

    json_file = tmp_path / "data.json"
    txt_file = tmp_path / "data.txt"

    json_file.write_text(json.dumps(data), encoding="utf-8")
    txt_file.write_text("text file", encoding="utf-8")

    result = load_jsons_from_directory(tmp_path)

    assert result == [data]