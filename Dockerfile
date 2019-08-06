# nginx:latest
FROM nginx:alpine
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /etc/nginx/logs/
EXPOSE 9000