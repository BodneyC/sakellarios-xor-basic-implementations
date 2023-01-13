# Ben's Extra Notes

These are really just some picky extra notes, the core of the notes are in Python and Node implementations

## Resources

This one's more about duplication of resources, each implementation directory has a copy of `cypherkey.txt` and `input.txt` - if each project were its own repo and this was more of an aggregate repo of submodules, then that makes sense. But as it is, it's just duplication, I'd just have a `resources` directory

A practical reason to do this might be if you wanted to write some unit test to assure that all implementations output the same thing, well if you change `input.txt` in 2/3 directories, then suddenly your test(s) will start failing

Not only does it keep the workspace clean, but if you want to test ten inputs of nine edge-cases plus a simple example, then having ten `.txt` files in each directory is messy 

### Encoded.txt

Each program expects an output file and your READMEs suggest naming that `encoded.txt`, so someone that clones and tries out the suggested commands will immediately have cleaning work to do if they wish to contribute (very simple cleaning work but cleaning work none-the-less)

It might be worth chucking a `*/encoded.txt` in your `.gitignore`

## Formatting

One thing that's common is a lack of formatting standards/tooling which helps with readability, maintainability, particularly when dealing with multiple contributors

All three languages have strong community opinions on linting and formatting:

- JS, `eslint` + `prettier`
- Python, `pylint` + `black` (/`autopep8`)
- Ruby, RuboCop (both)
