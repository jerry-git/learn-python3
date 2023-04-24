from pathlib import Path
import subprocess
import sys


def main():
    path = sys.argv[1]
    if path.strip().lower() == "all":
        convert_all_notebooks_to_html()
    else:
        convert_notebook_to_html(path)


def convert_all_notebooks_to_html():
    notebook_dir = Path(__file__).parent.parent / "notebooks"
    for directory in (
        notebook_dir / "beginner" / "notebooks",
        notebook_dir / "intermediate" / "notebooks",
    ):
        for notebook_path in directory.glob("*.ipynb"):
            convert_notebook_to_html(notebook_path)


def convert_notebook_to_html(notebook_path):
    path = Path(notebook_path)
    if not path.exists():
        raise SystemExit(f"Invalid path {path}")

    output_dir = path.parent.parent / "html"

    cmd = f"jupyter nbconvert --to html --execute --ExecutePreprocessor.timeout=30 --output-dir {output_dir} {path.absolute()}"
    subprocess.check_call(cmd.split())


if __name__ == "__main__":
    main()
