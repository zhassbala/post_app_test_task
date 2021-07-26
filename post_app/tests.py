from dateutil.parser import parse as date_parse

if __name__ == '__main__':
    datestr = '2021-07-26 9:33'
    print(date_parse(datestr))
