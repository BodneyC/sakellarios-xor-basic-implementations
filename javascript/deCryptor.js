import fs from 'fs'

function encryptDecrypt(){

try {

    // ==============  READ FILES ======================
    let args = process.argv.slice(2)
    if(args.length < 2) {
        console.log("\n\x1B[31mThis function needs at least two arguments, one input file and one output file.\n")
        return
    }
    let input = fs.readFileSync(args[0], 'utf8')
    let cypherkey = args[2] ? args[2] : fs.readFileSync('cypherkey.txt', 'utf8')
    

    
    // ==============  OUTPUT FILE ======================
    let output = [];
    
    // ==============  ENCRYPT/DECRYPT ======================
    for (let i = 0; i < input.length ; i++) {
        // XOR each character of the input with the cypherkey
        // modulo is used to normalise the output of the division (a popular use of modulo 
        // in Hash functions)  
        let char = input.charCodeAt(i)  ^ cypherkey[i % cypherkey.length].charCodeAt(0)
        output.push(String.fromCharCode(char))
    }
    const outputFinal = output.join("")
    
    fs.writeFileSync(`${args[1]}`, outputFinal, 'utf8');

    console.log(`\n\x1b[32mFile \x1b[33m${args[0]} \x1b[32mhas been encrypted using ${ args[2] ? "the custom encryption key provided"  : "the default encryption key in file \x1b[31mcypherkey.txt\n" }`)
    if(args[2]) console.log("The encryption key used is \x1b[31m%s. \x1b[32mPlease ensure that you keep a record of it for future use\n", args[2])


} catch (error) {
    console.error('\n\x1B[31mOoops something went wrong with your encoding/decoding');

    switch (error.code){
        case 'ENOENT':
            console.log('Please check that the following file exists: ' + '\x1b[33m%s\x1b[0m\n', error.path);
            break;
        case 'ERR_INVALID_ARG_TYPE':
            console.log('Please check that you have provided the correct arguments to the function');
            break;
        default:
            console.log("Not sure what, but so why don't you try again. %s \n", error.message);
    }


}
}

encryptDecrypt()