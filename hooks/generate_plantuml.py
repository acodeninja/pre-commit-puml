import subprocess
from os import mkdir, getcwd, path
from os.path import exists
import argparse
from urllib.request import urlretrieve

__PLANTUML_VERSION__ = "1.2022.5"
__PLANTUML_JARFILE__ = f".plantuml-{__PLANTUML_VERSION__}.jar"


def has_plantuml():
    return exists(__PLANTUML_JARFILE__)


def fetch_plantuml():
    plantuml_download_url = f"https://github.com/plantuml/plantuml/releases/download/v{__PLANTUML_VERSION__}/plantuml-{__PLANTUML_VERSION__}.jar"
    print(f"DEBUG: Downloading PlantUML from {plantuml_download_url}")
    urlretrieve(plantuml_download_url, __PLANTUML_JARFILE__)


def hook(output_directory, output_extension, file_paths):
    if not has_plantuml():
        fetch_plantuml()

    if not exists(output_directory):
        mkdir(output_directory)

    for file_path in file_paths:
        print(f"DEBUG: processing {file_path}")
        subprocess.call([
            'java',
            '-jar',
            __PLANTUML_JARFILE__,
            f'-T{output_extension}',
            '-o', output_directory,
            file_path
        ])
        print(f"DEBUG: finished processing {output_directory}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PlantUML Generator Hook')
    parser.add_argument('--output-directory', default="./images")
    parser.add_argument('--output-extension', default="svg")
    parser.add_argument('file_paths', nargs="+")

    args = parser.parse_args()
    
    output_directory = path.join(getcwd(), args.output_directory)

    print(f"DEBUG: Parsed arguments {args}")

    hook(
        output_directory,
        output_extension=args.output_extension,
        file_paths=args.file_paths
    )
