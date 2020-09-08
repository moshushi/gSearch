# This is a sample script that search in Google result of query 'сыр чай' and save link to file outfile.txt

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def googleSearch(query):
    st = search(query=query, tld='ru', lang='ru', num=10, stop=20, pause=2)
    return list(st)

def toFile(itemlist):
    with open("outfile.txt", "w") as outfile:
        outfile.write("\n".join(itemlist))


if __name__ == '__main__':
    # print(googleSearch('сыр чай'))
    toFile(googleSearch('сыр чай'))

