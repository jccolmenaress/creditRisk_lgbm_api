FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./app /app
RUN pip install -r requeriments.txt
EXPOSE 80
CMD [ "uvicorn", "ml_api:app", "--host", "0.0.0.0", "--port", "80" ]