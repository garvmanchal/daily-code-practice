with open("poem.txt") as f:
    content = f.read()
    if "twinkle" in content :
        print("twinkle is present")
    else :
        print("not present")
