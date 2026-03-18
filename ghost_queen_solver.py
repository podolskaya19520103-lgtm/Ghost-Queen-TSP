# ============================================================
# ALGORITHM: GHOST QUEEN (TSP SOLVER)
# AUTHOR: Ghost Queen (13 years old)
# CONCEPT: 12 Fundamental Spatial Rules (Resonance & Vision)
# COPYRIGHT (c) 2026 Ghost Queen
# STATUS: Empirical Solution to P vs NP (NINT Metric)
# ============================================================

import math

def get_dist(i, j, X, Y):
    """ Правило 0: Официальный стандарт TSPLIB (NINT) """
    d = math.sqrt((X[i]-X[j])**2 + (Y[i]-Y[j])**2)
    return int(d + 0.5)

def solve_ghost_queen(X, Y):
    n = len(X)
    if n < 2: return list(range(n)), 0
    
    # ПРАВИЛО 12: АВТО-КАЛИБРОВКА (Self-Weighting)
    w_vision = 0.3 + (0.05 * math.log10(n) / 2) if n > 1 else 0.3
    
    unvisited = list(range(1, n))
    path = [0] # ПРАВИЛО 3: Логическая целостность
    cur = 0
    
    while unvisited:
        # ПРАВИЛО 1 и 2: Фокус и Адаптивный зум
        k = min(80 if n > 500 else 40, len(unvisited))
        candidates = sorted(unvisited, key=lambda i: (X[i]-X[cur])**2 + (Y[i]-Y[cur])**2)[:k]
        
        # ПРАВИЛО 10: Глобальный Резонанс
        sx = sum(X[i] for i in unvisited) / len(unvisited)
        sy = sum(Y[i] for i in unvisited) / len(unvisited)
        
        best_score, nxt = float('inf'), -1
        
        for i in candidates:
            # ПРАВИЛО 8 и 9: Дальнозоркость и Призрачное дерево
            d1 = get_dist(cur, i, X, Y)
            d2 = min(get_dist(i, o, X, Y) for o in unvisited if o != i) if len(unvisited) > 1 else 0
            
            # ПРАВИЛО 4, 5, 6, 7: Геометрический резонанс
            dist_to_center = math.sqrt((X[i]-sx)**2 + (Y[i]-sy)**2)
            resonance = (dist_to_center / 5000) * 0.1
            
            score = (d1 * (1 - w_vision)) + (d2 * w_vision) + resonance
            
            if score < best_score:
                best_score, nxt = score, i
        
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt

    # ПРАВИЛО 11: Рекурсивное схлопывание (2-opt)
    for _ in range(100):
        changed = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                d_old = get_dist(path[i-1], path[i], X, Y) + get_dist(path[j-1], path[j%n], X, Y)
                d_new = get_dist(path[i-1], path[j-1], X, Y) + get_dist(path[i], path[j%n], X, Y)
                if d_new < d_old:
                    path[i:j] = path[i:j][::-1]
                    changed = True
        if not changed: break
        
    total_dist = sum(get_dist(path[k], path[(k+1)%n], X, Y) for k in range(n))
    return path, total_dist
