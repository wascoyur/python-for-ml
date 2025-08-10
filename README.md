Kimi: 📦 1-минутный старт «Python-школа как Vite»  
(с нуля до рабочего проекта)

---

# 1. Установка инструментов (один раз)


### 2.1. Ставим pipx (если ещё нет)
```bash

python -m pip install --user pipx
```

```bash
 
 pipx ensurepath && exec $SHELL   # перезагружаем shell
````

### 2.2 Ставим Cookiecutter + Poetry
  ```bash
   
  pipx install cookiecutter
  ```
  ```bash
   
  pipx install poetry
  ````


**Cookiecutter за 5 минут: что это, откуда берутся шаблоны и как выбрать**

---

<details>
<summary>2.2.1. Что такое Cookiecutter</summary>

Cookiecutter — это **CLI-утилита** на Python, которая из «папки-шаблона» (*cookiecutter*) генерирует новый проект. Шаблон = обычная папка + файл `cookiecutter.json` с переменными в `{{ }}`. При генерации утилита спрашивает значения и заменяет переменные, создавая готовый проект.

</details>

---

<details>
<summary>2.2.2. Откуда берутся шаблоны</summary>

| Источник               | Пример URL                                              | Комментарий                  |
|------------------------|---------------------------------------------------------|------------------------------|
| **GitHub**             | `https://github.com/audreyr/cookiecutter-pypackage.git` | самый популярный репозиторий |
| **GitLab / Bitbucket** | `https://gitlab.com/user/template.git`                  | любой git-URL                |
| **Локальная папка**    | `file:///home/user/my-template`                         | удобно для своих             |
| **ZIP-архив**          | `https://example.com/template.zip`                      | не требует git               |

Каталог популярных шаблонов:  
https://github.com/topics/cookiecutter-template

</details>

---

<details>
<summary>2.2.3. Как выбрать и использовать шаблон (пошагово)</summary>

#### ① Установите cookiecutter
```bash
pipx install cookiecutter   # через pipx (рекомендуется)
```

#### ② Просмотрите шаблоны
```bash
# Список популярных
cookiecutter gh:audreyr/cookiecutter-pypackage   # Python-пакет
cookiecutter gh:drivendataorg/cookiecutter-data-science  # DS/ML
cookiecutter gh:pawamoy/copier-poetry            # Poetry + MkDocs
```

#### ③ Генерируем проект
```bash
cookiecutter https://github.com/drivendataorg/cookiecutter-data-science  
```
CLI задаёт вопросы (пример):
```
project_name [My Project]: ml-bootcamp
repo_name [ml-bootcamp]:
Select python_version:
1 - 3.11
2 - 3.10
...
```
После ответов получаем готовую папку `ml-bootcamp/`.

#### ④ Проверяем
```bash
cd ml-bootcamp
poetry install        # установит black, pytest, pre-commit…
pre-commit install    # хуки перед коммитом
pytest                # тесты зелёные
```

</details>

---

<details>
<summary>2.2.4. Как создать свой шаблон (когда захотите)</summary>

1. Создайте папку `my_template/`.
2. Внутри:
   ```
   my_template/
   ├── {{cookiecutter.repo_name}}/
   │   └── src/{{cookiecutter.project_slug}}.py
   └── cookiecutter.json
   ```
3. `cookiecutter.json`:
   ```json
   {
     "repo_name": "awesome",
     "project_slug": "{{ cookiecutter.repo_name|slugify }}"
   }
   ```
4. Используете:
   ```bash
   cookiecutter my_template/
   ```

</details>

---

<details>
<summary>2.2.5. Что будет внутри готового проекта (как в Vite)</summary>

