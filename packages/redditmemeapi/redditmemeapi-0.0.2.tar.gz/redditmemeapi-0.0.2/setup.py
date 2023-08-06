import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='redditmemeapi',                           # should match the package folder
    packages=['redditmemeapi'],                     # should match the package folder
    version='0.0.2',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='A pythonic API wrapper to fetch memes from https://meme-api.com',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='thereal_cyber',
    author_email='quantechlxxi.corp@gmail.com',
    url='https://github.com/therealcyber71/redditmemeapi', 
    project_urls = {                                # Optional
        "APIs": "https://github.com/therealcyber71/redditmemeapi/issues"
    },
    install_requires=[], #these are filler packages, you need to fill them with the packages your python package will require to function                 
    keywords=["memes", "api", "discord", "telegram"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]

    )