import time

from sanic import Sanic
from sanic.response import json, text
from sanic.exceptions import ServerError

from anomaly_detection.time_series.worker import worker

app = Sanic()


@app.route('/')
async def test(_):
    return text('Greetings!')


@app.get('/status')
async def status(_):
    return json({'OK': time.time(), 'status': 200})


@app.post('/detect/time_series/outlier')
async def detect_time_series_outlier(request):
    data = request.json
    try:
        return json(worker(data))
    except Exception as e:
        raise ServerError(e)


def run():
    app.run(host="0.0.0.0", port=8888)
