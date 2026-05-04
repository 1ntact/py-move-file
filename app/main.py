import os
import shutil


def move_file(command: str) -> None:

    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)
    dir_path = os.path.dirname(destination)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    shutil.move(source, destination)
