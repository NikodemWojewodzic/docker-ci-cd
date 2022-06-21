FROM python:3.8

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
RUN pip install python-dotenv

ENV PORT=3000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]