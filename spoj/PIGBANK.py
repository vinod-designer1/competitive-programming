#http://en.wikipedia.org/wiki/Knapsack_problem
#Integer Knapsack Problem( Duplicate items permitted)
#http://programmers.stackexchange.com/questions/117136/converting-a-bounded-knapsack-problem-to-0-1-knapsack-problem
#http://stackoverflow.com/questions/15476499/variation-on-knapsack-minimum-total-cost-with-exact-weight

def knapsack_01_exact_min_old(weights, values, W):
    # 0-1 knapsack, exact total weight W, minimizing total value
    n = len(weights)
    values = [0] + values
    weights = [0] + weights
    K = [[0 for i in range(W+1)] for j in range(n+1)]
    choice = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            K[i][w] = K[i-1][w]
            choice[i][w] = '|'
            if w >= weights[i]:
                t = K[i-1][w-weights[i]]
                if (w==weights[i] or t) and (K[i][w]==0 or t+values[i] < K[i][w]):
                    choice[i][w] = '\\'
                    K[i][w] = t+values[i]
    return K[n][W]

def knapsack_01_exact_min(weights, values, W):
	# 0-1 knapsack, exact total weight W, minimizing total value
    n = len(weights)
    if W != 0 and n == 0:
    	return 'Impossible'
    elif n == 0:
    	return 0

    if W == 0:
    	return 0

    if n == 1:
    	if W%weights[0] == 0:
    		return values[0] * (W/weights[0])
    	else:
    		return 'Impossible'

    

    N = [0]*(W+1)

def print_choice(choice, weights):
    i = len(choice)-1
    j = len(choice[0])-1
    weights = [0] + weights
    while i > 0 and j > 0:
        if choice[i][j]=='\\':
            print weights[i],
            j -= weights[i]
        i -= 1
    print

n = 2
wt = [1, 30]
vl = [1, 50]
cap = 100

print knapsack_01_exact_min(wt, vl, cap)
