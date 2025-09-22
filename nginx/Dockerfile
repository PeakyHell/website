FROM nginx:latest

COPY certificates/cert.pem /etc/nginx/certificates/
COPY certificates/key.pem /etc/nginx/certificates/

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
