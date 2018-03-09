class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        i = len(M)
        j = len(M[0])
        N = [[0 for x in range(j)] for y in range(i)] 

        for y in range(i):
            for x in range(j):
                avg = 0
                cnt = 1
                if (x == 0 or x==j-1 or y ==0 or y==i-1):
                    avg = M[y][x]
                    cnt = 1

                    if y-1 >= 0 and x-1 >=0:
                        avg = avg + M[y-1][x-1]
                        cnt = cnt + 1

                    if y-1 >= 0:
                        avg = avg + M[y-1][x]
                        cnt = cnt + 1                

                    if y-1 >= 0 and x+1 < j:
                        avg = avg + M[y-1][x+1]
                        cnt = cnt + 1

                    if x-1 >= 0 :
                        avg = avg + M[y][x-1]
                        cnt = cnt + 1

                    if x+1 < j :
                        avg = avg + M[y][x+1]
                        cnt = cnt + 1   

                    if y+1 < i and x-1 >=0 :
                        avg = avg + M[y+1][x-1]
                        cnt = cnt + 1

                    if y+1 < i:
                        avg = avg + M[y+1][x]
                        cnt = cnt + 1

                    if y+1 < i and x+1 < j:
                        avg = avg + M[y+1][x+1]
                        cnt = cnt + 1

                    avg = avg / cnt
                else:
                    avg = (M[y][x] + M[y-1][x-1] + M[y-1][x] + M[y-1][x+1] + M[y][x-1] + M[y][x+1] + M[y+1][x-1] + M[y+1][x] + M[y+1][x+1])/9

                N[y][x] = int(avg)

        return N