from collections import OrderedDict
data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}

od = OrderedDict(sorted(data.items(), key=lambda x:len(x[1]), reverse=False))

ini_dict = dict(od)
#print(ini_dict)
final_dict = {}
for k,v in ini_dict.items():
    new_dict = {}
    val = v
    for k1,v1 in ini_dict.items():
        if v1 == v:
            new_dict[k1] = v1
    sorted(new_dict)
    final_dict.update(new_dict)
print(final_dict)
