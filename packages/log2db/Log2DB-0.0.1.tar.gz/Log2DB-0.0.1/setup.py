import setuptools

setuptools.setup(
    name="Log2DB",
    version="0.0.1",
    license='MIT',
    author="WooSung Jo",
    author_email="jwsjws99@gmail.com",
    description="Send Deep Learning Training,Test Log To DB",
    long_description=open('README.md').read(),
    url="https://github.com/Oldentomato/Log2DB",
    package_dir={"":"Log2DB"},
    packages=setuptools.find_packages(where="Log2DB"),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)