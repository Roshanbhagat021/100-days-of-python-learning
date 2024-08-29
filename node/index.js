const fs = require("fs")



const data = fs.readFileSync('./name.txt',{ encoding: 'utf8'})
console.log(data)



fs.writeFileSync("text.txt","Learning node js",(err)=>{
    console.log(err)
})

let data2 = {
    name: "Roshan",
    age: 20
}

fs.writeFileSync("db.json",JSON.stringify(data2),(err)=>{
    console.log(err);
})