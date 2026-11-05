parts = input().split()
 
values = []
missing = 0
 
for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))
 
print("Olcme:", len(values))
print("Bos:", missing)
 

print("Min:", min(values))
print("Max:", max(values))
print("Orta qiymet:", round(sum(values) / len(values), 1))
 
 
def level(v):
    if v < -105:
        return "zeif"
    elif v < -95:
        return "orta"
    else:
        return "yaxsı"
 
 
for v in values:
    print(v, "→", level(v))
 
counts = {"zeif": 0, "orta": 0, "yaxsı": 0}
 
for v in values:
    s = level(v)
    counts[s] += 1
 
print(counts)
 
share = round(counts["zeif"] / len(values) * 100, 1)
print("Zeif payı:", share, "%")
 
if share >= 30:
    print("Qerar: briqadanı gonder")
elif share >= 10:
    print("Qerar: musahidede saxla")
else:
    print("Qerar: stansiya normaldır")
 
current = 0
best = 0
 
for v in values:
    if level(v) == "zəif":
        current += 1
        if current > best:
            best = current
    else:
        current = 0
 
print("Ən uzun zəif seriya:", best)
