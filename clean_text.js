
const readline =  require("readline");
const fs =   require("fs");
const path =  require("path");
const events = require('events')
const process = require('process')

const readStream = fs.createReadStream(path.join(__dirname, process.argv[2].toString()));
const writeStream = fs.createWriteStream(path.join(__dirname, process.argv[3].toString()), {flags: "w+", mode: 0o777,})

const rl = readline.createInterface({
    input: readStream,
    crlfDelay: Infinity
});

let index  = 0;

rl.on('line', function(line){
    if(line != "") {
        line.split(".").forEach(data => {
            if(data != ''){
                if(!data.startsWith("#") || !data.startsWith("http") || !data.startsWith("https"))  writeStream.write(`${line}\n\n`)
            }
        })
    }
    index++;
});

(async ()=>{
    await events.once(rl, "close");
})()

