import subprocess


def get_chrome_version():
    result = subprocess.run(
        ["google-chrome", "--version"], capture_output=True, text=True
    )
    return result.stdout.strip()


def get_chromedriver_version():
    result = subprocess.run(
        ["chromedriver", "--version"], capture_output=True, text=True
    )
    return result.stdout.strip()


def test_chrome_version():
    version = get_chrome_version()
    assert "Google Chrome" in version


def test_chromedriver_version():
    version = get_chromedriver_version()
    assert "ChromeDriver" in version
