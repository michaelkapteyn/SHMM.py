import json

def read_json_file(json_file):
    f = open(json_file, 'r')
    ref_json = json.load(f)
    f.close()
    return ref_json

def write_json_file(filepath, data):
    with open(filepath, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
    f.close()
