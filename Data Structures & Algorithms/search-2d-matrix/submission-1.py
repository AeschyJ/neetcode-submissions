class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(target, l):
            from collections import deque
            if target == l[0]:
                return True
            elif target == l[-1]:
                return True
            else:
                t = len(l) // 2
                d = deque()
                d.append(0)
                d.append(len(l)-1)
                for i in l:
                    if target == l[t]:
                        return True
                    elif target > l[t]:
                        if t != d[0]:
                            d.appendleft(t)
                            t = (d[-1] + t) // 2
                        else: return False
                    else:
                        if t != d[-1]:
                            d.append(t)
                            t = (d[0] + t) // 2
                        else: return False

        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                if i < len(matrix) - 1:
                    if target < matrix[i+1][0]:
                        return binary_search(target,matrix[i])
                elif i == len(matrix) - 1:
                    if target <= matrix[i][-1]:
                        return binary_search(target,matrix[i])
                    else: return False
            else: return False

        