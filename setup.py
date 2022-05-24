import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pre-commit-puml",
    version="0.0.1",
    description="A PlantUML pre-commit hook that generates diagrams for use in technical documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acodeninja/pre-commit-puml",
    project_urls={
        "Bug Tracker": "https://github.com/acodeninja/pre-commit-puml/issues",
    },
    package_dir={"": "hooks"},
    scripts=['hooks/generate_plantuml.py'],
    python_requires=">=3.6",
)
