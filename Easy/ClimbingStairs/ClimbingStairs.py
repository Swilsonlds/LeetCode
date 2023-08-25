# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbingStairs(target: int) -> int:
    if target < 2:
        return 1
    else:
        return climbingStairs(target-1) + climbingStairs(target-2)
    
print(climbingStairs(5))