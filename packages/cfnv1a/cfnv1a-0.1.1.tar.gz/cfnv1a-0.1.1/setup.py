from setuptools import Extension, setup



setup(
    name="cfnv1a",
    version="0.1.1",
    ext_modules=[Extension("cfnv1a", ["cfnv1a.c"])],
    description="fnv1a c implementation for python",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    license="MIT",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    url="https://github.com/mosquito/cfnv1a/",
    keywords=["fnv1a", "c"],
    packages=["."],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
    ],
    python_requires=">=3.7.*, <4",
)
