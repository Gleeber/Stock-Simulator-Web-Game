FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash gcc musl-dev
COPY ./stocksim stocksim/
ENV STATIC_URL /static
ENV STATIC_PATH stocksim/static
COPY ./requirements.txt stocksim/requirements.txt
RUN pip install -r stocksim/requirements.txt

EXPOSE 5000
ENV FLASK_APP stocksim
CMD ["flask", "run", "--host", "0.0.0.0"]
