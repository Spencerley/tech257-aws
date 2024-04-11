#!/bin/bash 

export DB_HOST=mongodb://172.31.48.79:27017/posts

cd tech257-sparta-app/app

node seeds/seed.js

# npm -
npm install

# stop pm2 -
pm2 kill

# run pm2 -
pm2 start app.js