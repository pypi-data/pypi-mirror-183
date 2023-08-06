import setuptools

setuptools.setup(
    name="ATS-Library",
    version="0.1",
    author="Gu Xin",
    author_email="g_xin@outlook.com",
    maintainer="Gu Xin",
    maintainer_email="g_xin@outlook.com",
    url="https://github.com/isguxin/ATS-Library",
    license="MIT",
    description="Auto Test Suite Library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    platforms=["Windows", "Linux", "Unix", "Mac OS-X"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="auto test suite library",
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.txt", "*.rst", "*.md", "*.json", "*.yaml", "*.yml", "*.xml", "*.ini", "*.csv"]
    },
    data_files=[("", ["LICENSE"])],
    python_requires=">=3.8" and "<3.11",
    install_requires=[
        "requests",
        "websocket-client",
        "colorlog",
        "sqlalchemy",
        "treelib",
        "PyYAML",
        "easy-ocr",
        "ddddocr",
        "selenium"
    ],
    zip_safe=False,
)
