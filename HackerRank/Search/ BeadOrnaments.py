#http://en.wikipedia.org/wiki/Cayley%27s_formula
## Two things
# ways to arrage tree for each color
# and ways to combine all trees
## ways to arrange each tree be T(n)
# T(n) = n^n-2
## combining trees 
# b(i) = beads in tree i
# a(i) = ways to arrange tree i
# to combine to trees conf i1, i2= (b(i1)*arrange(i1)) * (b(i2)*arrange(i2))
# conf(i1, i2) = (b(i1)^(b(i1)-1)) * (b(i2)^(b(i2)-1))
# so for n trees
# http://math.stackexchange.com/questions/293669/total-permutation-of-tree-if-we-combine-n-tree
# (b(i1)+b(i2)+...+b(in))^(b(i1)+b(i2)+...+b(in)-2)
# b(0)*b(1)*…*b(n) *  (b(0)+b(1)+…+b(n))^n-2
# combining 1 &2 
# b(0)b(0)-1 * b(1)b(1)-1 * … *b(n)b(n)-1 *  (b(0)+b(1)+…+b(n))n-2


t = input()
while t > 0:
	n = input()
	ar = [int(i) for i in raw_input().strip().split(' ')]
	init_ar = [[0]*n]*n