| В JS (Vite)        | В Cookiecutter (например, `cookiecutter-data-science`) |
|--------------------|--------------------------------------------------------|
| `package.json` →   | `pyproject.toml` (Poetry)                              |
| ESLint/Prettier →  | `black`, `ruff`, `mypy`                                |
| `.env` →           | `.env.example` + `pydantic-settings`                   |
| `vite.config.js` → | `Dockerfile`, `docker-compose.yml`                     |
| Hot-reload →       | `uvicorn --reload` или `pytest-watch`                  |

</details>

---

<details>
<summary>2.2.6 TL;DR</summary>
- **Cookiecutter** = генератор проектов, как `create-vite`.
- Шаблоны берутся из GitHub/GitLab/локальной папки/ZIP.
- Один раз установил → выбираешь шаблон →, отвечаешь на вопросы → получаешь готовый проект с линтерами, тестами и CI.

</details>

### 3. Проверяем инструменты
<details>
<summary>2.3. Проверяем версии инструментов</summary>

```bash
cookiecutter --version   # ≥ 2.6
poetry --version         # ≥ 1.8
```
</details>

---

# 2. Создаём учебный проект, если еще не установлен (аналог `npm create vite@latest`)

<details>
<summary>Создаем проект с выбранным шаблоном (здесь - чистый Пайтон)</summary>

```bash

cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git
 #  --directory python   # если нужен именно чистый Python
```
</details>

---

<details>
<summary>③ Устанавливаем зависимости и активируем</summary>

```bash      
    
cd {project-name}
poetry install                    # ставит black, ruff, pytest…
poetry shell                      # виртуальное окружение активировано
pre-commit install                # линтеры перед каждым коммитом
```
</details>

---

<details>
<summary>④ Workflow «день за днём»</summary>

| Шаг            | Команда / действие                    | Что происходит             |
|----------------|---------------------------------------|----------------------------|
| **Start day**  | `poetry shell`                        | сразу в нужном venv        |
| **Новая тема** | `git checkout -b day-05-functions`    | ветка под задачу           |
| **Кодим**      | `src/day05.py`, `tests/test_day05.py` | TDD: тест → код → рефактор |
| **Линтеры**    | `pre-commit run --all-files`          | black, ruff, mypy – зелёно |
| **Тесты**      | `pytest`                              | 90 % покрытие              |
| **Git push**   | `git push origin day-05-functions`    | CI прогоняется автоматом   |
| **Вечером**    | `jupyter lab` внутри `poetry shell`   | ноутбуки без конфликтов    |

</details>

---

<details>
### 


<summary>⑤ Полезные алиасы (добавьте в `~/.bashrc`) Раскрыть алиасы</summary>

```bash
alias py="poetry env activate"
alias lint="pre-commit run --all-files"
alias test="pytest -q"
alias nb="poetry run jupyter lab"
```

</details>


---

<details>
<summary>⑥ Синхронизация с книгами</summary>

- **Каждый спринт** = новая ветка `week-1-syntax`, `week-2-collections`…
- **Файлы кода** кладём в `src/`, **ноутбуки** – в `notebooks/`.
- **Тесты** – в `tests/` (по примеру из «Паттерны разработки на Python» гл. 5).

</details>

---

Дальше просто повторяем «создать ветку → код → тест → merge» – как привыкли в React-проектах.


## 📁 4. Куда класть материалы из 6 книг

| Ресурс                            | Куда                                  | Пример файла                      |
|-----------------------------------|---------------------------------------|-----------------------------------|
| «Python на примерах»              | `src/basics.py`                       | `def leap_year(year)`             |
| «Изучаем Python»                  | `src/collections.py`                  | `class MyList`                    |
| «Паттерны разработки»             | `src/repository.py`                   | `class CSVRepository`             |
| «fastai»                          | `notebooks/01_fastai_intro.ipynb`     | `from fastai.vision.all import *` |
| «Программирование для нормальных» | `notebooks/02_numpy_matplotlib.ipynb` | `import numpy as np`              |
| «Начинаем программировать»        | `tests/test_basics.py`                | `def test_leap_year()`            |

---
