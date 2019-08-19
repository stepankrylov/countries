import json
import hashlib

#with open(r'countries_wiki_url.txt', 'r', encoding='utf-8') as file:
#    p = [hashlib.md5(str(item).encode("utf-8")).hexdigest() for item in file]
#    print(len(p), p)

def hash():
    with open(r'countries_wiki_url.txt', 'r', encoding='utf-8') as file:
        for item in file:
            yield hashlib.md5(str(item).encode("utf-8")).hexdigest()

c = hash()

p = []
for item in c:
    p.append(item)
    
print(len(p), p)