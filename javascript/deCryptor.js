// BEN: Suuuuuuuper picky one that I would 100% ignore would be the directory 
//  name of `javascript` - so much of the JS is using the FS API that I would 
//  call it node
// 
// If there was more of that composition mentioned in the Python 
//  implementation and the use of `fs` was in a little `parseArgs()` function, 
//  then yeah, the XOR bit is 100% Javascript, but as it's one block the file is 100% Node.
import fs from 'fs'

function encryptDecrypt(){

// BEN: I'm generally not a fan of `try{}catch{}` statements, if you have a 
//  very predictable error that happens on one or two lines and there's no way 
//  to execute the code safely, then yes they can make sense
// 
// There can be some debate on the performance costs of these statements 
//  (particularly in the `catch` clause) but that's not a concern here
//  
// The concern is that the whole program is wrapped in a try-catch. Two of 
//  three cases of the switch are concerned with file IO, one of them provides 
//  no further context, and the third may give a message but if it were a 
//  generic error (NPE or indexing) then the line number is lost. Which 
//  statement failed?
// 
// Wrapping big chunks regularly can, in my opinion, become an anti-pattern, 
//  particularly when you call functions which themselves are wrapped, you can 
//  end up masking the true nature of the error quite easily or doing the 
//  opposite and adding a little message each time forming a largely useless 
//  "stack trace" of your own design
// 
// There is then the fact that it's another indent level (or it would with 
//  any formatter) for the entire code base, not the worst thing but it can 
//  seem disorganised - perhaps in this case, wrapping the last line, the call 
//  to `encryptDecrypt()` would have been cleaner
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
