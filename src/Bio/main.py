import json
with open('data.json',encoding='utf-8') as f:
    data = json.load(f)
    f.close()

print(data.get('text'))