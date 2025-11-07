from pathlib import Path
import requests

CURRENT_DIR = Path(__file__).parent.absolute()
DATA_DIR = CURRENT_DIR / "data"
INPUTS_DIR = DATA_DIR / "inputs"
INPUTS_DIR.mkdir(exist_ok=True, parents=True)
SESSION_FILE = DATA_DIR / "session.txt"
if not SESSION_FILE.exists():
    raise ValueError("Please set your session cookie")

SESSION = SESSION_FILE.read_text().strip()
if not SESSION:
    raise ValueError("Please set your session cookie")


def get_input(day: int, year: int):
    input_file = INPUTS_DIR / f"{year}_{day}.txt"
    if input_file.exists():
        return input_file.read_text()
    else:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        response = requests.get(
            url,
            cookies={"session": SESSION},
            headers={"User-Agent": "github.com/eivindjahren/simple-aoc-template"},
        )
        if not response.ok:
            raise RuntimeError(
                f"Fetching from {url} resulted in "
                f"code: {response.status_code}, "
                f"message: {response.content}."
            )
        problem_input = response.text[:-1]
        input_file.write_text(problem_input)
        return problem_input


__all__ = ["get_input"]
