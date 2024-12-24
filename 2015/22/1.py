from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

@cache
def fight(
        playerHealth,
        playerMana,
        bossHealth,
        bossDamage,
        shieldLeft,
        posionLeft,
        rechargeLeft,
        playerTurn
):
    if shieldLeft:
        shieldLeft -= 1

    if posionLeft:
        bossHealth -= 3
        posionLeft -= 1

    if rechargeLeft:
        playerMana += 101
        rechargeLeft -= 1
    
    if bossHealth <= 0:
        return 0
    
    if not playerTurn:
        playerHealth -= bossDamage
        if shieldLeft:
            playerHealth += 7
        
        if playerHealth <= 0:
            return math.inf
        return fight(playerHealth, playerMana, bossHealth, bossDamage, shieldLeft, posionLeft, rechargeLeft, not playerTurn)
    
    
    minMana = math.inf

    if playerMana >= 53:
        minMana = min(minMana, 53+fight(playerHealth, playerMana-53, bossHealth-4, bossDamage, shieldLeft, posionLeft, rechargeLeft, not playerTurn))

    if playerMana >= 73:
        minMana = min(minMana, 73+fight(playerHealth+2, playerMana-73, bossHealth-2, bossDamage, shieldLeft, posionLeft, rechargeLeft, not playerTurn))
    
    if posionLeft <= 1 and playerMana >= 173:
        minMana = min(minMana, 173+fight(playerHealth, playerMana-173, bossHealth, bossDamage, shieldLeft, 6, rechargeLeft, not playerTurn))

    if shieldLeft <= 1 and playerMana >= 113:
        minMana = min(minMana, 113+fight(playerHealth, playerMana-113, bossHealth, bossDamage, 6, posionLeft, rechargeLeft, not playerTurn))

    if rechargeLeft <= 1 and playerMana >= 229:
        minMana = min(minMana, 229+fight(playerHealth, playerMana-229, bossHealth, bossDamage, shieldLeft, posionLeft, 5, not playerTurn))

    return minMana

print(fight(50, 500, 51, 9, 0, 0, 0, True))