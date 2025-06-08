FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install streamlit requests pandas

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
