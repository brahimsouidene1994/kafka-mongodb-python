# https://programminghistorian.org/en/lessons/output-data-as-html-file
# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata and open in Firefox tab.
from bs4 import BeautifulSoup
from webbrowser import open as webopen
from selenium import webdriver

wrapper = """<html>
    <head>
    <title>Users list</title>
    </head>
    <body >
        <h1 style="text-align:center">Users of Apache Kafka</h1>
    </body>
    </html>"""


def delete_content_file(filename):
    open(filename, 'w').close()


def wrap_String_In_HTMLMac(filename, html):
    f = open(filename, 'w')
    f.write(html)
    f.close()


def render_file(filename):
    # Change the filepath variable below to match the location of your directory
    url = 'D:/MPDAM2/BigData-NoSql/kafka-tuto/kafka-project/' + filename
    webopen(url)


def page_refresher():
    driver = webdriver.Chrome("D:/MPDAM2/BigData-NoSql/kafka-tuto/kafka-project/index.html")
    driver.refresh()


def append_new_tag_file(data, position):
    print(data)
    with open("./index.html") as file:
        html_file = file.read()
        soup = BeautifulSoup(html_file, features="html.parser")
        head_tag = soup.find("div", {"class": position})
        div_tag = soup.new_tag('p')
        div_tag['class'] = "link"
        ch = ""
        for key, value in data.items():
            ch += key + ":" + value + " - "
        print(ch)
        div_tag.string = ch
        head_tag.insert(0, div_tag)
        print(soup)
        return soup  # This should print the new, modified html


def original_format():
    return """<html>
    <head>
    <title>Users list</title>
    </head>
    <body >
        <h1 style="text-align:center">Users of Apache Kafka</h1>
        <div style="display:flex; justify-content:space-arround">
            <div class="old-users" style="width: 100%; border-right:2px solid #000">
                <h2 style="text-align:center">Old users</h2>
                <div class="users-one"></div>
            </div>
            <div class="young-users" style="width: 100%">
                <h2 style="text-align:center">Young users</h2>
                <div class="users-two"></div>
            </div>
        </div>
    </body>
    </html>"""


if __name__ == "__main__":
    delete_content_file("index.html")
    wrap_String_In_HTMLMac('index.html', wrapper)
    i = 0
    while i < 10:
        # wrap_String_In_HTMLMac('index.html', str(append_new_tag_file()))
        i += 1
    render_file("index.html")
