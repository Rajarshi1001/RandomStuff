
//simple NODE_JS server using http core module.(without SSL encryption)

const http = require('http') //absolute path
const fs = require('fs');


const server = http.createServer(function(req, res) {
   //console.log(req.url, req.headers, req.method, req.rawHeaders);
   const url = req.url;
   const http_method= req.method;
   if(url === '/'){
    res.setHeader('Content-Type','text/html');
    res.write('<html>');
    res.write('<head><title>nodeJS server</title></head>');  
    res.write('<body><form action="/message" method="POST"><input type="text" name="message"><button type="submit">Submit</button></form></body>');
    res.write('</html>');
    return res.end;    
   }
   if(url ==='/message' && http_method === 'POST'){
       fs.appendFileSync('message.txt','Message Submitted\n');
       res.statusCode = 302; //statuscode for redirect
       res.setHeader('Location','/');
   }
   
   res.setHeader('Content-Type', 'text/html');
   res.write('<html>');
   res.write('<head><title>nodeJS server</title></head>');
   res.write('<body><p>hello folks this is a NodeJS server<p>');
            // res.write("<p>");
            // res.write(text);
            // res.write("</p>");   
   res.write("</body></html>");
   res.end();
});
server.listen(3000);