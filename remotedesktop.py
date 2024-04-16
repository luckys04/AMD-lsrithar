import subprocess
import requests
import os

# List of packages with versions
packages = [
    "BitVector==3.5.0",
    "certifi==2022.12.7",
    "charset-normalizer==3.1.0",
    "Deprecated==1.2.13",
    "dohq-artifactory==0.9.2",
    "enum-tools==0.11.0",
    "et-xmlfile==1.1.0",
    "idna==3.4",
    "keyboard==0.13.5",
    "multipledispatch==0.6.0",
    "numpy==1.21.6",
    "openpyxl==3.1.2",
    "pandas==1.3.5",
    "pygments==2.17.2",
    "PyJWT==2.8.0",
    "pyparsing==3.1.1",
    "pyreadline3==3.4.1",
    "pyserial==3.5",
    "python-dateutil==2.8.2",
    "pytz==2023.3.post1",
    "pyzmq==25.0.2",
    "requests==2.30.0",
    "setuptools==47.1.0",
    "six==1.16.0",
    "typing-extensions==4.7.1",
    "urllib3==2.0.2",
    "wrapt==1.15.0"
]

def install_packages(packages):
    for package in packages:
        subprocess.run(["pip", "install", package], check=True)

def download_and_install_notepad_plus_plus():
    url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.8/npp.8.4.8.Installer.exe"
    filename = os.path.basename(url)
    with open(filename, "wb") as f:
        response = requests.get(url)
        f.write(response.content)
    subprocess.run([filename, "/S"], check=True)
    os.remove(filename)

def download_and_install_vscode():
    url = "https://update.code.visualstudio.com/latest/win32-archive/stable"
    response = requests.get(url)
    download_url = response.url
    filename = os.path.basename(download_url)
    with open(filename, "wb") as f:
        response = requests.get(download_url)
        f.write(response.content)
    subprocess.run([filename, "/verysilent"], check=True)
    os.remove(filename)

def main():
    try:
        # Install Python 3.7.9 if not installed
        subprocess.run(["python3.7.9", "--version"], check=True)
    except FileNotFoundError:
        print("Python 3.7.9 not found. Please install Python 3.7.9 before running this script.")
        return

    # Install packages
    install_packages(packages)

    # Download and install Notepad++
    download_and_install_notepad_plus_plus()

    # Download and install Visual Studio Code
    download_and_install_vscode()

if __name__ == "__main__":
    main()
