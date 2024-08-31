

var http = require('http');

//create a server object:
const server = http.createServer(function (req, res) {
    if (req.url === "/"){
        res.write("This is our Home page")
    }else if (req.url === "./contact"){
        res.write("This is contact page")
    }else{
        res.write("About page")
    }
  
    res.end();
})

//the server object listens on port 8080
port = 3030
server.listen(port,()=>{
    console.log(`Listing on port ${port}`)
})