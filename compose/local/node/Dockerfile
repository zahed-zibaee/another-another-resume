FROM node:16-stretch-slim

WORKDIR /app

COPY ./package.json /app

RUN npm install && npm cache clean --force

ENV PATH ./node_modules/.bin/:$PATH
