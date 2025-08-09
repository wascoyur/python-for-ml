User: расскажи подробнее про cookiecutter. Я не понимаю как он работает, какие шаблоны откуда берутся и как шаблоны выбирать
Kimi: 📚 **Cookiecutter за 5 минут: что это, откуда берутся шаблоны и как выбрать**

---

### 1. Что такое Cookiecutter
Cookiecutter — это **CLI-утилита** на Python, которая из «папки-шаблона» (*cookiecutter*) генерирует новый проект.  
Шаблон = обычная папка + файл `cookiecutter.json` с переменными в `{{ }}`.  
При генерации утилита спрашивает значения и заменяет переменные, создавая готовый проект.

---

### 2. Откуда берутся шаблоны

| Источник | Пример URL | Комментарий |
|---|---|---|
| **GitHub** | `https://github.com/audreyr/cookiecutter-pypackage.git` | самый популярный репозиторий |
| **GitLab / Bitbucket** | `https://gitlab.com/user/template.git` | любой git-URL |
| **Локальная папка** | `file:///home/user/my-template` | удобно для своих |
| **ZIP-архив** | `https://example.com/template.zip` | не требует git |

Каталог популярных шаблонов:  
https://github.com/topics/cookiecutter-template

---

### 3. Как выбрать и использовать шаблон (пошагово)

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

---

### 4. Как создать свой шаблон (когда захотите)

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

---

### 5. Что будет внутри готового проекта (как в Vite)

| В JS (Vite) | В Cookiecutter (например, `cookiecutter-data-science`) |
|---|---|
| `package.json` → `pyproject.toml` (Poetry) |
| ESLint/Prettier → `black`, `ruff`, `mypy` |
| `.env` → `.env.example` + `pydantic-settings` |
| `vite.config.js` → `Dockerfile`, `docker-compose.yml` |
| Hot-reload → `uvicorn --reload` или `pytest-watch` |

---

### TL;DR
- **Cookiecutter** = генератор проектов, как `create-vite`.
- Шаблоны берутся из GitHub/GitLab/локальной папки/ZIP.
- Один раз установил → выбираешь шаблон → отвечаешь на вопросы → получаешь готовый проект с линтерами, тестами и CI.
