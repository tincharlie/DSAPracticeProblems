import math

def minEatingSpeed(piles, h):
    s, e = 1, max(piles)
    res = e
    while s <= e:
        k = (s + e) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
            if k == 6:# That is my own perspective
                print(f"This is the max bananas she can eat ==>  p:{p},k:{k},hours:{math.ceil(p / k)}")
            else:
                print(f"p:{p},k:{k},hours:{math.ceil(p/k)}")
        if hours <= h:
            res = min(res, k)
            e = k - 1
        else:
            s = k + 1
    return res


k = [3, 6, 7, 11]
h = 8

print(minEatingSpeed(k, h))
