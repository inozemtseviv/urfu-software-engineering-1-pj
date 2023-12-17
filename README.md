# Summarizer

Сервис предназначен для сокращения исходного текста

## Пример использования

Запрос:

```shell
curl --location 'http://pi.pragmus.ru/summarize' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Уральский федеральный университет создан в контексте реализации концепции долгосрочного развития Российской Федерации как один из глобальных лидеров образования и научно-инновационных разработок. Миссия университета — повышение международной конкурентоспособности Уральского региона и обеспечение реиндустриализации, наращивание человеческого и научно-технического потенциала, сбалансированное обновление традиционных и развитие постиндустриальных отраслей экономики России, в первую очередь на территории Уральского федерального округа. Стратегической целью создания университета является формирование в Уральском федеральном округе научно-образовательного и инновационного центра, ядром которого станет университет. Это обеспечит лидерство университета в области естественных, гуманитарных и технических наук, его вхождение в число ведущих мировых образовательных и интеллектуальных центров."
}'
```

Ответ:

```json
{
  "text": "Уральский федеральный университет создан в рамках реализации концепции долгосрочного развития Российской Федерации как один из глобальных лидеров образования и научно-инновационных разработок. Миссия университета — повышение международной конкурентоспособности Уральского региона и обеспечение реиндустриализации, наращивание человеческого и научно-технического потенциала, сбалансированное обновление традиционных и развитие постиндустриальных отраслей экономики России, в первую очередь на территории Уральского федерального округа."
}
```

## Установка зависимостей

Зависимости указаны в файле [requirements.txt](requirements.txt)

Для установки можно использовать команду:

```shell
pip install -r requirements.txt
```

## Переменные среды окружения

Для корректной работы приложения необходимо задать данным переменным значения:

- `SUMMARIZER_TYPE` - `remote` или `local`. Определяет, какой сервис использовать: запускать модель локально или с
  помощью http-запроса к API huggingface;
- `API_TOKEN` - токен, полученный в huggingface.

Для локального развёртывания эти переменные можно указать в файле `.env`.

## Запуск

```shell
uvicorn main:app
```

## Запуск в Docker

Требуется:

- утилита [Make](https://ru.wikipedia.org/wiki/Make)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

Для поднятия всех сервисов в Docker:

```shell
make up
```

Для остановки работы сервисов:

```shell
make down
```