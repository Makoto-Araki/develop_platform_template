import subprocess


def get_chrome_version():
    """
    Chromeのバージョン情報取得

    Parameters
    -------
    None
        なし

    Returns
    -------
    result.stdout.strip()
        Chromeのバージョン情報
    """

    result = subprocess.run(
        ["google-chrome", "--version"], capture_output=True, text=True
    )
    return result.stdout.strip()


def get_chromedriver_version():
    """
    ChromeDriverのバージョン情報取得

    Parameters
    -------
    None
        なし

    Returns
    -------
    result.stdout.strip()
        ChromeDriverのバージョン情報
    """

    result = subprocess.run(
        ["chromedriver", "--version"], capture_output=True, text=True
    )
    return result.stdout.strip()


def test_chrome_version():
    """
    Chromeのバージョン情報取得のテスト

    Parameters
    -------
    None
        なし

    Returns
    -------
    None
        なし
    """

    version = get_chrome_version()
    assert "Google Chrome" in version


def test_chromedriver_version():
    """
    ChromeDriverのバージョン情報取得のテスト

    Parameters
    -------
    None
        なし

    Returns
    -------
    None
        なし
    """

    version = get_chromedriver_version()
    assert "ChromeDriver" in version
