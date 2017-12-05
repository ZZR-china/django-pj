from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379//0',
             backend='redis',
             include=['tasks'])


if __name__ == '__main__':
    print(1)
