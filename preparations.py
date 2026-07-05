import subprocess
from pathlib import Path

# 1. Определяем shell корректно
shell = subprocess.check_output("echo $SHELL", shell=True).decode().strip()

# 2. Клонируем репозиторий
subprocess.run([
    "git", "clone",
    "https://github.com/MrQwerty13/TaskTrackerPyVersion.git"
])

project_dir = Path("TaskTrackerPyVersion")

# 3. Создаём venv
subprocess.run(["python3", "-m", "venv", str(project_dir / ".venv")])

# 4. Установка зависимостей (ВАЖНО: используем pip внутри venv)
pip_path = project_dir / ".venv" / "bin" / "pip"

subprocess.run([str(pip_path), "install", "-r", str(project_dir / "requirements.txt")])

# 5. Работа с rc файлами
rc_file = Path.home() / (".zshrc" if "zsh" in shell else ".bashrc")

ai_text = Path("ai.txt").read_text()
tasks_text = Path("tasks.txt").read_text()

with open(rc_file, "a") as f:
    f.write("\n# AI config\n")
    f.write(ai_text + "\n")
    f.write(tasks_text + "\n")