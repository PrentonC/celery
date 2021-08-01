FROM python:3
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A test_celery worker flower --loglevel=info
# ENTRYPOINT celery -A test_celery flower --loglevel=info
# CMD ["celery","-A","test_celery", "flower", "--loglevel=info"]
