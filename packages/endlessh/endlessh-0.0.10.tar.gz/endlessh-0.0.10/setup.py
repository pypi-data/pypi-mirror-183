import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="endlessh",
    version="0.0.10",
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="SSH honeypot implemented with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GaoangLiu/pyendlessh",
    packages=setuptools.find_packages(),
    install_requires=['codefast', 'paramiko', 'argparse', 'colorama'],
    entry_points={
        'console_scripts': ['endlessh=endlessh.async_endlessh:endlessh']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
