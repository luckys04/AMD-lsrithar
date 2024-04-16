import subprocess
import sys

# Function to install a Python package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

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

# Function to install all required packages
def install_packages(packages):
    for package in packages:
        install_package(package)

# Install requests if not already installed
try:
    import requests
except ImportError:
    print("Installing 'requests' library...")
    install_package("requests")
    import requests

# Install all required packages
install_packages(packages)

print("All required packages installed successfully!")
