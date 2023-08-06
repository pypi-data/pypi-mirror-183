from setuptools import setup


setup (
    name="formatSlackMessage",
    version="1.0.4",
    description="A project to format the slack messages in a structured way",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=['formatmessage', 'slackoutput', 'slack', 'format'],
    author="Bilal Peerzade",
    author_email="bilalpeerzade@gmail.com",
    packages=['formatslackmessage'],
    package_dir={"":"src"},
    install_requires=[
        "pandas >= 1.1.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Development Status :: 5 - Production/Stable"
    ]
)
