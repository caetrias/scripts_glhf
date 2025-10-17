import time
import json
import base64

def print_sess_id(user, id, role):
    tempo = int(time.time()//1)+3600
    i = 0
    payload = {
            "u":user,
            "id":id,
            "r":role,
            "exp":tempo, 
            "v":1
        }

    payload_json = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
    payload_bytes = payload_json.encode('utf-8')
    encoded = base64.b64encode(payload_bytes).decode('utf-8')
    print(f"Encoded: {encoded}")

print_sess_id("windows96", 1337, "user")