#echo.py

def echo(text:str, repetitions:int = 3) -> str:
    """Imitate a real world echo."""
    last3characters = text[-3:]
    print(last3characters)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

