const path = require('path');
const fs = require('fs');

console.log(path.basename(__filename));
console.log(path.extname(__filename));
console.log(path.dirname(__filename));
console.log(path.parse(__filename));
console.log(path.join(__dirname,'/text','hello.txt'));

fs.mkdir(path.join(__dirname, '/text'), {}, function(err){
   if(err) throw err;
 });
//Asynchronous function writeFile AND appendFile.
fs.writeFile(path.join(__dirname, '/text','logs.txt'), 'This is complete junk', function(err){
      if(err) throw err;
      console.log('File written to....');
      fs.appendFile(path.join(__dirname, '/text','logs.txt'), 'NODE_JS is a non-blocking framework that runs on a single js thread.', function(err){
         if(err) throw err;
         console.log('appended to....'); 
         fs.readFile(path.join(__dirname,'/text','logs.txt'),'utf8',function(err,data){
            if(err) throw err;
            console.log('File read successfully');
            console.log('The content of the file is:',data);
            fs.rename(path.join(__dirname,'/text','logs.txt'),path.join(__dirname,'/text','lol.txt'),function(err){
                if(err) throw err;
                console.log('File renamed successfully');
                //console.log('The content of the file is:',data);
            });
            
        });
    });
});


