choice = 1

while choice == 1:
    print("=======================Calculator========================")

    salary = input("Enter your full salary (per month) :")

    if float(salary) <= 1000:
        taxing = float(salary) * (5 / 100)

        currentsalary = float(salary) - taxing

        print(
            "\nSalary :",
            salary,
            "\nTaxing :",
            taxing,
            "\nClear salary :",
            currentsalary,
        )

    elif float(salary) > 1000 or float(salary) < 5000:
        taxing = int(salary) * (10 / 100)

        currentsalary = float(salary) - taxing

        print(
            "\nSalary :",
            salary,
            "\nTaxing :",
            taxing,
            "\nClear salary :",
            currentsalary,
        )

    elif float(salary) > float(5000):
        taxing = float(salary) * (15 / 100)

        currentsalary = float(salary) - taxing

        print(
            "\nSalary :",
            salary,
            "\nTaxing :",
            taxing,
            "\nClear salary :",
            currentsalary,
        )
