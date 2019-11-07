import time

from sanic import Sanic
from sanic.response import json, text
from sanic.exceptions import ServerError

# import anomaly_detection.time_series.worker as w

app = Sanic()


@app.route('/')
async def test(_):
    return text('Greetings!')


@app.get('/status')
async def status(_):
    return json({'OK': time.time(), 'status': 200})


# @app.post('/detect/time_series/low')
# async def detect_time_series_low(request):
#     data = request.json
#     try:
#         return json(w.worker(data))
#     except Exception as e:
#         raise ServerError(e)


def run():
    app.run(host="0.0.0.0", port=7754)
