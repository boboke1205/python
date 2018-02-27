from Calculator import Calculator

cal = Calculator()



while True:
    print "wellcome!!"
    print "Select number"
    print "1. Set data"
    print "2. Plus"
    print "3. Minus"
    print "4. Multiply"
    print "5. divide"
    inputData = input("Select Menu :")

    if inputData == 1:
        value1 = input("value 1 :")
        value2 = input("value 2 :")
        cal.setData(value1, value2)
        continue

    elif inputData == 2:
        print cal.Plus()
        continue

    elif inputData == 3:
        print cal.Minus()
        continue


    elif inputData == 4:
        print cal.Multiply()
        continue

    elif inputData == 5:
        print cal.Divide()
        continue

    else:
        print "You've got the wrong number"
        continue

