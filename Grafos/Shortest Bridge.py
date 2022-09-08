def shortestBridge(self, A):
    def dfs(A,i,j):
        if i < 0 or j < 0 or i > len(A)-1 or j > len(A[0])-1:
            return
        if self.visited[i][j] or A[i][j] == 0: return
        self.visited[i][j] = True
        self.queue.append((i,j))
        for k in range(4):
            rr = i + self.rowVector[k]
            cc = j + self.colVector[k]
            dfs(A,rr,cc)
    self.visited = [[False for i in range(len(A[0]))] for j in range(len(A))]
    self.rowVector = [1,-1,0,0]
    self.colVector = [0,0,1,-1]
    self.queue = []
    found = False
    for i in range(len(A)):
        if found:
            break;
        for j in range(len(A[0])):
            if A[i][j] == 1:
                dfs(A,i,j)
                found = True
                break;
    step = 0
    while self.queue:
        subQ= []
        while self.queue:
            temp = self.queue.pop(0)
            for k in range(4):
                i = temp[0] + self.rowVector[k]
                j = temp[1] + self.colVector[k]
                if i < 0 or j < 0 or i > len(A)-1 or j > len(A[0])-1 or self.visited[i][j]:
                    continue;
                if A[i][j] == 1:
                    return step
                subQ.append((i,j))
                self.visited[i][j] = True
        self.queue = subQ
        step += 1
    return -1