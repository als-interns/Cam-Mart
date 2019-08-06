FROM node

#vue

WORKDIR /app

COPY package*.json ./

RUN npm cache verify

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]