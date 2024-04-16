import subprocess

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

def install_notepad_plus_plus():
    try:
        subprocess.run(["choco", "install", "notepadplusplus", "--version", "8.4.8", "-y"], check=True)
    except FileNotFoundError:
        print("Chocolatey is not installed. Please install Chocolatey before running this script.")

def install_vscode():
    try:
        subprocess.run(["choco", "install", "vscode", "-y"], check=True)
    except FileNotFoundError:
        print("Chocolatey is not installed. Please install Chocolatey before running this script.")

def install_papi2():
    try:
        subprocess.run(["pip", "install", "-i", "http://mkmartifactory.amd.com/artifactory/api/pypi/fw-papi2pyapi-prod-virtual/simple", "papi2", "--trusted-host", "mkmartifactory.amd.com", "--upgrade"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error installing papi2:", e)

def main():
    try:
        # Install Python 3.7.9 if not installed
        subprocess.run(["python3.7.9", "--version"], check=True)
    except FileNotFoundError:
        print("Python 3.7.9 not found. Please install Python 3.7.9 before running this script.")
        return

    # Install packages
    install_packages(packages)

    # Install Notepad++ 8.4.8
    install_notepad_plus_plus()

    # Install Visual Studio Code
    install_vscode()

    print("Before installing 'papi2', make sure to download 'ahds'.")

    # Install papi2
    install_papi2()

if __name__ == "__main__":
    main()
