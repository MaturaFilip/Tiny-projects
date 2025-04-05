
s = [4,1,2,1,2]

results = {}

for i in range(len(s)):
    results[s[i]] = 1 + results.get(s[i], 0)

#for k, v in results.items():
#    if v == 1:
#        print(k)
print(results)