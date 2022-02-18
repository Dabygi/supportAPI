FROM python:latest
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1 #означает, что Python не будет пытаться создавать файлы .pyc
ENV PYTHONUNBUFFERED 1 #гарантирует, что наш вывод консоли выглядит знакомым и не буферизируется Docker
RUN pip install --upgrade pip
COPY . .
RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc
RUN apt-get install gettext -y
RUN pip install -r ./requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]