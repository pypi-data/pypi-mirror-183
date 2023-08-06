from setuptools import setup
long_description = open("README.md", "r").read()
setup(
    name="description_generator",
    version="0.1.3",
    py_modules=["description_generator"],
    entry_points={
        "console_scripts": [
            "description_generator=description_generator:main"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Generate a personal description for a GitHub user's profile.",
    author="Wadjih Bencheikh",
    author_email="jw_bencheikh@esi.dz",
    install_requires=[
        "openai",
        "requests"
    ],
)
