## JSON WEB TOKENS
___

This is a simple express app for demonstration of `json web tokens`.These tokens basically enables secure transmission of information between the client and server as Json object.The tokens are signed using `secret` or using a `public/private` key.These tokens contains information assciated with the authorised user and is sent back to the user by the server in the `Headers` section of the request.

This application has routes: 

* `__/login__` : this route creates a accesstoken and refresh token assicated with a particular user present in the posts list in `server.js`,the access token expires within every 15s so the refresh token is used to generate a new accesstoken.

* `__/posts__`: this routes accepts the accesstoken in the Bearer section to display the post associated with that particular user.

* `__/token__`: this route is used to generate a new `accesstoken` with the `refreshtoken` of the previous accesstoken since accesstoken expires every `15s`.

* `__/logout__`: this route is used to remove authentication of the user form the server by deleting the refreshtokens from the server.

I have used a simple list to store the refreshtokens instead of a database.

The authentication of the tokens are executed on `localhost:5000`
The post retrieval (`get request`) is executed on `localhost:3000` 

All the dependencies are stored in `package.json` file.

The relevant `npm dependencies` include:
- jsonwebtoken
- express
- dotenv
- crypto
- nodemon

To install the dependencies, run the following command in the terminal:
```
npm install
```
To start the servers, run the following commands in two seperate terminals:
```
npm run devStart
npm run devStart2
```
I have used the Rest Client extension in VSCode for passing on multiple http requests to the endpoints.
The requests are present in the `response.rest` file.
