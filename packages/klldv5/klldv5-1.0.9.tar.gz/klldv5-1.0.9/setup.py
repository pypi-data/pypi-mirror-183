import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="klldv5",
    version="1.0.9",
    author="klld",
    description="klldv5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://klld.42web.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'crayons',
          'PirxcyPinger',
          'fortnitepy',
          'BenBotAsync',
          'FortniteAPIAsync',
          'sanic',
          'aiohttp',
          'uvloop',
          'requests'  
      ],
)
