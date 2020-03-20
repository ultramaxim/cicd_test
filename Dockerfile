FROM python:3.8.2

RUN mkdir -p /usr/src/api_calculator
WORKDIR /usr/src/api_calculator

COPY . /usr/scr/api_calculator

RUN pip install flask
RUN pip install pytz

EXPOSE 5000

CMD ["python", "/usr/scr/api_calculator/web_core.py"]
