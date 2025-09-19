class BIT2D:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.tree = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    
    def update(self, x, y, delta):
        i = x
        while i <= self.max_x:
            j = y
            while j <= self.max_y:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)
    
    def query(self, x, y):
        if x <= 0 or y <= 0:
            return 0
        result = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                result += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result
    
    def range_query(self, x1, y1, x2, y2):
        return (self.query(x2, y2) - self.query(x1-1, y2) 
                - self.query(x2, y1-1) + self.query(x1-1, y1-1))


n, q = map(int, input().split())

x_cords = set()
y_cords = set()
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x,y))
    x_cords.add(x)
    y_cords.add(y)

queries = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    queries.append((x1, y1, x2, y2))
    x_cords.update([x1, x2])
    y_cords.update([y1, y2])

# Please write your code here.
x_sorted = sorted(x_cords)
y_sorted = sorted(y_cords)

x_map = {x:idx for idx, x in enumerate(x_sorted,1)}
y_map = {y:idx for idx, y in enumerate(y_sorted,1)}

max_x = len(x_sorted)
max_y = len(y_sorted)

bit = BIT2D(max_x, max_y)

for x, y in points:
    bit.update(x_map[x], y_map[y], 1)

results = []
for x1, y1, x2, y2 in queries:
    compressed_x1 = x_map[x1]
    compressed_y1 = y_map[y1]
    compressed_x2 = x_map[x2]
    compressed_y2 = y_map[y2]
    result = bit.range_query(compressed_x1, compressed_y1, compressed_x2, compressed_y2)
    results.append(result)

for result in results:
    print(result)