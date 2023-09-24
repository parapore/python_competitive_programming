import itertools

N=int(input())
like321=[1,2,3,4,5,6,7,8,9]

for i in range(2,11):
  for seq in itertools.combinations(range(0,10), i):
      seq2=sorted(seq, reverse=True)
      like321.append(int(''.join(map(str, seq2))))

like321.sort()
print(like321[N-1])