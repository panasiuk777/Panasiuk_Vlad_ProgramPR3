
import math

# Особисті дані
NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"

# Розміри кімнати (демонстраційні значення)
LENGTH = 4.0
WIDTH = 3.5
HEIGHT = 2.7

# Розміри дверей і вікна
DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0
WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

# Параметри плитки
TILE_SIZE = 0.3
TILE_PRICE = 42.30

# Площа підлоги та стін
floor_area = LENGTH * WIDTH
wall_area = (
    2 * (LENGTH + WIDTH) * HEIGHT
    - DOOR_WIDTH * DOOR_HEIGHT
    - WINDOW_WIDTH * WINDOW_HEIGHT
)

# Діагоналі
floor_diag = math.hypot(LENGTH, WIDTH)
room_diag = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)

# Кількість плиток
tile_area = TILE_SIZE ** 2
tiles_exact = floor_area / tile_area

tiles_round = round(tiles_exact)
tiles_floor = math.floor(tiles_exact)
tiles_ceil = math.ceil(tiles_exact)

tiles_to_buy = math.ceil(tiles_exact * 1.10)

# Кількість фарби
paint_liters = wall_area / 10 * 2
paint_cans = math.ceil(paint_liters / 2.5)

# Вартість плитки двома способами
cost_mul = tiles_to_buy * TILE_PRICE

cost_sum = 0.0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"{NAME} {SURNAME}, {GROUP}")
print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")

print(f"\ntiles exact:   {tiles_exact:.2f}")
print(f"  round:       {tiles_round}")
print(f"  floor:       {tiles_floor}")
print(f"  ceil:        {tiles_ceil}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")

print(f"paint:         {paint_liters:.2f} l -> "
      f"{paint_cans} cans of 2.5 l")

print(f"\ntiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")
