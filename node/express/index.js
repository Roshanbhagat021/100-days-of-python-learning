const  express  = require("express")
const fs = require("fs")
app = express()

app.get("/",(req,res)=>{
    res.send("Hello this is my first express server")
})

app.get("/data",(req,res)=>{
    data = fs.readFile("./db.json","utf-8",(err, data)=>{
        
    })
    console.log(data)

})

app.listen(8080,()=>{
    console.log("The serer is runnig on 8080");
})