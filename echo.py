#echo.py

#echo function that simulates an echo with the text and repetitions specified by the user
def echo(text:str, repetitions:int = 3) -> str:
    """Imitate a real world echo."""
    lastCharacters = text[-repetitions:]
    print(lastCharacters)
    for i in range(repetitions-1):
        print(lastCharacters[(-repetitions+1+i):])
    return "."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

