import json

file_path = f"uploads/test.json"

with open(file_path, "wt") as f:
    f.write(json.dumps({}))
