User: Для на базе собственного локального репозитория гитлаб такое можно реализовать? В описании добавь как поднять и настроить локальный гит-лаб  репо.
Kimi: Да, **GitLab можно поднять локально** и использовать его вместо GitHub для той же схемы «UML + Kanban + CI».  
Ниже пошаговый рецепт: от установки до первого «зелёного» пайплайна.

---

### 1️⃣ Установка (Docker, 5 минут)

#### Вариант A. Docker-Compose (рекомендую)
Создайте файл `docker-compose.yml`:

```yaml
version: '3.8'
services:
  gitlab:
    image: gitlab/gitlab-ce:latest
    container_name: gitlab
    restart: always
    hostname: localhost
    ports:
      - "8080:80"    # HTTP
      - "8443:443"   # HTTPS
      - "6022:22"    # SSH для Git
    volumes:
      - ./gitlab/config:/etc/gitlab
      - ./gitlab/logs:/var/log/gitlab
      - ./gitlab/data:/var/opt/gitlab
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://localhost:8080'
        gitlab_rails['gitlab_shell_ssh_port'] = 6022
```

Запуск:

```bash
docker-compose up -d
```

#### Вариант B. Один docker-run
```bash
docker run --detach \
  --hostname localhost \
  --publish 8080:80 --publish 6022:22 \
  --name gitlab --restart always \
  --volume $PWD/gitlab/config:/etc/gitlab \
  --volume $PWD/gitlab/logs:/var/log/gitlab \
  --volume $PWD/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:latest
```

---

### 2️⃣ Первый вход

1. Откройте браузер: `http://localhost:8080`
2. **root** пароль выдаёт контейнер:
   ```bash
   docker exec -it gitlab cat /etc/gitlab/initial_root_password
   ```
3. Залогиньтесь под `root` и **сразу смените пароль**.

---

### 3️⃣ Создаём проект «LLM-Roadmap»

Projects → New Project → Create blank project →
- **Project name**: `llm-roadmap`
- **Visibility**: Private
- **Initialize repository with README**: ☑

---

### 4️⃣ Поднимаем Kanban-доску

1. Side-menu → **Issues → Boards** → «New Board» → «Basic Kanban»
2. Колонки:
    - To Learn
    - In Progress
    - Done
3. Добавляем **12 issues** по шаблону:

| Title | Description |
|---|---|
| Q1_Sprint1 | [checklist] bird classifier CNN |
| Q1_Sprint2 | [checklist] sentiment-analysis pipeline |
| … | … |

---

### 5️⃣ Загружаем UML-файл и настраиваем CI

#### 5.1  Загрузите файлы в репозиторий
```
llm-roadmap/
├── llm-roadmap.puml
├── .gitlab-ci.yml
├── docs/
│   └── roadmap.png
```

#### 5.2  `.gitlab-ci.yml` — перерисовка UML при каждом push
```yaml
stages: [build]

plantuml:
  stage: build
  image: plantuml/plantuml-server:jetty
  script:
    - plantuml -tpng llm-roadmap.puml -o docs
  artifacts:
    paths:
      - docs/roadmap.png
    expire_in: 1 week
```

#### 5.3  Добавьте **GitLab Runner** (если ещё нет)
```bash
docker run -d --name gitlab-runner \
  --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

В GitLab → Settings → CI/CD → Runners → copy **token** и:

```bash
docker exec -it gitlab-runner gitlab-runner register
# URL http://localhost:8080
# token <token>
# executor docker
# image alpine:latest
```

---

### 6️⃣ Пример рабочего процесса

1. **Developer** делает `git clone ssh://git@localhost:6022/root/llm-roadmap.git`
2. Открывает `llm-roadmap.puml`, **ставит галочку**:
   ```plantuml
   class "Q1_Sprint1 ✅" <<done>> #C8E6C9
   ```
3. `git add . && git commit -m "Q1_Sprint1 done" && git push`
4. **GitLab CI** собирает новый PNG и кладёт его в artifacts.
5. **Board** автоматически переносит issue в Done.

---

### 7️⃣ Дополнительно (по желанию)

- **Container Registry** уже включён:  
  `docker login localhost:8080` → можно пушить собственные образы моделей.
- **LDAP / локальные пользователи** настраиваются через Admin → Settings.
- **HTTPS** — добавьте самоподписанный сертификат или LetsEncrypt.

---

### Шпаргалка команд

| Действие | Команда |
|---|---|
| Перезапустить GitLab | `docker-compose restart gitlab` |
| Смотреть логи | `docker logs -f gitlab` |
| Обновить GitLab | `docker-compose pull && docker-compose up -d` |
| Сбросить root-пароль | `docker exec -it gitlab gitlab-rake "gitlab:password:reset[root]"` |

После этих шагов у вас поднят **полностью локальный GitLab** с Kanban-досками, CI/CD и UML-перерисовкой, который можно использовать как единую точку управления 1–2-летним планом обучения без внешнего интернета.
