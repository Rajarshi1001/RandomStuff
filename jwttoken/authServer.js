const express = require('express');
const app =  express();
const crypt = require('crypto');
const jwt = require('jsonwebtoken');
require('dotenv').config();

app.use(express.json());

//list of all refreshtokens
var refreshtokens = [];


app.post('/token', (request, response) => {
    const refreshToken = request.body.token;
    if (refreshtokens.length === 0) return response.sendStatus(403);
    if (refreshToken == null) return response.sendStatus(401);
    if (!refreshtokens.includes(refreshToken)) return response.sendStatus(403);
    jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET, (err, user) => {
        if(err) return response.sendStatus(403);
        const accessToken = generateAccessToken({ name: user.name });
        response.json({ accessToken: accessToken });
    });
});

app.post('/logout', (request, response) => {
    refreshtokens.pop(request.body.token);
    // console.log(refreshtokens);
    response.sendStatus(204);
});


app.post('/login', (request, response) => {
    //Authenticate User
    const username = request.body.username;
    const user = { name: username };
    const accessToken = generateAccessToken(user);
    const refreshToken = jwt.sign(user, process.env.REFRESH_TOKEN_SECRET);
    refreshtokens.push(refreshToken);
    console.log(refreshtokens)
    response.json({ accessToken: accessToken, refreshToken: refreshToken });
});

function generateAccessToken(user){
    return jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, { expiresIn: '20s'});
}

app.listen(5000)