def no_dups(s):
    # Your code here
    _str = ""
    unq_words = {}

    ## If you Give me a Empty stirng ill Give you one back
    if len(s) == 0:
        return ""


    for i in s.split():
        if i not in unq_words:
            unq_words[i] = i
    
    for ind, val in enumerate(unq_words):
        _str +=  val

        if ind is not len(unq_words) - 1:
            _str +=  " "
    
        print(f"_: {ind}\t _s: {len(unq_words)}")
        
    return _str


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))