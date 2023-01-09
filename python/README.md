# deCryptor

This is the simplest possible Javascript program to encrypt files using XOR cypher.

In order to use following command:

    python3 deCryptor.js <FILE_TO_ENCRYPT_DECRYPT> <OUTPUT_FILE> [KEY]

Please note that the KEY parameter is optional. If it is not provided, then the default cypherkey from file **_cypherkey.txt_** will be used

## Examples of commands:

### To encode:

- with a custom key

        python3 deCryptor.js input.txt encoded.txt  testytytuytytuy

- with default key:

        python3 deCryptor.js input.txt encoded.txt

### To decode:

    Just ensure you use the same encryption key used and reverse the order of the files.
