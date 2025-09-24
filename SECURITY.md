# 🔐 FalkorDB Security Guide

## 🚨 Текущая проблема
FalkorDB развернут **БЕЗ ПАРОЛЯ** - это критическая уязвимость безопасности!

## ✅ Решение

### 1. В Coolify добавьте переменные окружения:
```
FALKORDB_PASSWORD=neuro_sachok_secure_2024
FALKORDB_LOG_LEVEL=INFO
REDIS_COMMANDER_USER=admin
REDIS_COMMANDER_PASSWORD=admin123
```

### 2. Redeploy приложение в Coolify

### 3. После перезапуска подключение будет:
```bash
# Redis CLI
redis-cli -h YOUR_HOST -p 6379 -a neuro_sachok_secure_2024

# Python
import redis
r = redis.Redis(
    host='YOUR_HOST',
    port=6379,
    password='neuro_sachok_secure_2024'
)
```

## 🔒 Дополнительные меры безопасности

### A. ACL (Access Control Lists)
Создайте пользователей с ограниченными правами:

```bash
# Пользователь только для чтения
ACL SETUSER readonly_user on >readonly_password ~* &* +@read +GRAPH.QUERY

# Пользователь для приложения
ACL SETUSER app_user on >app_password ~* &* +@read +@write +GRAPH.QUERY
```

### B. TLS шифрование
Для продакшена добавьте TLS:

```yaml
# В docker-compose.yaml
command: [
  "redis-server", 
  "--tls-port", "6380", 
  "--port", "0",
  "--tls-cert-file", "/tls/server.crt",
  "--tls-key-file", "/tls/server.key",
  "--requirepass", "${FALKORDB_PASSWORD}"
]
```

### C. Firewall правила
Ограничьте доступ по IP:
```bash
# Только для ваших серверов
iptables -A INPUT -p tcp --dport 6379 -s YOUR_SERVER_IP -j ACCEPT
iptables -A INPUT -p tcp --dport 6379 -j DROP
```

## 🧪 Тестирование безопасности

### Проверка пароля:
```bash
# Должно работать
redis-cli -h YOUR_HOST -p 6379 -a neuro_sachok_secure_2024 ping

# Должно НЕ работать
redis-cli -h YOUR_HOST -p 6379 ping
```

### Проверка ACL:
```bash
# Список пользователей
ACL LIST

# Проверка прав пользователя
ACL GETUSER app_user
```

## 📋 Checklist безопасности

- [ ] Установлен сильный пароль
- [ ] Настроены ACL пользователи
- [ ] Включено TLS (для продакшена)
- [ ] Настроен firewall
- [ ] Регулярное обновление паролей
- [ ] Мониторинг подключений
- [ ] Backup данных

## 🚀 Для приложений Neuro-Sachok

### Подключение из Python:
```python
import redis

# Безопасное подключение
r = redis.Redis(
    host='zwo4o088ookkc0w4csosgwk4.147.93.72.109.sslip.io',
    port=6379,
    password='neuro_sachok_secure_2024',
    decode_responses=True
)

# Тест подключения
r.ping()  # True
```

### Подключение из Node.js:
```javascript
const redis = require('redis');

const client = redis.createClient({
    host: 'zwo4o088ookkc0w4csosgwk4.147.93.72.109.sslip.io',
    port: 6379,
    password: 'neuro_sachok_secure_2024'
});
```

## ⚠️ Важно!
После настройки пароля **все существующие подключения будут разорваны** и потребуют повторной авторизации.
