from setuptools import setup, find_packages

setup(
    name = 'phalanx',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/phalanx.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "phalanx is a password generator with any file",
    install_requires = ['setuptools', "hashlib"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "phalanx = phalanx.phalanx:main",
        ]
    }
)
