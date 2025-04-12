import heapq
import sys

INF = float('inf')  # 무한대 값을 정의합니다.
MAX_N = 2000        # 코드트리 랜드의 최대 도시 개수입니다.
MAX_ID = 30005      # 여행상품 ID의 최대값입니다.

input = sys.stdin.readline

N, M = 0, 0  # 도시의 개수 N과 간선의 개수 M을 초기화합니다.
A = []       # 인접 리스트로 그래프 저장
D = []       # 최단거리 저장
isMade = []  # 여행상품 생성 여부
isCancel = []  # 여행상품 취소 여부
S = 0        # 출발 도시

# 여행 상품 클래스
class Package:
    def __init__(self, id, revenue, dest, profit):
        self.id = id
        self.revenue = revenue
        self.dest = dest
        self.profit = profit

    def __lt__(self, other):
        if self.profit == other.profit:
            return self.id < other.id
        return self.profit > other.profit

pq = []

# 우선순위 큐 기반 다익스트라 알고리즘
def dijkstra():
    global D
    D = [INF] * N
    D[S] = 0
    hq = [(0, S)]

    while hq:
        dist, u = heapq.heappop(hq)
        if D[u] < dist:
            continue
        for v, cost in A[u]:
            if D[v] > D[u] + cost:
                D[v] = D[u] + cost
                heapq.heappush(hq, (D[v], v))

# 그래프 구성
def buildLand(n, m, arr):
    global A, N, M
    N, M = n, m
    A = [[] for _ in range(N)]
    for i in range(M):
        u, v, w = arr[i*3], arr[i*3+1], arr[i*3+2]
        A[u].append((v, w))
        A[v].append((u, w))

# 여행 상품 추가
def addPackage(id, revenue, dest):
    isMade[id] = True
    profit = revenue - D[dest]
    heapq.heappush(pq, Package(id, revenue, dest, profit))

# 여행 상품 취소
def cancelPackage(id):
    if isMade[id]:
        isCancel[id] = True

# 최적의 여행상품 판매
def sellPackage():
    while pq:
        p = pq[0]
        if p.profit < 0:
            break
        heapq.heappop(pq)
        if not isCancel[p.id]:
            return p.id
    return -1

# 출발 도시 변경 및 상품 재계산
def changeStart(param):
    global S
    S = param
    dijkstra()
    temp_packages = []
    while pq:
        temp_packages.append(heapq.heappop(pq))
    for p in temp_packages:
        addPackage(p.id, p.revenue, p.dest)

# 메인 함수
def main():
    global isCancel, isMade
    Q = int(input())
    isMade = [False] * MAX_ID
    isCancel = [False] * MAX_ID
    for _ in range(Q):
        query = list(map(int, input().split()))
        T = query[0]
        if T == 100:
            buildLand(query[1], query[2], query[3:])
            dijkstra()
        elif T == 200:
            id, revenue, dest = query[1], query[2], query[3]
            addPackage(id, revenue, dest)
        elif T == 300:
            cancelPackage(query[1])
        elif T == 400:
            print(sellPackage())
        elif T == 500:
            changeStart(query[1])

if __name__ == "__main__":
    main()
