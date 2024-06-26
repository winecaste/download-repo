### Тестовое задание

**Запуск проекта:**

`python radium\src\main.py `

**Запуск тестов:**

`pytest`

**Техническое задание:**

1) Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration во временную папку.
2) После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.

* Код должен проходить без замечаний проверку линтером wemake-python-styleguide.
* Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration
* Обязательно 100% покрытие тестами

**Вопросы:**
1) Как вы реализовали асинхронное выполнение задач в вашем скрипте?
* В скрипте были использованы асинхронные функции и корутины из стандартной библиотеки asyncio. Для выполнения HTTP-запросов был использован aiohttp, который предоставляет асинхронный HTTP-клиент для работы с веб-ресурсами

* В функции download_repo инициируется асинхронный HTTP-запрос к указанному URL, затем асинхронно считываются и записываются данные
* Для вычисления хэша файла также использовалась асинхронная функция calculate_hash, которая читает файл кусками асинхронно и вычисляет хэш для каждого куска
2) Какие библиотеки использовались для скачивания содержимого репозитория и для каких целей?
* Для скачивания содержимого репозитория была использована библиотека aiohttp. Она используется для асинхронного выполнения HTTP-запросов. В данном случае она была использована для выполнения GET-запроса к URL-адресу репозитория и получения его содержимого.
3) Какие проблемы асинхронности вы сталкивались при выполнении задания и как их решали?
* Синхронизация асинхронных вызовов:  Необходимо было дождаться завершения нескольких асинхронных операци. Использовал asyncio.gather() для одновременного запуска нескольких асинхронных задач и ожидания их завершения.
* Тестирование асинхронного кода. Стандартные методы тестирования не работают с асинхронными функциями.
Использовал библиотеку pytest-asyncio, которая предоставляет специальные декораторы для тестирования асинхронного кода, такие как @pytest.mark.asyncio.
4) Как вы организовали скачивание файлов во временную папку?
* Скачивание файлов во временную папку было организовано с использованием библиотеки tempfile. TemporaryDirectory из модуля tempfile создает временный каталог наиболее безопасным способом. При создании каталога нет условий гонки.
5) Как вы настраивали свой проект для соответствия конфигурации nitpick, указанной в задании? Были ли трудности при настройке?
* Первым шагом я установил wemake-python-styleguide, так как он является основой для конфигурации nitpick. Затем установил конфигурцию nitpick в pyproject.toml. После настройки инструментов я применил их к моему проекту, чтобы убедиться, что код соответствует конфигурации. Настройка проекта не вызвала проблем
6) Какие инструменты использовали для измерения 100% покрытия тестами?
* pytest-cov: Это расширение для фреймворка тестирования pytest, которое интегрирует инструмент Coverage.py в процесс выполнения тестов с помощью pytest. Оно автоматически запускает анализатор покрытия и генерирует отчеты после каждого запуска тестов.
7) Какие типы тестов вы написали для проверки функциональности вашего скрипта?
* Написаны интеграционные и модульные тесты
8) Как вы тестировали асинхронный код? Использовали ли вы моки (mocks) или стабы (stubs) для тестирования асинхронных операций?
*  Использовал unittest.mock.patch для создания заглушек для функций download_repo() и calculate_hash(), чтобы не выполнять реальные HTTP-запросы и операции с файловой системой во время тестирования.
