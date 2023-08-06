import setuptools

setuptools.setup(
    name="ezslack",
    version="0.1.0",
    author="taekop",
    author_email="taekop@naver.com",
    description="Easy Slack framework wrapping Bolt for Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
