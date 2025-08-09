Kimi: Системный 1–2-летний план «LLM-инженер»  
(каждый квартал = 1 большой блок; внутри — 2–3 спринта по 2–3 недели).  
Все ссылки уже есть в ваших материалах или взяты из открытых источников Hugging Face, fast.ai и др.

------------------------------------------------  
Q1  «Базовый каркас» (мес 1–3)  
Цель: закрыть столпы ①, ②, ④, ⑥ на минимальном уровне (запустить и поиграться).

| Спринт | Тема                                                                                                                              | Цель                                      | Практика                                                    |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------- |
| **P0** | **Python за 3 дня**<br>[fast.ai «Python for Programmers»](https://course.fast.ai/Lessons/python.html)                             | синтаксис, list-comprehensions, f-strings | написать `data_loader.py`, который читает CSV и выдаёт JSON |
| **P1** | **PyTorch + GPU**<br>[Hugging Face «PyTorch 60 min blitz»](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) | тензоры, `.to(device)`, `DataLoader`      | обучить линейную регрессию на GPU                           |
| **P2** | **Jupyter & Poetry**<br>[Poetry docs](https://python-poetry.org/docs/)                                                            | виртуальные окружения, `pyproject.toml`   | завести проект `llm-sprint` через Poetry + Jupyter-Lab      |


------------------------------------------------  
Q2 «Токенизация, датасеты, векторные базы» (мес 4–6)  
Цель: закрыть столп ⑦ и научиться готовить данные.

| Спринт | Тема + ресурс | Что изучаем | Что умеем | Практические задания |
|---|---|---|---|---|
| 2.1 | **HF Datasets & Tokenizers**<br>[HF Course ch. 2.5–2.7](https://huggingface.co/learn/nlp-course/ru/chapter2) | map, filter, streaming | Грузим 1 Гб датасет без ОЗУ | 4) Сделать свой `Dataset` из папки .txt и выгрузить в Hub |
| 2.2 | **Векторные базы**<br>LangChain RAG tutorial<br>[официальный гайд](https://python.langchain.com/docs/use_cases/question_answering/) | Chroma / FAISS | Строим индекс | 5) Загрузить 100 PDF → вектор-стор → RetrievalQA |
| 2.3 | **Production-ready токенизатор**<br>HF Tokenizers course<br>[раздел](https://huggingface.co/learn/nlp-course/ru/chapter6) | BPE, WordPiece | Обучаем собственный токенизатор | 6) Обучить BPE на корпусе русских чатов, сохранить в Hub |

------------------------------------------------  
Q3 «Fine-tuning & оптимизация» (мес 7–9)  
Цель: столп ⑤ – LoRA, quant, Flash-Attention.

| Спринт | Тема + ресурс | Что изучаем | Что умеем | Практические задания |
|---|---|---|---|---|
| 3.1 | **LoRA & PEFT**<br>[HF Fine-tuning ch. 3](https://huggingface.co/learn/nlp-course/ru/chapter3) | Trainer API, LoRA | 1 GPU, 3 эпохи | 7) Дообучить ruGPT-3.5 на 5k примерах FAQ |
| 3.2 | **Квантизация**<br>bitsandbytes + GGUF | INT4, INT8, GPTQ | 7B модель укладывается в 6 Гб VRAM | 8) Сравнить BLEU/ROUGE модели fp16 vs int4 |
| 3.3 | **Flash-Attn + DeepSpeed**<br>официальные туториалы | memory-efficient attention | Пропускаем 32k контекст | 9) Добавить Flash-Attn в свой Trainer |

------------------------------------------------  
Q4 «MCP-сервер & деплой» (мес 10–12)  
Цель: столп ③ – запуск модели как сервис.

| Спринт | Тема + ресурс | Что изучаем | Что умеем | Практические задания |
|---|---|---|---|---|
| 4.1 | **Ollama & REST**<br>ollama.ai docs | REST / OpenAI-совместимый API | Запускаем модель по `localhost:11434` | 10) Скрипт `curl`-тестов + юнит-тесты |
| 4.2 | **MCP-протокол**<br>официальный репо [modelcontextprotocol](https://github.com/modelcontextprotocol) | JSON-RPC вызовы | Пишем свой MCP-хендлер | 11) MCP-сервер, который отдает эмбеддинги |
| 4.3 | **Docker + CI/CD**<br>fast.ai lesson 7 | Dockerfile, GitHub Actions | Модель деплоится одной командой | 12) Пуш контейнера в GHCR + деплой на VPS |

------------------------------------------------  
Год 2 «Специализация» (мес 13–24)  
Выбираем **два направления** из трёх:

| Трек | Ресурсы | Глубина | Примерный проект |
|---|---|---|---|
| **A. Мультимодальные медицинские агенты** | [Gemini 2.0 медицинский пример](https://github.com/reflex-dev/reflex-llm-examples) | Vision + Text | Чат-врач по снимкам |
| **B. Эмбеддинги и поиск** | DeepLearning.AI «Understanding Text Embeddings» | Sentence-T5, ColBERT | Semantic-API для 1 млн документов |
| **C. RLHF / инструкционный fine-tuning** | Anthropic Claude course + TRLX | PPO, DPO | Инструкционный 13B-чат для колл-центра |

Каждый трек = 2 квартала (6 спринтов). Пример для трека A:

13.1  Подготовка медицинского датасета (HF Datasets)  
13.2  Instruction fine-tuning Gemini-2.0-Flash  
13.3  Подключение vision-энкодера  
14.1  RLHF на медицинских QA  
14.2  Gradio-UI + HIPAA-совместимый деплой  
14.3  Нагрузочное тестирование (locust)

------------------------------------------------  
Инструменты контроля

• Kanban-доска в GitHub Projects – колонки «To Learn / In Progress / Done».  
• Каждый спринт = issue с чек-листом «что должно работать».  
• По окончании квартала – релиз-тег `v0.x` и короткий пост в README.

Таким образом за 1–2 года вы последовательно закроете все 7 столпов и выйдете на уровень «можно спокойно взять заказ / устроиться LLM-инженером».
