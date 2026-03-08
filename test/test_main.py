import sys
from pathlib import Path

# プロジェクトルートをパスに追加
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.main import Main

def test_run_outputs_hello(capsys):
    main = Main()
    main.run()

    captured = capsys.readouterr()
    assert captured.out == "Hello\n"
