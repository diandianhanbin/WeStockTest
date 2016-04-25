class strtest:  
    def __init__(self):  
        print "init: this is only test"  
    def __str__(self):  
        return "str: this is only test"  
  
if __name__ == "__main__":  
    st=strtest()  
    print st  