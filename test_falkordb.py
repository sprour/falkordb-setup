#!/usr/bin/env python3
"""
Тестирование FalkorDB для проекта Neuro-Sachok
"""

import redis
import json
import time

# Конфигурация подключения
FALKORDB_HOST = 'zwo4o088ookkc0w4csosgwk4.147.93.72.109.sslip.io'
FALKORDB_PORT = 6379
FALKORDB_PASSWORD = None  # Если нужен пароль, укажите его здесь

def test_connection():
    """Тест базового подключения"""
    print("🔌 Тестирование подключения...")
    try:
        r = redis.Redis(
            host=FALKORDB_HOST,
            port=FALKORDB_PORT,
            password=FALKORDB_PASSWORD,
            decode_responses=True
        )
        result = r.ping()
        print(f"✅ Подключение успешно: {result}")
        return r
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return None

def test_basic_operations(r):
    """Тест базовых операций"""
    print("\n📊 Тестирование базовых операций...")
    
    # Создание узла
    query = """
    CREATE (n:IdeaCard {
        id: 'test_001',
        title: 'Тестовая идея',
        content: 'Это тестовая идея для проверки FalkorDB',
        timestamp: timestamp(),
        tags: ['test', 'falkordb', 'neuro-sachok']
    })
    RETURN n
    """
    
    try:
        result = r.execute_command('GRAPH.QUERY', 'GLOBAL', query)
        print(f"✅ Узел создан: {result}")
    except Exception as e:
        print(f"❌ Ошибка создания узла: {e}")

def test_semantic_links(r):
    """Тест семантических связей"""
    print("\n🔗 Тестирование семантических связей...")
    
    # Создание связанных идей
    query = """
    CREATE (idea1:IdeaCard {
        id: 'idea_001',
        title: 'Искусственный интеллект',
        content: 'AI - это технология будущего',
        tags: ['ai', 'technology', 'future']
    })
    CREATE (idea2:IdeaCard {
        id: 'idea_002', 
        title: 'Машинное обучение',
        content: 'ML - подраздел AI',
        tags: ['ml', 'ai', 'algorithms']
    })
    CREATE (idea1)-[:SEMANTIC_LINK {
        type: 'RELATED',
        strength: 0.9,
        created_at: timestamp()
    }]->(idea2)
    RETURN idea1, idea2
    """
    
    try:
        result = r.execute_command('GRAPH.QUERY', 'GLOBAL', query)
        print(f"✅ Семантические связи созданы: {result}")
    except Exception as e:
        print(f"❌ Ошибка создания связей: {e}")

def test_search_operations(r):
    """Тест поисковых операций"""
    print("\n🔍 Тестирование поисковых операций...")
    
    # Поиск по тегам
    query = """
    MATCH (n:IdeaCard)
    WHERE 'ai' IN n.tags
    RETURN n.title, n.tags
    """
    
    try:
        result = r.execute_command('GRAPH.QUERY', 'GLOBAL', query)
        print(f"✅ Поиск по тегам: {result}")
    except Exception as e:
        print(f"❌ Ошибка поиска: {e}")

def test_graph_statistics(r):
    """Тест статистики графа"""
    print("\n📈 Тестирование статистики графа...")
    
    queries = [
        "CALL db.labels()",
        "CALL db.relationshipTypes()", 
        "MATCH (n) RETURN count(n) as node_count",
        "MATCH ()-[r]->() RETURN count(r) as relationship_count"
    ]
    
    for query in queries:
        try:
            result = r.execute_command('GRAPH.QUERY', 'GLOBAL', query)
            print(f"✅ {query}: {result}")
        except Exception as e:
            print(f"❌ Ошибка в запросе '{query}': {e}")

def cleanup_test_data(r):
    """Очистка тестовых данных"""
    print("\n🧹 Очистка тестовых данных...")
    
    query = "MATCH (n) DETACH DELETE n"
    
    try:
        result = r.execute_command('GRAPH.QUERY', 'GLOBAL', query)
        print(f"✅ Данные очищены: {result}")
    except Exception as e:
        print(f"❌ Ошибка очистки: {e}")

def main():
    """Основная функция тестирования"""
    print("🚀 Тестирование FalkorDB для Neuro-Sachok")
    print("=" * 50)
    
    # Подключение
    r = test_connection()
    if not r:
        return
    
    # Тесты
    test_basic_operations(r)
    test_semantic_links(r)
    test_search_operations(r)
    test_graph_statistics(r)
    
    # Очистка (опционально)
    cleanup_test_data(r)
    
    print("\n🎉 Тестирование завершено!")

if __name__ == "__main__":
    main()
