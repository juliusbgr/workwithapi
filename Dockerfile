FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install streamlit requests pandas

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
