import traceback


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol variable should be single symbol string')
    if width <= 2:
        raise Exception('width value should be more than 2')
    if height <= 2:
        raise Exception('height value should be more than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


def test_boxPrint():
    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
        try:
            boxPrint(sym, w, h)
        except Exception as err:
            print('While procesing erorr occured: ' + str(err))


def test_traceback():
    try:
        raise Exception('Error message')
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('Stack info was been wrote in file errorInfo.txt')


def main():
    test_traceback()
        

if __name__ == '__main__':
    main()