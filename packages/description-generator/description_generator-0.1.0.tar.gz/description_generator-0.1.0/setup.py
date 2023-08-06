from setuptools import setup

setup(
    name="description_generator",
    version="0.1.0",
    py_modules=["description_generator"],
    entry_points={
        "console_scripts": [
            "description_generator=description_generator:main"
        ]
    },
    description="Generate a personal description for a GitHub user's profile.",
    author="Wadjih Bencheikh",
    author_email="jw_bencheikh@esi.dz",
    install_requires=[
        "openai",
        "requests"
    ],
)
