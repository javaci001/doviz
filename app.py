# python -m pip install beautifulsoup4
# pip install flask
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template
import socket


def dovizkuru():
    url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
    try:
        page = requests.get(url)
        htmlPage = BeautifulSoup(page.content,"html.parser")
        #print(htmlPage.prettify())
        actualvalue = htmlPage.find("span",class_="sym__price" ).getText()
        print(actualvalue)
    except:
        print("bir hata olustu")
    return actualvalue

def ipadres():
    return socket.gethostbyname(socket.gethostname())

app = Flask(__name__,template_folder="./templates")

@app.route("/")
def index():
    dolar_kuru= dovizkuru()
    ip_adresi = ipadres()
    doviz_kurlari = {"DOLAR : " ,dolar_kuru}
    return render_template("index.html" , doviz_kurlari = doviz_kurlari , ip_adresi = ip_adresi)

if __name__ == "__main__":
    app.run(debug=True , port=5555)




