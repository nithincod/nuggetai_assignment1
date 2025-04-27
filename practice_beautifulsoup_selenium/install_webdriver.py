import os
import subprocess
import requests
import zipfile
import shutil

def get_chrome_version():
    result = subprocess.run(
        ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
        capture_output=True, text=True
    )
    return result.stdout.split(" ")[2]

def download_chromedriver(version):
    major_version = version.split(".")[0]
    print(f"Detected Chrome major version: {major_version}")

    # Get latest compatible chromedriver version
    url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{major_version}"
    latest_version = requests.get(url).text.strip()

    download_url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_mac64.zip"
    print(f"Downloading ChromeDriver {latest_version} from {download_url}")

    response = requests.get(download_url)
    with open("chromedriver.zip", "wb") as f:
        f.write(response.content)

    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    os.remove("chromedriver.zip")
    print("Extracted chromedriver.")

    shutil.move("chromedriver", "/usr/local/bin/chromedriver")
    os.chmod("/usr/local/bin/chromedriver", 0o755)
    print("Moved chromedriver to /usr/local/bin/ and set permissions.")

if __name__ == "__main__":
    chrome_version = get_chrome_version()
    download_chromedriver(chrome_version)
    print("✅ ChromeDriver installed successfully!")
