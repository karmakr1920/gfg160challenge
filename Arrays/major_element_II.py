def findMajority(arr):
        #Your Code goes here.
        if not arr:
            return []
        # find upto 2 candidates for n//3 majority
        candidate1,candidate2 = None,None
        count1,count2 = 0,0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1,count1 = num, 1
            elif count2 == 0:
                candidate2,count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        #verify the candidates
        res = []
        n = len(arr)
        for candidate in [candidate1,candidate2]:
            if candidate is not None and arr.count(candidate) > n//3:
                res.append(candidate)
        return sorted(res)

# print(findMajority([33,545,23,1,1,1,1,2,22,2,1,4,23]))