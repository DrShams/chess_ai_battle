import json
#myjson = '["foo", {"bar":["baz", null, 1.0, 2]}]'
with open(r'C:\Users\Shams\Desktop\ChessProject\wrc.json') as f:
  parsed = json.load(f)
#parsed = json.loads(myjson)
print(json.dumps(parsed, indent=4, sort_keys=True))
