FROM python:3.9.0 as python
COPY . /app
WORKDIR  /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
