FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

EXPOSE 2025
#CMD ["python3", "/code/app.py"]
CMD ["gunicorn", "-c", "gunicorn.conf", "wsgi:application","-b", "0.0.0.0:2025"]