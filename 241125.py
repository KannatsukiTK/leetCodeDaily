'''
743.网络延迟时间
有 n 个网络节点，标记为 1 到 n。
给你一个列表 times，表示信号经过 有向 边的传递时间。 
times[i] = (ui, vi, wi)，
其中 ui 是源节点，vi 是目标节点，wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？
如果不能使所有节点收到信号，返回 -1 。
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX = float('inf') # python正无穷大
        graph = [[MAX] * n for _ in range(n)]
        for item in times: #邻接矩阵
            graph[item[0] - 1][item[1] - 1] = item[2]
        #这个循环更简单的写法：for x,y,t in times: graph[x-1][y-1] = t
        #Dijkstra
        visited = [False] * n # U
        dist = [MAX] * n # S
        # 初始化第一个节点,最短路径长为0
        dist[k-1] = 0
        # 传播路径
        for _ in range(n): # n = matrix_length
            min_index = -1
            min_value = MAX
            # 寻找最小值（初始为寻找起点）
            for index in range(n):
                if not visited[index] and dist[index] < min_value: # 这里min_value和dist的初始值一样
                    min_value = dist[index]
                    min_index = index
            # 标志访问过了
            visited[min_index] = True
            # 更新distance，算起点到新节点的距离
            for index in range(n):
                dist[index] = min(dist[index], dist[min_index] + graph[min_index][index])
        
        # for i in range(n):
        #     if visited[i] == False:
        #         return -1
        #没有考虑非连通图的情况
        ans = max(dist)
        # return ans
        return ans if ans < float('inf') else -1
'''
经典Dijkstra算法，关键点：
visited = [False] * n #未使用过的节点
dist = [MAX] * n #到每个节点的最短距离
循环节点个数次，每次先找到图中距离起点最近的点（dist最小），
然后再遍历一遍整张图，根据最小值更新dist（连着的更新，不连的就不更新，不用考虑neighbors，不是BFS）
此题要求找到最长时间，所以就从所有的传播时间里找到最大的那个。要求找不到时返回-1
'''