import json
import quart
import os
import quart_cors
import httpx
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

MOTION_API_URL = "https://api.usemotion.com/v1"
MOTION_API_KEY = "YOUR MOTION API KEY"
TIMEOUT_DURATION = 60.0  # Specify the timeout duration in seconds

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
async def api_proxy(path):
    url = f"{MOTION_API_URL}/{path}"
    headers = {
        "Accept": "application/json",
        "X-API-Key": MOTION_API_KEY
    }
    data = await request.get_data()

    async with httpx.AsyncClient(timeout=TIMEOUT_DURATION) as client:
        if request.method == 'GET':
            response = await client.get(url, headers=headers, params=request.args)
        else:
            response = await client.request(
                request.method, url, headers=headers, data=data
            )

    return quart.Response(response.content, response.status_code)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()