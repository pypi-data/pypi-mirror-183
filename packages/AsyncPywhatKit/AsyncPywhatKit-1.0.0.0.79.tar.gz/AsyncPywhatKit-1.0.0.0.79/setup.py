from setuptools import setup
import pathlib


def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="AsyncPywhatKit",
    packages=['AsyncPywhatKit'],
    version="1.0.0.0.79",
    license="MIT",
    description="AsyncPywhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features",
    author="SigireddyBalasai",
    author_email="sigireddybalasai@gmail.com",
    url="https://github.com/SigireddyBalasai/PyWhatKit",
    download_url="https://github.com/SigireddyBalasai/AsyncPywhatKit/archive/refs/tags/1.0.tar.gz",
    keywords=["sendwhatmsg", "info", "playonyt", "search", "watch_tutorial", "async pywhatkit"],
    install_requires=requirements(),
    package_data={"pywhatkit": ["py.typed"]},
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
