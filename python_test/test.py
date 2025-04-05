strs = ["eat","tea","tan","ate","nat","bat"]


counter = {}
for i in strs:
    srt = "".join(sorted(i))
    if srt not in counter:
        counter[srt] = []
    counter[srt].append(i)

print(list(counter.values()))