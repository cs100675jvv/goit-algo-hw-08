import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізація мін-купи
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Повторюємо, доки в купі більше одного елемента
    while len(cables) > 1:
        # Виймаємо два найменші елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість їх об'єднання
        cost = first + second
        total_cost += cost
        
        # Поміщаємо новий об'єднаний кабель назад в купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальна вартість з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
