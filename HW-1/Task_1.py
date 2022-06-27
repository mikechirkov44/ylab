# Задача №1. Секция статьи "Задача №1."
# Написать метод domain_name, который вернет домен из url адреса:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"

url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"
url3 = "https://www.cnet.com"

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

print(domain_name(url1))
print(domain_name(url2))
print(domain_name(url3))



