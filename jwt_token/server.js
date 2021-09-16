const express = require('express');
const app =  express();
const crypt = require('crypto');
const jwt = require('jsonwebtoken');
require('dotenv').config();

posts = [
    {
        name: 'Rahul',
        title: 'Automation using selenium',
        tech: 'Python',
        Free: true 
    },
    {
        name: 'Deepak',
        title: 'Creating Regex engine',
        tech: 'Javascript',
        Free: false 
    }, 
    {
        name: 'Raj',
        title: 'User Authnentication',
        tech: 'Javascript/Nodejs',
        Free: false
    }
]

app.use(express.json());
app.get('/posts', authenticateToken, (request, response) => {
    response.json(posts.filter(post => post.name === request.user.name));
});
app.post('/login', (request, response) => {
    //Authenticate User
    const username = request.body.username;
    const user = { name: username };
    const accessToken = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET)
    response.json({ accessToken: accessToken});
});

function authenticateToken(request, response, next) {
    //Bearer token
    const authHeader = request.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if(token == null) return response.sendStatus(401);

    jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err,  user) => {
        if(err) return response.sendStatus(403);
        else{
            request.user = user;
            next();
        }
    });
}

app.listen(3000)