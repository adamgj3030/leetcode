class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind(len(accounts))
        emailToAcc = {} # email to index

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    dsu.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        emailGrouping = defaultdict(list) # index to email grouping
        for email, i in emailToAcc.items():
            leader = dsu.find(i)
            emailGrouping[leader].append(email)
        
        res = []
        print(emailGrouping)
        for i, email in emailGrouping.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGrouping[i]))
        return res
