# [Debugging Techniques](https://www.youtube.com/watch?v=04paHt9xG9U&feature=emb_rel_pause)

## Basic Methods

   1. Read the error messages
   2. Insert `print()` statements 
   3. Make an hypothesis; what is the problem; what is the reason for the error
   4. Rubber duck technique; talk to a duck or yourself explaining what the code is doing
   5. Cleap-up the code
   6. Use `assert` frequently
    
## Advanced Methods
   7. Use pdb/ipdb ([documentation](https://docs.python.org/3/library/pdb.html)). Useful pdb commands: `l, n, s, b, c, q` 
   8. Use smaller version of the input file to test the code
   9. logging ([documentation](https://docs.python.org/3/howto/logging.html))
   
    
Other debugging strategies
- try-except
- count
- tests
- linter (pylint/pyflakes)
- restart kernel
- bisection