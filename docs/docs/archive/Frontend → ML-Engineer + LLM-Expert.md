Kimi: 📘 Hybrid Daily Roadmap  
«Frontend → ML-Engineer + LLM-Expert»  
(24 недели = 168 дней, 1 день = 1 задача)

Формат:  
день | тема | мини-задача (не более 2 ч) | тест / чек-лист

---

### 📅 Неделя 1  «Python Core, дни 1-7»
1 | Установка pyenv + poetry | `poetry new ml-bootcamp && poetry add pytest black` | CI workflow зелёный
2 | Git flow | создать ветку `day-02-python-syntax`, MR template | MR проходит линтеры
3 | Переменные, f-строки | написать `hello.py` с f-строками, покрыть тестами | pytest OK
4 | List comprehensions | рефактор цикла в comprehension, 100 % покрытие | `pytest --cov`
5 | Функции, type hints | функция `normalize(x: np.ndarray) -> np.ndarray` | mypy без ошибок
6 | Итераторы | собственный класс `RangeIterator` + `__iter__` | тест `for _ in RangeIterator(5)`
7 | Итог недели | слить ветку в main, релиз тег `v0.1.0`



---

### 📅 Неделя 2  «Коллекции & тесты, дни 8-14»
8 | Dataclasses | `User(id:int, name:str)` + `__post_init__` | pytest-dataclass
9 | Модуль `collections` | реализовать `Counter` для подсчёта слов | unit-test
10 | Генераторы | `fibonacci()` бесконечный, проверить 10 чисел | `assert list(islice(fib(),10))`
11 | Исключения | кастомное `ValidationError`, raise + catch | 100 % покрытие
12 | Модуль `itertools` | `pairwise()` аналог, тест на 5 списках
13 | Покрытие | `pytest --cov=src --cov-report=html`
14 | Code review | создать PR, пройти 2 аппрува

---

### 📅 Неделя 3  «ООП & паттерн Repository, дни 15-21»
15 | Класс `CSVRepository` | методы save/load | mock-файл в /tmp
16 | Dependency injection | передаём `Storage` интерфейс | тест с FakeStorage
17 | Property & setter | `User.full_name` | `assert user.full_name == "John Doe"`
18 | Dataclasses + slots | performance тест через `timeit`
19 | Паттерн UoW | `UnitOfWork` контекст-менеджер | rollback тест
20 | TDD цикл | написать тест → реализовать → рефактор
21 | Итог недели | merge request + релиз `v0.2.0`

---

### 📅 Неделя 4  «CI/CD & исключения, дни 22-28»
22 | GitHub Actions | job lint + test
23 | Docker | `Dockerfile` для проекта, build & push
24 | Poetry scripts | `poetry run test`, `poetry run lint`
25 | Pre-commit hooks | black, isort, flake8
26 | Исключения | `raise from` chaining
27 | Logging | `structlog`, тест через `caplog`
28 | Спринт-ретро | написать пост в README

---

### 📅 Неделя 5  «NumPy, дни 29-35»
29 | Создать ndarray 3×3 | проверить shape, dtype
30 | Broadcasting | `A + B` где A(3,1), B(1,4) | assert shape
31 | `einsum` | матричное умножение без `@`
32 | «Жизнь» 1 | Conway 10×10 поле, шаг 1
33 | «Жизнь» 2 | анимация через `matplotlib.animation`
34 | Профилирование | `%timeit` vs Numba
35 | Итог недели | push Docker image `day-35-life`

---

### 📅 Неделя 6  «Pandas EDA, дни 36-42»
36 | Загрузить Titanic CSV | head(), info()
37 | Missing values | `fillna()`, тест на NaN=0
38 | Feature engineering | `Title` из `Name`, тест регекс
39 | Groupby | средний возраст по `Pclass`
40 | Визуализация 1 | seaborn countplot
41 | Визуализация 2 | pairplot (survived)
42 | Залить ноутбук на Kaggle Datasets

---

### 📅 Неделя 7  «Matplotlib, дни 43-49»
43 | Subplots | 2×2 grid
44 | Custom style | `mplstyle` → тест
45 | Heatmap | корреляция Titanic
46 | Violin plot | Age vs Survived
47 | Swarm plot | Fare vs Survived
48 | Export | `plt.savefig(..., dpi=300)`
49 | Спринт-ретро | обновить README

---

### 📅 Неделя 8  «scikit-learn, дни 50-56»
50 | `make_classification` | 1000×20
51 | Pipeline | StandardScaler + LogReg
52 | GridSearchCV | 3 параметра, `cv=5`
53 | RandomForest baseline | `accuracy`, `f1`
54 | SVM baseline | `roc_auc`
55 | MLflow | `mlflow ui` логи
56 | Сохранить модель | `joblib.dump`

---

### 📅 Неделя 9  «Линейные модели, дни 57-63»
57 | Синтетические 2D точки | `make_blobs`
58 | LogisticRegression | границы решения
59 | SGD momentum | сравнить loss кривые
60 | Adam vs SGD | тест на 100 эпох
61 | Визуализация | `decision_boundary_plot`
62 | Weight decay | L2 1e-4 vs 1e-2
63 | Итог недели | merge PR

---

### 📅 Неделя 10  «Tree & Optuna, дни 64-70»
64 | RandomForest | `n_estimators=200`
65 | Optuna | objective `f1`
66 | Best params | сохранить `study.best_params`
67 | GradientBoosting | сравнение ROC
68 | Feature importance | `permutation_importance`
69 | SHAP | waterfall plot
70 | MLflow artifacts | log model + params

