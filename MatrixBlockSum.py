class Solution:
    def matrixBlockSum(self, a: List[List[int]], k: int) -> List[List[int]]:
        k+=1
        n=len(a)
        m=len(a[0])
        d=[[i for i in j]for j in a]
        for i in range(n):
            s=0
            for j in range(m):
                if j>=k:
                    s-=a[i][j-k]
                d[i][j]+=s
                s+=a[i][j]
        for i in range(n):
            s=0
            for j in range(m-1,-1,-1):
                if m-1-j>=k:
                    s-=a[i][j+k]
                d[i][j]+=s
                s+=a[i][j]
        a=[[i for i in j]for j in d]
        for i in range(m):
            s=0
            for j in range(n):
                if j>=k:
                    s-=a[j-k][i]
                d[j][i]+=s
                s+=a[j][i]
        for i in range(m):
            s=0
            for j in range(n-1,-1,-1):
                if n-1-j>=k:
                    s-=a[j+k][i]
                d[j][i]+=s
                s+=a[j][i]
        return d