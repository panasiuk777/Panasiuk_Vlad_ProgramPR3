from pathlib import Path
import sys


NAME = "Vladik"
SURNAME = "Panasiuk"
GROUP = "IT31"


def usage():
    print("usage: python3 task2.py [--force] <source> <destination>")


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]

    force = False

    if args and args[0] == "--force":
        force = True
        args = args[1:]

    if len(args) != 2:
        usage()
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        if not source.exists():
            raise FileNotFoundError

        if source.is_dir():
            raise IsADirectoryError("source")

        if destination.exists() and destination.is_dir():
            raise IsADirectoryError("destination")

        if destination.exists():
            if source.resolve() == destination.resolve():
                print(
                    "error: source and destination are the same file",
                    file=sys.stderr
                )
                return 1

            if not force:
                print(
                    f"error: {destination} already exists, "
                    f"use --force to overwrite",
                    file=sys.stderr
                )
                return 1

        if not destination.parent.exists():
            print(
                f"error: destination folder {destination.parent} not found",
                file=sys.stderr
            )
            return 1

        with source.open("r", encoding="utf-8") as src:
            content = src.read()

        with destination.open("w", encoding="utf-8") as dst:
            dst.write(content)

        print(f"copied: {source} -> {destination}")
        return 0

    except FileNotFoundError:
        print(
            f"error: source {source} not found",
            file=sys.stderr
        )
        return 1

    except IsADirectoryError as error:
        if str(error) == "source":
            print(
                f"error: source {source} is a directory, not a file",
                file=sys.stderr
            )
        else:
            print(
                f"error: destination {destination} is a directory, not a file",
                file=sys.stderr
            )
        return 1

    except UnicodeDecodeError:
        print(
            f"error: source {source} is not a UTF-8 text file",
            file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
