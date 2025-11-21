from collections import defaultdict


# 给定一棵树，用father数组表示，其中根节点1的father为0，共有n个节点。给定二维数组queries，
# 其中每个元素由u、v两个整数组成，表示要从树中的u节点走到v。每个节点有一个字符，用chs数组表示。
# 要求对每个query，求出u到v经过的路径组成的字符串中，是否存在子序列'BUG'。
class Tree:
    def __init__(self, n, father, chs):
        self.n = n
        self.chs = chs
        self.tree = defaultdict(list)
        self.LOG = (n + 1).bit_length()  # 计算最大深度 log(n)
        self.parent = [[-1] * self.LOG for _ in range(n + 1)]  # 倍增表
        self.depth = [0] * (n + 1)

        # 构建树
        for child in range(2, n + 1):  # 从 2 到 n 建树
            self.tree[father[child - 1]].append(child)

        # 预处理 LCA
        self.dfs(1, -1)
        self.precompute_lca()

    def dfs(self, node, par):
        """ 深度优先搜索来初始化 parent 和 depth """
        self.parent[node][0] = par
        for child in self.tree[node]:
            if child == par:
                continue
            self.depth[child] = self.depth[node] + 1
            self.dfs(child, node)

    def precompute_lca(self):
        """ 预处理倍增表 """
        for j in range(1, self.LOG):
            for i in range(1, self.n + 1):
                if self.parent[i][j - 1] != -1:
                    self.parent[i][j] = self.parent[self.parent[i][j - 1]][j - 1]

    def find_lca(self, u, v):
        """ 倍增法求 LCA """
        if self.depth[u] < self.depth[v]:  # 让 u 更深
            u, v = v, u

        # 使 u 和 v 到相同深度
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if (diff >> i) & 1:
                u = self.parent[u][i]

        if u == v:
            return u

        # 倍增法同步向上找 LCA
        for i in range(self.LOG - 1, -1, -1):
            if self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]

        return self.parent[u][0]

    def get_path_chars(self, u, v):
        """ 获取从 u 到 v 的路径上的字符 """
        lca = self.find_lca(u, v)
        path = []

        # u -> lca
        while u != lca:
            path.append(self.chs[u - 1])  # chs 是 0-based
            u = self.parent[u][0]

        path.append(self.chs[lca - 1])  # 加上 LCA 节点

        # v -> lca（逆向存储）
        v_path = []
        while v != lca:
            v_path.append(self.chs[v - 1])
            v = self.parent[v][0]

        path.extend(reversed(v_path))  # 逆向拼接
        return ''.join(path)

    def contains_bug(self, path):
        """ 判断字符串中是否存在子序列 'BUG' """
        target = "BUG"
        i = 0
        for c in path:
            if c == target[i]:
                i += 1
            if i == 3:
                return True
        return False

    def process_queries(self, queries):
        results = []
        for u, v in queries:
            path_str = self.get_path_chars(u, v)
            results.append("YES" if self.contains_bug(path_str) else "NO")
        return results


# 示例测试
n = 7
father = [0, 1, 1, 2, 2, 3, 3]  # 根节点 1 的 father 是 0
chs = "BBGUUUG"  # 每个节点的字符
queries = [(4, 5), (6, 7), (2, 6), (1, 7)]  # 查询路径

tree = Tree(n, father, chs)
results = tree.process_queries(queries)
print(results)  # 例如: ['NO', 'YES', 'YES', 'YES']
