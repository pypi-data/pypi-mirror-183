import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iaewoojinpython", # Replace with your own username
    py_modules=['iaewoojinmysql'],
    version="0.3.1",
    author="Woojin Cho",
    author_email="wooju_1@iae.re.kr",
    description="pymysql Simple used",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IAEWoojinCho",
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)