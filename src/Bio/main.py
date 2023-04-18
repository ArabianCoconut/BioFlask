"""
* Bio python based on Python 3.11.x
* This is simple python application for pairwise alignment.
"""

import json
with open('data.json',encoding='utf-8') as f:
    data = json.load(f)
    f.close()

print(data.get('Data'))
