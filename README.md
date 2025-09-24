# FalkorDB 

## Быстрый старт

1. Скопируйте `env.example` в `.env`
2. Настройте переменные окружения
3. Деплойте через Coolify (используйте `docker-compose.yaml`)

## Доступ

- **FalkorDB Web UI:** http://localhost:3000
- **Redis API:** localhost:6379
- **Redis Commander:** http://localhost:8081

## Переменные окружения

- `FALKORDB_PASSWORD` - Пароль для FalkorDB
- `FALKORDB_LOG_LEVEL` - Уровень логирования (INFO, DEBUG, ERROR)
- `FALKORDB_PORT` - Порт Redis API (по умолчанию 6379)
- `FALKORDB_WEB_PORT` - Порт Web UI (по умолчанию 3000)
- `REDIS_COMMANDER_USER` - Пользователь Redis Commander (по умолчанию admin)
- `REDIS_COMMANDER_PASSWORD` - Пароль Redis Commander
- `REDIS_COMMANDER_PORT` - Порт Redis Commander (по умолчанию 8081)

## Тестирование подключения

```bash
# Проверка через redis-cli
redis-cli -h your-host -p 6379 ping

# Создание тестового графа
redis-cli -h your-host -p 6379
> GRAPH.QUERY test "CREATE (:Person {name: 'Alice'})-[:KNOWS]->(:Person {name: 'Bob'})"
> GRAPH.QUERY test "MATCH (p:Person) RETURN p"
```

## Интеграция с Neuro-Sachok

В вашем MCP сервисе используйте следующие переменные:

```env
FALKORDB_HOST=falkordb
FALKORDB_PORT=6379
FALKORDB_PASSWORD=${FALKORDB_PASSWORD}
ZETTELKASTEN_GRAPH_NAME=neuro_sachok
```
