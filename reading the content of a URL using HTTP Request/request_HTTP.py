import requests

Specific_website = input("Enter web site: ");
#http://www.google.com/

#A site experiment I have designed for the IoT path that links to databases
#http://localhost/Task_php_mysql/response_without_html.php
web_site = requests.get(Specific_website)

#check status code

try:
    if web_site.status_code == 200:
        print("The request is OK,200")

    if web_site.status_code == 301:
        print("The requested page has moved to a new url ,ERROR 301")

    if web_site.status_code == 404:
        print("The server can not find the requested page,ERROR 404")

    if web_site.status_code == 505:
        print("The server does not support the http protocol version,ERROR 505")

except:
    print("HTTP error" ,web_site.status_code)


print('\n  \n \n')

#Print the contents of the page
print(web_site.text)