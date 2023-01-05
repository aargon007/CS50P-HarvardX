def main():
    #output using convert function
    x=input()
    print(convert(x))

def convert(x):
    x=x.replace(":)", "🙂")
    x=x.replace(":(", "🙁")
    return x

main()