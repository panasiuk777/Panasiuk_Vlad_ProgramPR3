from pathlib import Path


def main():
    script = Path(__file__).resolve()
    script_dir = script.parent
    cwd = Path.cwd()
    home = Path.home()

    data_dir = script_dir / "data"
    reports_dir = script_dir / "reports"
    backups_dir = script_dir / "backups"

    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    backups_dir.mkdir(exist_ok=True)

    profile_path = data_dir / "profile.txt"

    profile_data = [
        "name: Vladik",
        "surname: Panasiuk",
        "group: IT31",
        "year: 2009",
        "language: German",
    ]

    profile_path.write_text(
        "\n".join(profile_data) + "\n",
        encoding="utf-8"
    )

    print(f"cwd:         {cwd}")
    print(f"script:      {script}")
    print(f"script dir:  {script_dir}")
    print(f"home:        {home}")

    print()

    print(f"profile path: {profile_path}")
    print(f"relative:     {profile_path.relative_to(script_dir)}")
    print(f"name:         {profile_path.name}")
    print(f"stem:         {profile_path.stem}")
    print(f"suffix:       {profile_path.suffix}")
    print(f"parent:       {profile_path.parent.name}")
    print(f"size:         {profile_path.stat().st_size} bytes")

    print()
    print("project tree:")

    for path in sorted(script_dir.rglob("*")):
        relative = path.relative_to(script_dir)

        if path.is_dir():
            print("  " * len(relative.parts) + f"{path.name}/")
        else:
            print("  " * len(relative.parts) + path.name)


if __name__ == "__main__":
    main()
