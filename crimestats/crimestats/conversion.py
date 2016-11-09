from year.models import Years
import re


def years_into_db():
    """Put first data set into db."""
    ifile = open('/Users/David/Desktop/stats.txt', 'r')

    pages = []
    for i in ifile:
        pages.append(i)

    def check_alpha(s):
        if re.search('[a-zA-Z]', s):
            return False
        return True

    for i in pages:
        s = i.split()
        print(s)
        if len(s) == 12 and check_alpha(s[0]):
            new_year = Years(year=s[0], population=s[1], total=s[2],
                                        violent=s[3], prop=s[4], murder=s[5],
                                        rape=s[6], robbery=s[7], assault=s[8],
                                        burglary=s[9], theft=s[10], gta=s[11])
            new_year.save()
        else:
            print(i)

    ifile.close()
