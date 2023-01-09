def xor_encrypt()
    # Check if the correct number of arguments was provided
    if ARGV.length < 2
        puts "Usage: ruby xor_encrypt.rb [input file] [output file] [key]"
        exit
    end
    
    # Get the input, output, and key from the command line arguments
    input_file = ARGV[0]
    output_file = ARGV[1]
    key = ARGV[2]


    # If no key was provided, read it from the default file
    if key == nil
        key_file = File.open('cypherkey.txt', 'r')
        key = key_file.gets
        key_file.close
    end

    # Convert the key string to an array of bytes
    key_bytes = key.bytes
        
    # Open the input and output files
    input = File.open(input_file, 'rb')
    output = File.open(output_file, 'wb')

    # Read the input file one byte at a time
    input.each_byte.with_index do |byte, i|
    # XOR the byte with the corresponding key byte and write it to the output file
    output.putc(byte ^ key_bytes[i % key_bytes.length])
    end

    # Close the input and output files
    input.close
    output.close

    print "\n\x1b[32mFile \x1b[33m#{input_file} \x1b[32mhas been encrypted using the #{ARGV[2] != nil ? "custom encryption key provided": "default key"} #{ARGV[2] != nil ? "\n":"\n\n"}"
    if ARGV[2] != nil
        print "The encryption key used is \x1b[31m#{key}. \x1b[32mPlease ensure that you keep a record of it for future use\n\n"
    end
    
end
  
# Call the XOR encryption function
xor_encrypt()

