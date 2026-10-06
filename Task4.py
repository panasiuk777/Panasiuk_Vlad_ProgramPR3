from pathlib import Path
import shutil


SCRIPT_DIR = Path(__file__).resolve().parent
BACKUPS_DIR = SCRIPT_DIR / "backups"

SOURCE_DIR = Path("~/Downloads").expanduser()


def format_size(size):
    if size < 1024:
        return f"{size} B"

    if size < 1024 ** 2:
        return f"{size / 1024:.1f} KB"

    if size < 1024 ** 3:
        return f"{size / (1024 ** 2):.1f} MB"

    return f"{size / (1024 ** 3):.1f} GB"


def main():
    print(f"source directory: {SOURCE_DIR}")

    if not SOURCE_DIR.exists():
        print("error: directory does not exist")
        return

    if not SOURCE_DIR.is_dir():
        print("error: path is not a directory")
        return

    files = [
        path for path in SOURCE_DIR.iterdir()
        if path.is_file()
    ]

    print(f"files found: {len(files)}")

    if not files:
        print("error: directory contains no files")
        return

    print()
    print("files:")

    total_size = 0

    for path in sorted(files):
        size = path.stat().st_size
        total_size += size

        print(
            f"  {path.name:<40} "
            f"{format_size(size):>10}"
        )

    print()
    print(f"total size: {format_size(total_size)}")

    BACKUPS_DIR.mkdir(exist_ok=True)

    backup_dir = BACKUPS_DIR / SOURCE_DIR.name
    backup_dir.mkdir(exist_ok=True)

    print()
    print(f"backup directory: {backup_dir}")

    copied = 0

    for path in files:
        destination = backup_dir / path.name
        shutil.copy2(path, destination)
        copied += 1

    print(f"copied files: {copied}")


if __name__ == "__main__":
    main()
