from celery import Celery


brokers = 'redis://localhost:6379'
backend = 'redis://localhost'
app = Celery('tasks', backend=backend, broker=brokers)


@app.task
def add(x, y):
    return x + y
