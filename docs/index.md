# Welcome to Python Boilerplate's documentation!

## Repository structure

```ml-bootcamp/
├── 01-python-core/
├── 02-ds-libraries/
├── 03-ml-practice/
├── 04-deep-dive/
├── 05-cv-service/
│   ├── api/
│   ├── models/
│   ├── tests/
│   └── Dockerfile
├── 06-mlops/
└── README.md
```

## Contents

* [Readme](../README.MD)
* [Installation](installation.md)
* [Usage](usage.md)
* [Modules](modules.md)
* [Contributing](contributing.md)
* [History](history.md)

## Indices and tables

- [Index](genindex)
- [Module Index](modindex)
- [Search](search)


## Примерный План обучения

| Спринт  | Тема + ресурс                                                                                                      | Что изучаем                               | Что умеем                      | Практические задания                          | Как тестируем                              |
|---------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------|--------------------------------|-----------------------------------------------|--------------------------------------------|
| **P0**  | **Python за 3 дня**<br>[fast.ai «Python for Programmers»](https://course.fast.ai/Lessons/python.html)              | синтаксис, list-comprehensions, f-strings | запускаем скрипт без ошибок    | 1) `data_loader.py` читает CSV → JSON         | `pytest data_loader_test.py`               |
| **P1**  | **PyTorch + GPU**<br>[PyTorch 60-min blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) | тензоры, `.to(device)`, `DataLoader`      | обучаем линейную модель на GPU | 2) линейная регрессия на синтетике            | `assert torch.allclose(loss, expected)`    |
| **P2**  | **Jupyter & Poetry**<br>[Poetry docs](https://python-poetry.org/docs/)                                             | виртуальные окружения, `pyproject.toml`   | воспроизводимое окружение      | 3) проект `llm-sprint` через Poetry + Jupyter | `poetry run pytest`                        |
| **2.1** | **HF Datasets & Tokenizers**<br>[HF Course ch. 2.5–2.7](https://huggingface.co/learn/nlp-course/ru/chapter2)       | map, filter, streaming                    | грузим 1 Гб датасет без ОЗУ    | 4) `Dataset` из папки .txt → Hub              | `dataset.push_to_hub(...)`                 |
| **2.2** | **Векторные базы**<br>[LangChain RAG tutorial](https://python.langchain.com/docs/use_cases/question_answering/)    | Chroma / FAISS                            | строим индекс                  | 5) 100 PDF → вектор-стор → RetrievalQA        | `assert retriever.get_relevant_docs("AI")` |
| **2.3** | **Production-ready токенизатор**<br>[HF Tokenizers course](https://huggingface.co/learn/nlp-course/ru/chapter6)    | BPE, WordPiece                            | обучаем токенизатор            | 6) BPE на русских чатах → Hub                 | `tokenizer.save_pretrained(...)`           |
| **3.1** | **LoRA & PEFT**<br>[HF Fine-tuning ch. 3](https://huggingface.co/learn/nlp-course/ru/chapter3)                     | Trainer API, LoRA                         | 1 GPU, 3 эпохи                 | 7) ruGPT-3.5 fine-tune на 5k FAQ              | `evaluate() >= baseline + 5 %`             |
| **3.2** | **Квантизация**<br>bitsandbytes + GGUF                                                                             | INT4/8, GPTQ                              | модель в 6 Гб VRAM             | 8) fp16 vs int4 BLEU/ROUGE                    | `assert int4_bleu >= 0.9 * fp16_bleu`      |
| **3.3** | **Flash-Attn + DeepSpeed**<br>официальные туториалы                                                                | memory-efficient attention                | 32k контекст                   | 9) добавить Flash-Attn в Trainer              | `pytest test_flash_attn.py`                |
| **4.1** | **Ollama & REST**<br>ollama.ai docs                                                                                | REST / OpenAI-совместимый API             | localhost:11434                | 10) `curl`-тесты + pytest `httpx`             | `assert response.status_code == 200`       |
| **4.2** | **MCP-протокол**<br>[modelcontextprotocol](https://github.com/modelcontextprotocol)                                | JSON-RPC вызовы                           | MCP-хендлер                    | 11) MCP-сервер для эмбеддингов                | `pytest test_mcp_handler.py`               |
| **4.3** | **Docker + CI/CD**<br>fast.ai lesson 7                                                                             | Dockerfile, GitHub Actions                | одна команда деплой            | 12) push контейнера в GHCR                    | `docker run --rm image pytest`             |


<details>
    <summary> План подробнее</summary>

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║        📅 Hybrid Daily Roadmap «Frontend → ML-Engineer + LLM-Expert»  (24 недели = 168 дней)                             ║
╠════╦═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ День ║ Задача (2 ч)                                                                                                  ║
║      ║                                                                                                               ║
╠════==╬═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║  1   │ Установка pyenv + poetry → `poetry new ml-bootcamp && poetry add pytest black`                               ║
║  2   │ Git-flow: ветка `day-02-python-syntax`, MR template, CI workflow зелёный                                    ║
║  3   │ Переменные, f-strings → `hello.py` с тестами pytest                                                           ║
║  4   │ List-comprehension → рефактор цикла, 100 % покрытие pytest-cov                                                ║
║  5   │ Функции + type hints → `normalize(x: np.ndarray) -> np.ndarray`, mypy без ошибок                              ║
║  6   │ Собственный итератор `RangeIterator`, тест `for _ in RangeIterator(5)`                                       ║
║  7   │ Итог недели → merge в main, тег `v0.1.0`                                                                      ║
║  8   │ Dataclass `User(id:int,name:str)`, pytest-dataclass                                                           ║
║  9   │ Модуль `collections.Counter` для подсчёта слов, unit-test                                                     ║
║ 10   │ Бесконечный генератор `fibonacci()`, тест `list(islice(fib(),10))`                                            ║
║ 11   │ Кастомное `ValidationError`, raise/catch, 100 % покрытие                                                      ║
║ 12   │ itertools `pairwise()` аналог, тест на 5 списках                                                              ║
║ 13   │ Покрытие `pytest --cov=src --cov-report=html`                                                                 ║
║ 14   │ Code-review: 2 аппрува, merge PR                                                                              ║
║ 15   │ Класс `CSVRepository(save/load)`, mock-файл в /tmp                                                            ║
║ 16   │ Dependency Injection: интерфейс `Storage`, тест `FakeStorage`                                                 ║
║ 17   │ Property `User.full_name`, assert `== "John Doe"`                                                             ║
║ 18   │ Dataclasses + slots, бенчмарк `timeit`                                                                        ║
║ 19   │ UnitOfWork (UoW) контекст-менеджер, rollback тест                                                             ║
║ 20   │ TDD цикл: тест → реализация → рефактор                                                                        ║
║ 21   │ Merge PR + релиз `v0.2.0`                                                                                     ║
║ 22   │ GitHub Actions job lint + test                                                                                ║
║ 23   │ Dockerfile, `docker buildx`, push                                                                             ║
║ 24   │ Poetry скрипты `poetry run test`, `poetry run lint`                                                           ║
║ 25   │ Pre-commit hooks black, isort, flake8                                                                         ║
║ 26   │ Исключения `raise from` chaining                                                                              ║
║ 27   │ Logging `structlog`, тест через `caplog`                                                                      ║
║ 28   │ Спринт-ретро: пост в README                                                                                   ║
║ 29   │ NumPy ndarray 3×3, проверка shape/dtype                                                                       ║
║ 30   │ Broadcasting `A(3,1)+B(1,4)`, assert shape                                                                    ║
║ 31   │ `einsum` матричное умножение без `@`                                                                          ║
║ 32   │ «Жизнь» Conway 10×10, 1 шаг                                                                                   ║
║ 33   │ Анимация «Жизнь» через `matplotlib.animation`                                                                 ║
║ 34   │ Профилирование `%timeit` vs Numba                                                                             ║
║ 35   │ Docker image `day-35-life` push                                                                               ║
║ 36   │ Titanic CSV → `df.head()`, `df.info()`                                                                        ║
║ 37   │ Missing values `fillna`, тест NaN=0                                                                           ║
║ 38   │ Feature engineering `Title` из `Name`, regex тест                                                             ║
║ 39   │ Groupby средний возраст по `Pclass`                                                                           ║
║ 40   │ Seaborn countplot                                                                                             ║
║ 41   │ Pairplot (survived)                                                                                           ║
║ 42   │ Ноутбук Titanic_EDA.ipynb → Kaggle Datasets                                                                   ║
║ 43   │ Matplotlib 2×2 subplots                                                                                       ║
║ 44   │ Custom `mplstyle` + тест                                                                                      ║
║ 45   │ Heatmap корреляция Titanic                                                                                    ║
║ 46   │ Violin plot Age vs Survived                                                                                   ║
║ 47   │ Swarm plot Fare vs Survived                                                                                   ║
║ 48   │ `plt.savefig(..., dpi=300)`                                                                                   ║
║ 49   │ README обновить                                                                                               ║
║ 50   │ `make_classification(1000×20)`                                                                                ║
║ 51   │ Pipeline `StandardScaler + LogReg`                                                                            ║
║ 52   │ GridSearchCV 3 params, cv=5                                                                                   ║
║ 53   │ RandomForest baseline accuracy/f1                                                                             ║
║ 54   │ SVM baseline roc_auc                                                                                          ║
║ 55   │ MLflow `mlflow ui` логи                                                                                       ║
║ 56   │ `joblib.dump` модель                                                                                          ║
║ 57   │ Синтетические 2D точки `make_blobs`                                                                             ║
║ 58   │ LogisticRegression границы решения                                                                            ║
║ 59   │ SGD momentum loss кривые                                                                                      ║
║ 60   │ Adam vs SGD 100 эпох                                                                                          ║
║ 61   │ `decision_boundary_plot`                                                                                      ║
║ 62   │ Weight decay L2 1e-4 vs 1e-2                                                                                  ║
║ 63   │ Merge PR                                                                                                      ║
║ 64   │ RandomForest `n_estimators=200`                                                                               ║
║ 65   │ Optuna objective `f1`                                                                                         ║
║ 66   │ `study.best_params` сохранить                                                                                 ║
║ 67   │ GradientBoosting ROC сравнение                                                                                ║
║ 68   │ `permutation_importance`                                                                                      ║
║ 69   │ SHAP waterfall plot                                                                                           ║
║ 70   │ MLflow artifacts log                                                                                          ║
║ 71   │ StratifiedKFold 5 folds                                                                                       ║
║ 72   │ ROC-AUC `roc_auc_score`                                                                                       ║
║ 73   │ PR-AUC `average_precision`                                                                                    ║
║ 74   │ F_beta scorer `make_scorer(beta=2)`                                                                           ║
║ 75   │ `plot_roc_curve`                                                                                              ║
║ 76   │ Markdown отчёт                                                                                                ║
║ 77   │ Kaggle House Prices submit                                                                                    ║
║ 78   │ EDA template day 0                                                                                            ║
║ 79   │ Baseline RandomForest                                                                                         ║
║ 80   │ Feature engineering 5 новых признаков                                                                         ║
║ 81   │ Cross-validation 5-fold                                                                                       ║
║ 82   │ Submit 1 public LB                                                                                            ║
║ 83   │ Hyperopt submit 2                                                                                             ║
║ 84   │ Final submit top-35 %                                                                                         ║
║ 85   │ `torch.manual_seed(42)`                                                                                       ║
║ 86   │ `tensor.requires_grad=True`                                                                                   ║
║ 87   │ `torch.matmul` vs `@`                                                                                         ║
║ 88   │ Написать `nn.Linear` с нуля                                                                                   ║
║ 89   │ Backward pass градиенты вручную                                                                               ║
║ 90   │ Unit-test `torch.allclose`                                                                                    ║
║ 91   │ `state_dict` сохранить                                                                                        ║
║ 92   │ CIFAR-10 `torchvision.datasets`                                                                               ║
║ 93   │ ResNet-18 `torchvision.models`                                                                                ║
║ 94   │ Fine-tune freeze backbone                                                                                     ║
║ 95   │ 10 эпох accuracy ≥ 60 %                                                                                       ║
║ 96   │ 20 эпох target ≥ 90 %                                                                                         ║
║ 97   │ TensorBoard scalars & images                                                                                  ║
║ 98   │ Checkpoint сохранить                                                                                          ║
║ 99   │ Imagenette dataset                                                                                            ║
║100   │ Discriminative LR slice(1e-5,1e-3)                                                                            ║
║101   │ 5 эпох accuracy ≥ 85 %                                                                                        ║
║102   │ 8 эпох target ≥ 88 %                                                                                          ║
║103   │ Confusion matrix                                                                                              ║
║104   │ Error analysis top-5                                                                                          ║
║105   │ Push checkpoint HF Hub                                                                                        ║
║106   │ Hook последнего conv-слоя                                                                                     ║
║107   │ Grad-CAM реализация                                                                                           ║
║108   │ Streamlit app skeleton                                                                                        ║
║109   │ Upload image → heatmap                                                                                        ║
║110   │ Deploy HuggingFace Spaces                                                                                     ║
║111   │ GitHub Actions CI                                                                                             ║
║112   │ README demo GIF                                                                                               ║
║113   │ FastAPI `main.py` hello-world                                                                                 ║
║114   │ Pydantic `PredictRequest`                                                                                     ║
║115   │ Repository pattern `ImageRepository`                                                                          ║
║116   │ DI `storage: Storage`                                                                                         ║
║117   │ Unit-test `TestClient` pytest                                                                                 ║
║118   │ Dockerfile + docker-compose                                                                                   ║
║119   │ GitHub Actions push                                                                                           ║
║120   │ Redis install & ping                                                                                          ║
║121   │ MinIO локальный S3                                                                                            ║
║122   │ Store embeddings np.savez → S3                                                                                ║
║123   │ Retrieve by key                                                                                               ║
║124   │ Caching cachetools                                                                                            ║
║125   │ Rate limiting slowapi                                                                                         ║
║126   │ Load test locust 100 RPS                                                                                      ║
║127   │ dvc init                                                                                                      ║
║128   │ dvc add data/                                                                                                 ║
║129   │ dvc repro train                                                                                               ║
║130   │ MLflow tracking URI                                                                                           ║
║131   │ Log params & metrics                                                                                          ║
║132   │ Register model                                                                                                ║
║133   │ Git tag v0.5.0                                                                                                ║
║134   │ pytest fixtures                                                                                               ║
║135   │ mock S3 moto                                                                                                  ║
║136   │ Integration test /predict                                                                                     ║
║137   │ Coverage 90 %                                                                                                 ║
║138   │ GitHub Actions matrix 3.9-3.11                                                                                ║
║139   │ Heroku deploy                                                                                                 ║
║140   │ Badge in README                                                                                               ║
║141   │ Multi-stage Dockerfile                                                                                        ║
║142   │ docker buildx                                                                                                 ║
║143   │ kubectl apply -f deploy/                                                                                      ║
║144   │ Healthcheck endpoint                                                                                          ║
║145   │ Rolling update                                                                                                ║
║146   │ Liveness & readiness probes                                                                                   ║
║147   │ K9s dashboard                                                                                                 ║
║148   │ prometheus_client Counter                                                                                     ║
║149   │ Counter predict_total                                                                                         ║
║150   │ Histogram predict_duration                                                                                    ║
║151   │ Grafana dashboard JSON                                                                                        ║
║152   │ Alertmanager webhook                                                                                          ║
║153   │ SLO 99 % latency < 200 ms                                                                                     ║
║154   │ Post-incident runbook                                                                                         ║
║155   │ FastAPI middleware variant                                                                                    ║
║156   │ Split traffic 50/50                                                                                           ║
║157   │ Log variant & metric                                                                                          ║
║158   │ Prometheus query                                                                                              ║
║159   │ Jupyter analysis                                                                                              ║
║160   │ Decision rule                                                                                                 ║
║161   │ Switch 100 % winner                                                                                           ║
║162   │ Medium draft статья                                                                                           ║
║163   │ Lightning-talk слайды                                                                                         ║
║164   │ Demo-day репетиция                                                                                            ║
║165   │ Code-review коллегой                                                                                          ║
║166   │ Release v1.0.0                                                                                                ║
║167   │ Apply to ML jobs                                                                                              ║
║168   │ 🎉 Отпуск                                                                                                     ║
╚════╩═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```
</details>
