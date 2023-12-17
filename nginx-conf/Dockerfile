FROM nginx:alpine

COPY ./nginx-conf/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443

ENTRYPOINT ["nginx", "-g", "daemon off;"]
