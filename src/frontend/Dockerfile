FROM nginx

RUN mkdir /static

WORKDIR /static

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./auth /usr/share/nginx/html/auth
COPY ./tracker /usr/share/nginx/html/tracker

CMD ["nginx", "-g", "daemon off;"]
