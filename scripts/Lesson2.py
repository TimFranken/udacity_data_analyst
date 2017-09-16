import pandas as pd


def footbal_stats():
    data = pd.read_csv(r'D:\Udacity\data\2015-16-premier-league.csv')
    print(data[['Wins']].mean())
    print(data[['Wins']].median())
    print(round(data[['Wins']].std(ddof=0), 4))
    aa = data[['Wins']].describe()
    print(aa.loc['75%'] - aa.loc['25%'])


def most_frequent(s):
    """Return the most frequently occurring word in s."""

    words = s.split(' ')
    sorted(words)
    un_words = set(words)

    count_words = []

    for x in un_words:
        count_words.append(words.count(x))

    ind = count_words.index(max(count_words))

    return list(un_words)[ind]


def which_date(start_date, time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """

    import datetime

    date = datetime.datetime.strptime(start_date, '%Y/%m/%d')
    delta = time.split(' ')

    if delta[1] == 'days':
        return datetime.datetime.strftime(date + datetime.timedelta(days=int(delta[0])), '%Y/%m/%d')
    else:
        return datetime.datetime.strftime(date + datetime.timedelta(days=int(delta[0])*7), '%Y/%m/%d')


def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10', '35 days') == '2016/03/16'
    assert which_date('2016/12/21', '3 weeks') == '2017/01/11'
    assert which_date('2015/01/17', '1 week') == '2015/01/24'
    print("All tests completed.")


test()
