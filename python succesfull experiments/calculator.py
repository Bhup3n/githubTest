resume = True
while resume:
    num1 = float(input("what is a number you would like to use:"))
    operation = input("\nwhat operation do you want to use,:\n+ or - or * or / or ^ or %:")
    if operation == "^":
        x = float(input("what power would you like to raise it to:"))
        ans = num1 ** x
        print(ans)
    else:
        num2 = float(input("\nwhat is another number you want to use:"))
        if operation == "+":
            ans = num1 + num2
            print(ans)
        elif operation == "%":
            ans = num1 * num2 / 100
            print(ans)
        elif operation == "-":
            ans = num1 - num2
            print(ans)
        elif operation == "*":
            ans = num1 * num2
            print(ans)
        else:
            ans = num1 / num2
            print(ans)

    more = input("\nwould you like to continue to use the calculator, yes or no:")
    if more == "no":
        resume = False
    else:
        use_ans = input("would you like to use the previous answer as one of your numbers, yes or no:")
        if use_ans == "yes":
            where_ans = input("do you want to use your previous answer as your first or second number:")
            if where_ans == "first":
                num1 = ans
            else:
                num2 = ans