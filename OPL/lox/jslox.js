


//process.argv gets the commandline arguments
function main(){
    //the splice takes everything important
    //it will include the "node" and "jslox.js" otherwise
    args= process.argv.splice(2);

    if (args.length > 1){
        System.out.println("Usage: jlox [script]");
    }
    else if (args.length == 1){
    //I have no idea if this is what he intends but this will run stuff
        runFile(args[0]);
    }
    else{
        runPrompt();
    }
}

function runFile(path){
    var exec = require('child_process').exec;
    exec(path);
}

function runPrompt(){
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

    var waitForUserInput = function() {
    rl.question("> ", function(input) {
        run(input);
        waitForUserInput();
    });
    }

    waitForUserInput();
}


function run(source){
    const tokens = source.split(" ");
    tokens.forEach(element => console.log(element));
}

main();
