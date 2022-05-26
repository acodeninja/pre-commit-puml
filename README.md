# pre-commit-puml

---

A [PlantUML](https://plantuml.com/) [pre-commit](https://pre-commit.com/) hook that generates diagrams for use in 
technical documentation.

## Using pre-commit-puml with pre-commit

### Requirements

* Java
* Python3

`.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/acodeninja/pre-commit-puml
    rev: main
    hooks:
      - id: generate_plantuml
        args:
          # The repository root relative directory to output generated images to. 
          # To place generated images in the same directory as the source file, use @
          - --output-directory=./images
          # The file type to use, file names are maintained and extensions swapped.
          - --output-extension=svg
```