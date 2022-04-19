import traceback
import logging


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


def switch_lights(stoplight):
    assert 'red' in stoplight.values(), 'red signal is required'
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'


def traffic_light_simulation():
    # dicts are streets name; ns - north-south, ew - east, west
    market_2nd = {'ns': 'green', 'ew': 'red'}
    mission_16th = {'ns': 'red', 'ew': 'green'}
    print(market_2nd, mission_16th)
    switch_lights(market_2nd)
    switch_lights(mission_16th)
    print(market_2nd, mission_16th)


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='program-log.txt')
# Using logging instead print function very convinient. Disable all debuging code with one line.
# logging.disable(logging.CRITICAL)

def factorial(n):
    logging.debug('Factorial start(%s%%).' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))
    logging.debug('Factorial end(%s%%).' % (n))
    return total


def test_logging():
    print(factorial(5))
    logging.debug('Program end.')


def main():
    test_logging()
        

if __name__ == '__main__':
    main()