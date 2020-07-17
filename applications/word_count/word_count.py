def word_count(s):
    # Your code here
    index = {}

    # ignore Casing..
    s = s.lower()

    # Grab all Punctuation Chars
    punctuations = '''":;,.-+=/\\|[]{}()*^&'''
    
    # add a temp string
    _s = ""
    
    # look through all chars in the string
    for char in s:
        # as long as the char doesnt exist in our punctuations
        if char not in punctuations:
            # we can add it to our temp _stripped string
            _s = _s + char
        
    words = _s.split()

    for word in words:
        if word not in index:
            index[word] = 0

        index[word] += 1
        # for i in range(1, len(words)):
        #     cache[words[i]] 

    return index


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))