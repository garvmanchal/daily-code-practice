def myFunc():
    print("hello world")


if __name__ == "__main__":
    # if this code is directly executing by running the file its present in
    print("We are directly runnig this code")
    myFunc()
    print(__name__) # this will tell the current module