---

### 📅 Неделя 11  «CV & metrics, дни 71-77»
71 | StratifiedKFold | 5 folds
72 | ROC-AUC | `roc_auc_score`
73 | PR-AUC | `average_precision`
74 | F_beta scorer | `make_scorer(beta=2)`
75 | Кривые | `plot_roc_curve`
76 | Отчёт | markdown таблица
77 | Push на Kaggle | House Prices submit

---

### 📅 Неделя 12  «Kaggle-зачёт, дни 78-84»
78 | EDA template | день 0
79 | Baseline model | RandomForest
80 | Feature engineering | 5 новых признаков
81 | Cross-validation | 5-fold
82 | Submit 1 | public LB
83 | Submit 2 | hyperopt
84 | Финальный сабмит | top-35 %

---

### 📅 Неделя 13  «PyTorch тензоры, дни 85-91»
85 | `torch.manual_seed(42)`
86 | `tensor` + `requires_grad`
87 | `torch.matmul` vs `@`
88 | `nn.Linear` с нуля
89 | Backward pass | градиенты вручную
90 | Unit-test | `assert torch.allclose`
91 | Сохранить модель | `state_dict`

---

### 📅 Неделя 14  «CNN, дни 92-98»
92 | CIFAR-10 загрузка | `torchvision.datasets`
93 | ResNet-18 | `torchvision.models`
94 | Fine-tune | freeze backbone
95 | 10 эпох | accuracy ≥ 60 %
96 | 20 эпох | target ≥ 90 %
97 | TensorBoard | scalars, images
98 | Сохранить чекпойнт

---

### 📅 Неделя 15  «Transfer Learning, дни 99-105»
99 | Imagenette dataset
100 | Discriminative LR | `slice(1e-5, 1e-3)`
101 | 5 эпох | accuracy ≥ 85 %
102 | 8 эпох | target ≥ 88 %
103 | Confusion matrix
104 | Error analysis | top-5 ошибок
105 | Push checkpoint HF Hub

---

### 📅 Неделя 16  «Grad-CAM, дни 106-112»
106 | Hook для последнего conv-слоя
107 | Grad-CAM реализация
108 | Streamlit app skeleton
109 | Upload image → heatmap
110 | Deploy HuggingFace Spaces
111 | Add GitHub Actions CI
112 | README demo gif

---

### 📅 Неделя 17  «FastAPI, дни 113-119»
113 | `main.py` hello-world
114 | Pydantic модель `PredictRequest`
115 | Repository pattern | `ImageRepository`
116 | Dependency injection | `storage: Storage`
117 | Unit-test | `TestClient` pytest
118 | Docker | `Dockerfile` + `docker-compose`
119 | CI/CD | GitHub Actions push

---

### 📅 Неделя 18  «Feature Store, дни 120-126»
120 | Redis install & test `ping`
121 | MinIO local S3
122 | Store embeddings | `np.savez → S3`
123 | Retrieve by key
124 | Caching layer | `cachetools`
125 | Rate limiting | `slowapi`
126 | Load test | `locust` 100 RPS

---

### 📅 Неделя 19  «MLflow + DVC, дни 127-133»
127 | `dvc init`
128 | `dvc add data/`
129 | `dvc repro train`
130 | MLflow tracking URI
131 | Log parameters & metrics
132 | Register model
133 | Git tag `v0.5.0`

---

### 📅 Неделя 20  «Тесты & CI, дни 134-140»
134 | pytest fixtures
135 | mock S3 with `moto`
136 | integration test `/predict`
137 | Coverage 90 %
138 | GitHub Actions matrix (3.9, 3.10, 3.11)
139 | Heroku deploy
140 | Badge in README

---

### 📅 Неделя 21  «Docker & K8s, дни 141-147»
141 | Multi-stage Dockerfile
142 | `docker buildx`
143 | `kubectl apply -f deploy/`
144 | Healthcheck endpoint
145 | Rolling update
146 | Liveness + readiness probes
147 | K9s dashboard

---

### 📅 Неделя 22  «Prometheus + Grafana, дни 148-154»
148 | `prometheus_client` metrics
149 | Counter `predict_total`
150 | Histogram `predict_duration`
151 | Grafana dashboard JSON
152 | Alertmanager webhook
153 | SLO 99 % latency < 200 ms
154 | Post-incident runbook

---

### 📅 Неделя 23  «A/B-тесты, дни 155-161»
155 | FastAPI middleware variant
156 | Split traffic 50/50
157 | Log variant & metric
158 | Prometheus query
159 | Jupyter notebook analysis
160 | Decision rule
161 | Switch 100 % winner

---

### 📅 Неделя 24  «Финиш, дни 162-168»
162 | Medium статья draft
163 | Lightning-talk слайды
164 | Demo-day репетиция
165 | Код-ревью коллегой
166 | Release `v1.0.0`
167 | Apply to ML jobs
168 | 🎉 Отпуск

---

### 🧪 Повседневное тестирование
- **Каждая задача** заканчивается **автоматическим тестом** или **CI-check**.
- **Coverage-бот** комментирует PR.
- **pre-commit** не даёт закоммитить «красный» код.
- **Kanban-доска** в GitHub Projects: To Do → In Progress → Tests Pass → Done.

Сохрани файл как `daily-ml-llm-roadmap.md`, отмечай ✅ вместо галочек и двигайся день за днём!
