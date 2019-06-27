FROM cassandra:latest

WORKDIR /app

ADD . .

RUN chmod +x *.sh

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["cassandra", "-f"]
