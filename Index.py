from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def getIndexURL(url):
    return url.split('.com')[0] + '.com/'

def Download(url):
    try:
        content = requests.get(url).content
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a')

        __i__ = 0
        for link in links:
            link = link['href']

            if not 'http' in link and not 'https' in link and not 'javascript:void(0)' in link and not '#' in link:
                true_link = link

                if '/' in true_link:
                    soup = BeautifulSoup(requests.get(getIndexURL(url)).content, 'html.parser')

                # writing in file
                file_name = '{}.{}'.format(__i__, true_link.replace('/','.'))
                file = open(file_name, 'w', encoding = 'utf-8')
                file.write(soup.prettify())
                file.close()
                print(file_name)
                __i__ += 1

        return True

    except Exception as e:
        messagebox.showinfo('Error', e)
        return False

window = Tk()
window.title("Source Code Downloader")
window.geometry('500x300+500+200')

label1 = Label(window, text="Copy and Paste URL.\n", font=("Arial Bold", 13))
label1.grid(column=1, row=1)

txt = Entry(window, width=60)
txt.grid(column=1, row=2)

message = StringVar()
message.set('load..')

result = Label(window, text='', font=("Arial", 13))
result.grid(column=1, row=4)

def download():
    url = txt.get()
    if (len(url) > 0):

        result.config(text = "Getting informations...Please Wait!..")

        if Download(url=url) == True:
            result.config(text="Downloaded Success.")
        else:
            result.config(text="")

    else:
        messagebox.showinfo('Error', 'Please enter something.')

btn = Button(window, text='Download', command=download)
btn.grid(column=3, row=2)

window.mainloop()


