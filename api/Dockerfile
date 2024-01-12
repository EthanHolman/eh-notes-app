FROM python:3.10-slim

# setup
WORKDIR /code
COPY . .

# install packages
RUN pip install -r requirements.txt

# Run API
EXPOSE 5000
CMD ["python3", "app.py"]
