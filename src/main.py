import os
import sys


class Main:
    """
    メインクラス

    Methods
    -------
    run
        メイン処理
    """

    def run(self) -> None:
        """
        メイン処理

        Parameters
        -------
        None
            なし

        Returns
        -------
        None
            なし
        """

        print("Hello")
        print(os.listdir("jptext"))
        print(sys.version)


if __name__ == "__main__":
    main = Main()
    main.run()
