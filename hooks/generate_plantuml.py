#!/usr/bin/env python3

import subprocess
from os import mkdir, getcwd
from os.path import exists, dirname, join
import argparse
from urllib.request import urlretrieve

__PLANTUML_VERSION__ = "1.2022.5"
__PLANTUML_JARFILE__ = f".plantuml-{__PLANTUML_VERSION__}.jar"


def has_plantuml():
    return exists(__PLANTUML_JARFILE__)


def fetch_plantuml():
    plantuml_download_url = f"https://github.com/plantuml/plantuml/releases/download/v{__PLANTUML_VERSION__}/plantuml-{__PLANTUML_VERSION__}.jar"
    print(f"[generate-plantuml] DEBUG: Downloading PlantUML from {plantuml_download_url}")
    urlretrieve(plantuml_download_url, __PLANTUML_JARFILE__)


def get_output_directory(output_directory, file_path):
    print(f"[generate-plantuml] DEBUG: getting output directory for {file_path}")
    if output_directory == '@':
        finalised_output_directory = dirname(join(getcwd(), file_path))
        print(f'[generate-plantuml] DEBUG: output directory for {file_path} is same as diagram {finalised_output_directory}')
        return finalised_output_directory

    finalised_output_directory = join(getcwd(), output_directory)
    print(f"[generate-plantuml] DEBUG: output directory for {file_path} is project relative {finalised_output_directory}")
    return finalised_output_directory


def process_file(output_directory, output_extension, file_path):
    output_location = get_output_directory(output_directory, file_path)
    if not exists(output_location):
        print("[generate-plantuml] DEBUG: output directory did not exist, creating")
        mkdir(output_location)

    print(f"[generate-plantuml] DEBUG: processing {file_path}")
    subprocess.call([
        'java',
        '-jar',
        __PLANTUML_JARFILE__,
        f'-T{output_extension}',
        '-o', output_location,
        file_path
    ])
    print(f"[generate-plantuml] DEBUG: finished processing {file_path}")


def hook(output_directory, output_extension, file_paths):
    if not has_plantuml():
        fetch_plantuml()

    print(f"[generate-plantuml] DEBUG: running hook with {output_directory}, {output_extension}, {file_paths}")

    for file_path in file_paths:
        process_file(output_directory, output_extension, file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PlantUML Generator Hook')
    parser.add_argument('--output-directory', default="./images")
    parser.add_argument('--output-extension', default="svg")
    parser.add_argument('file_paths', nargs="+")

    args = parser.parse_args()

    print(f"[generate-plantuml] DEBUG: Parsed arguments {args}")

    hook(
        output_directory=args.output_directory,
        output_extension=args.output_extension,
        file_paths=args.file_paths
    )
