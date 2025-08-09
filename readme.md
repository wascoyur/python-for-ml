Kimi: 📦 1-минутный старт «Python-школа как Vite»  
(с нуля до рабочего проекта)

---

### ① Установка инструментов (один раз)


# 1. Ставим pipx (если ещё нет)
```bash

python -m pip install --user pipx
```

```bash
 
 pipx ensurepath && exec $SHELL   # перезагружаем shell
````

# 2. Cookiecutter + Poetry
```bash
 
pipx install cookiecutter
```
```bash
 
pipx install poetry
````

# 3. Проверяем
```bash
 
cookiecutter --version   # ≥ 2.6
poetry --version         # ≥ 1.8
```

---

### ② Создаём учебный проект (аналог `npm create vite@latest`)

```bash

pipx install cookiecutter-data-science
 #  --directory python   # если нужен именно чистый Python
 ````

```bash
  
ccds
#стартуем новый проект

# Отвечаем на 4 вопроса:
# project_name: ml-bootcamp
# repo_name: ml-bootcamp
# author_name: Your Name
# python_version: 3.11
```

Получаем структуру:

```
ml-bootcamp/
├── src/                 ← ваш код
├── tests/               ← pytest-тесты
├── notebooks/           ← Jupyter-ноутбуки
├── pyproject.toml       ← Poetry + линтеры
├── .pre-commit-config.yaml
├── Dockerfile
├── .github/workflows/   ← CI
└── README.md
```

---

### ③ Устанавливаем зависимости и активируем

```bash
cd ml-bootcamp
poetry install                    # ставит black, ruff, pytest…
poetry shell                      # виртуальное окружение активировано
pre-commit install                # линтеры перед каждым коммитом
```

---

### ④ Workflow «день за днём»

| Шаг | Команда / действие | Что происходит |
|---|---|---|
| **Start day** | `poetry shell` | сразу в нужном venv |
| **Новая тема** | `git checkout -b day-05-functions` | ветка под задачу |
| **Кодим** | `src/day05.py`, `tests/test_day05.py` | TDD: тест → код → рефактор |
| **Линтеры** | `pre-commit run --all-files` | black, ruff, mypy – зелёно |
| **Тесты** | `pytest` | 90 % покрытие |
| **Git push** | `git push origin day-05-functions` | CI прогоняется автоматом |
| **Вечером** | `jupyter lab` внутри `poetry shell` | ноутбуки без конфликтов |

---

### ⑤ Полезные алиасы (добавьте в `~/.bashrc`)

```bash
alias py="poetry shell"
alias lint="pre-commit run --all-files"
alias test="pytest -q"
alias nb="poetry run jupyter lab"
```

---

### ⑥ Синхронизация с книгами

- **Каждый спринт** = новая ветка `week-1-syntax`, `week-2-collections`…
- **Файлы кода** кладём в `src/`, **ноутбуки** – в `notebooks/`.
- **Тесты** – в `tests/` (по примеру из «Паттерны разработки на Python» гл. 5).

---

### 🏁 Через 5 минут вы уже:
- создали структуру проекта,
- активировали виртуальное окружение,
- запустили `pytest --cov` и `jupyter lab`.

Дальше просто повторяем «создать ветку → код → тест → merge» – как привыкли в React-проектах.
