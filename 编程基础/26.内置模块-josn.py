import json
# vardict = {'name':'admin','age':20,'sex':'男'}
# res = json.dumps(vardict)
# print(res,type(res))
# res = json.loads(res)
# print(res,type(res))

vardict = [{'name':'admin','age':20,'sex':'男'},{'name':'aa','age':21,'sex':'m'}]
with open('data.json', 'w') as fp:
    json.dump(vardict,fp)

with open('data.json', 'r') as fp:
    new = json.load(fp)
print(new)