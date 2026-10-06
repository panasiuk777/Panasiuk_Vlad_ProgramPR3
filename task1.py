from pathlib import Path
import sys


NAME = "Vladik"
SURNAME = "Panasiuk"
GROUP = "IT31"

SCRIPT_DIR = Path(__file__).resolve().parent


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if len(sys.argv) < 2:
        print("usage: python3 task1.py <path> [<path> ...]")
        return 2

    checked = 0
    failed = 0

    for path_text in sys.argv[1:]:
        path = Path(path_text)
        checked += 1

        try:
            if path.is_dir():
                raise IsADirectoryError

            with path.open("r", encoding="utf-8") as file:
                lines = file.readlines()

            if not lines:
                raise ValueError("file is empty")

            first = lines[0].rstrip("\n")

            print(
                f"ok:    {path}: {len(lines)} lines, first: {first}"
            )

        except FileNotFoundError:
            failed += 1
            print(
                f"error: {path}: file not found "
                f"(FileNotFoundError)",
                file=sys.stderr
            )

        except IsADirectoryError:
            failed += 1
            print(
                f"error: {path}: is a directory "
                f"(IsADirectoryError)",
                file=sys.stderr
            )

        except UnicodeDecodeError:
            failed += 1
            print(
                f"error: {path}: not a UTF-8 text file "
                f"(UnicodeDecodeError)",
                file=sys.stderr
            )

        except ValueError:
            failed += 1
            print(
                f"error: {path}: file is empty "
                f"(ValueError)",
                file=sys.stderr
            )

    print(f"checked {checked}, failed {failed}")

    if failed > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
