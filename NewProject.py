def start():
    user_coin = input('Hello, write the coin you want to convert !(dollar/shekel)')
    user_coin = user_coin.replace(" ", "")
    convert_to = input('What coin do you want to convert to ? (dollar/shekel)')
    convert_to = convert_to.replace(" ", "")
    while user_coin == convert_to:
        print("same coin error")
        convert_to = input('Write again')

    number = input(f'how much {user_coin} do you want to convert?')
    Yuval = amount(user_coin, convert_to, int(number))
    print(Yuval)


def amount(user_coin: str, convert_to: str, number: int) -> str:
    try:
        result = 0
        if user_coin == "dollar":
            result = number / 3.42
            return f"you have {result} {convert_to}"
        if user_coin == "shekel":
            result = number * 3.42
            return f"you have{result} {convert_to}"
    except Exception as e:
        print(e)




def main():
    start()


if __name__ == '__main__':
    main()
