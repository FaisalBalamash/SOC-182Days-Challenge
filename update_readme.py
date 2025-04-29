import os
from datetime import datetime

# === CONFIGURATION ===
REPO_CREATION_DATE = datetime(2025, 4, 25)  # Set your repository creation date
README_PATH = "README.md"
TARGET_EXTENSIONS = ['.pdf']

# === FUNCTIONS ===

def count_challenges(directory="."):
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                count += 1
    return count

def calculate_days_passed(start_date):
    today = datetime.utcnow()  # UTC to match GitHub Actions
    return (today - start_date).days + 1

def update_readme(readme_path, solved, day):
    with open(readme_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("## ") and "Solved" in line:
            new_lines.append(f"## {solved} / 191 Solved\n")
        elif line.startswith("## Day") and "/" in line:
            new_lines.append(f"## Day {day}/220\n")
        else:
            new_lines.append(line)

    with open(readme_path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)

# === MAIN ===

if __name__ == "__main__":
    solved_challenges = count_challenges()
    days_passed = calculate_days_passed(REPO_CREATION_DATE)
    update_readme(README_PATH, solved_challenges, days_passed)
    print(f"Updated README.md -> {solved_challenges} challenges solved, Day {days_passed}/220")
