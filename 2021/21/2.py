from functools import cache
from collections import defaultdict

numberOfPermuations = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@cache
def dp(pos1, pos2, score1, score2):
    res = [0, 0]
    for i in range(3, 10):
        newPos1 = (pos1 + i) % 10
        newScore1 = newPos1 + score1 + 1
        if newScore1 >= 21:
            res[0] += numberOfPermuations[i]
            continue
        
        for j in range(3, 10):
            newPos2 = (pos2 + j) % 10
            newScore2 = newPos2 + score2 + 1
            if newScore2 >= 21:
                res[1] += numberOfPermuations[i] * numberOfPermuations[j]
                continue

            tmp = dp(newPos1, newPos2, newScore1, newScore2)
            res[0] += numberOfPermuations[i] * numberOfPermuations[j] * tmp[0]
            res[1] += numberOfPermuations[i] * numberOfPermuations[j] * tmp[1]

    return res

            
print(max(dp(7,0,0,0)))
                    