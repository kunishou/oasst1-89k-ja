import json
import glob

path_list = glob.glob("*.json")

results = []

for path in path_list:
    json_open = open(path, 'r', encoding="utf-8")
    results += json.load(json_open)

json_data = json.dumps(results, indent=4, ensure_ascii=False)
with open(f'oasst1_ja_89k.json', 'w', encoding="utf-8") as f:
    f.write(json_data)