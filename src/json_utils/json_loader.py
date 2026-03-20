import json
from pathlib import Path


# --------------------------------------------------
# JSONファイルを読み込み辞書に変換する
# --------------------------------------------------
def load_json_to_dict(file_path: str) -> dict:
    """
    JSONファイルを読み込み辞書に変換する

    Parameters
    -------
    file_path : str
        JSONファイルのパス

    Returns
    -------
    dict
        辞書

    Raises
    -------
    FileNotFoundError
        JSONファイルが存在しない場合
    ValueError
        JSONファイルの解析失敗
    """

    try:
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"JSONの解析に失敗しました: {e}") from e


# --------------------------------------------------
# フォルダ内のJSONファイルを辞書リストで返す
# --------------------------------------------------
def load_jsons_from_directory(dir_path: str) -> list[dict]:
    """
    フォルダ内のJSONファイルを辞書リストで返す

    Parameters
    ----------
    dir_path : str
        JSONファイルが格納されたフォルダ

    Returns
    -------
    list[dict]
        JSONを辞書に変換したリスト

    Raises
    -------
    FileNotFoundError
        フォルダが存在しない場合
    """

    path = Path(dir_path)

    if not path.exists():
        raise FileNotFoundError(f"フォルダが存在しません: {dir_path}")

    result: list[dict] = []

    for json_file in path.glob("*.json"):
        data = load_json_to_dict(str(json_file))
        result.append(data)

    return result
