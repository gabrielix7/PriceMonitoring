import threading # necesar pentru folosirea thread-urile de la finalul programului
import time # necesar pentru folosirea time.sleep(nr. secunde), se face o pauză de n secunde
import datetime # necesar pentru accesarea datei curente
import urllib.request # necesat pentru accesarea site-ului dorit
from bs4 import BeautifulSoup # necesar pentru accesarea datelor site-ului și extragerea acestora
import re # necesar pentru formatarea un string-uri
import matplotlib.pyplot as plt # necesar pentru plotare

# declararea unor string-uri care conțin site-urile ”mamă”, cu ajutorul cărora se va face identificarea site-urilor

myString1 = "https://mediagalaxy.ro/" 

myString2 = "https://carrefour.ro/"

myString3 = "https://altex.ro/"

# definim o funcție cu ajutorul căreia accesăm site-ul și căutăm datele necesare programului nostru

def makeSoup(url):

    thePage = urllib.request.urlopen(url) # ne conectăm la site

    soupData = BeautifulSoup(thePage, 'html.parser') # putem naviga pe site și putem căuta datele HTML de care avem nevoie

    return soupData

# definim o funcție care v-a deschide fișierul în care se vor da link-urile produselor, va identifica pentru fiecare site-ul ”mamă” din care face parte și va aplica metodele pentru extragerea titlului, prețului, va inregistra data la care sunt extrase, va crea un fișier cu numele link-ului produsului și va salva acolo datele necesare în următoarea partea a programului 

def myProgram():

    # fișierul cu link-uri trebuie creat

    fileOpen = open('linkuri.txt', "r") # deschidem fișierul în care avem salvate link-urile produselor

    while True:

        myLinks = fileOpen.readline() # se citește fiecare linie din fișierul cu link-uri


        if myLinks.find(myString1, 0, len(myLinks)) == 0: # se face identificarea site-ului, funcția find caută string-ul în link-ul extras din fișier

            # print("for  MediaGalaxy:")

            soup = makeSoup(myLinks) # link-ului identificat i se aplică funcția makeSoup, conectându-ne la site pentru a putea accesa datele HTML

            # pentru title, price și link, atributele (attrs={'clasă': 'valoare'}) regăsite în fiecare site sunt diferite și trebuie modificare în cazul în care utilizatorul dorește să folosească alte site-uri

            title = soup.find(attrs={'class': 'font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0'}) # extragem titlul, se face căutarea acestuia pe baza atributului specific în site   
           
            price = soup.find(attrs={'class': 'Price-int'}) # extragem prețul, se face căutarea acestuia pe baza atributului specific în site

            link = soup.find(attrs={'rel': 'canonical'}) # extragem adresa link-ului, se face căutarea acestuia pe baza atributului specific în site

            href = link.get('href') # extragem link-ul produsului

            dateToday = datetime.datetime.now() # data curentă, la care se extrag datele produsului

            currentData = str(dateToday.day) + '/' + str(dateToday.month) + ' ' + str(dateToday.hour) + ':' + str(dateToday.minute) + ':' + str(dateToday.second) # formatarea datei curente

#             print(title.text, '\n', price.text, ' Lei' '\n', currentData, '\n', href, '\n')

            newHref = re.sub('\W+', '', href) # pentru a putea crea un fișier cu numele link-ului produsului, din acesta trebuie extrase caracterele speciale

            siteFile = open(newHref+'.txt', 'a') # se creează un fișier având ca și nume link-ul produsului și se deschide fișierul în modul append

            siteFile.write(price.text + "\n") # se scrie în fișier prețul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.write(str(currentData) + "\n") # se scrie în fișier data curentă, '\n' realizează trecerea pe rândul următor

            siteFile.write(title.text + "\n"*2) # se scrie în fișier titlul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.close() # închidem fișierul în care s-au scris datele

        elif myLinks.find(myString2, 0, len(myLinks)) == 0: # se face identificarea site-ului, funcția find caută string-ul în link-ul extras din fișier

#             print("for Carrefour:")

            soup = makeSoup(myLinks) # link-ului identificat i se aplică funcția makeSoup, conectându-ne la site pentru a putea accesa datele HTML

            title = soup.find(attrs={'class':'base'}) # extragem titlul, se face căutarea acestuia pe baza atributului specific în site

            price = soup.find(attrs={'class':'price'}) # extragem prețul, se face căutarea acestuia pe baza atributului specific în site

            link = soup.find(attrs={'rel':'canonical'}) # extragem adresa link-ului, se face căutarea acestuia pe baza atributului specific în site

            href = link.get('href') # extragem link-ul produsului

            dateToday = datetime.datetime.now() # data curentă, la care se extrag datele produsului

            currentData = str(dateToday.day) + '/' + str(dateToday.month) + ' ' + str(dateToday.hour) + ':' + str(dateToday.minute) + ':' + str(dateToday.second) # formatarea datei curente

#             print(title.text, '\n', price.text, '\n', currentData, '\n', href, '\n') 

            newHref = re.sub('\W+','', href) # pentru a putea crea un fișier cu numele link-ului produsului, din acesta trebuie extrase caracterele speciale

            siteFile = open(newHref+'.txt', 'a') # se creează un fișier având ca și nume link-ul produsului și se deschide fișierul în modul append

            siteFile.write(price.text + "\n") # se scrie în fișier prețul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.write(str(currentData) + "\n") # se scrie în fișier data curentă, '\n' realizează trecerea pe rândul următor

            siteFile.write(title.text + "\n"*2) # se scrie în fișier titlul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.close() # închidem fișierul în care s-au scris datele

        elif myLinks.find(myString3, 0, len(myLinks)) == 0: # se face identificarea site-ului, funcția find caută string-ul în link-ul extras din fișier

#             print("for Altex:")     
 
            soup = makeSoup(myLinks)  # link-ului identificat i se aplică funcția makeSoup, conectându-ne la site pentru a putea accesa datele HTML

            title = soup.find(attrs={'class':'font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0'}) # extragem titlul, se face căutarea acestuia pe baza atributului specific în site
            
            price = soup.find(attrs={'class':'Price-int'}) # extragem prețul, se face căutarea acestuia pe baza atributului specific în site

            link = soup.find(attrs={'rel':'canonical'}) # extragem adresa link-ului, se face căutarea acestuia pe baza atributului specific în site

            href = link.get('href') # extragem link-ul produsului

            dateToday = datetime.datetime.now() # data curentă, la care se extrag datele produsului

            currentData = str(dateToday.day) + '/' + str(dateToday.month) + ' ' + str(dateToday.hour) + ':' + str(dateToday.minute) + ':' + str(dateToday.second) # formatarea datei curente

#             print(title.text, '\n', price.text, ' Lei' '\n', currentData, '\n',  href, '\n') 

            newHref = re.sub('\W+','', href) # pentru a putea crea un fișier cu numele link-ului produsului, din acesta trebuie extrase caracterele speciale

            siteFile = open(newHref+'.txt', 'a') # se creează un fișier având ca și nume link-ul produsului și se deschide fișierul în modul append

            siteFile.write(price.text + "\n") # se scrie în fișier prețul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.write(str(currentData) + "\n") # se scrie în fișier data curentă, '\n' realizează trecerea pe rândul următor

            siteFile.write(title.text + "\n"*2) # se scrie în fișier titlul produsului, '\n' realizează trecerea pe rândul următor

            siteFile.close() # închidem fișierul în care s-au scris datele

        time.sleep(5) # după fiecare buclă, funcția face o pauză de 5 (se poate modifica această valoare) secunde până la începerea următoarei
        
# definim o funcție care va primi ca parametru unul sau mai multe link-uri de la tastatură, va citi datele produsului din fișier și va face grafic cu acestea; graficul se va salva automat

def myClient():

    myList=[] # definim o listă goală în care vom înregistra link-urile introduse de la tastatură

    maxSite = int(input()) # se va seta o limită pentru câte site-uri se pot introduce de la tastatură

    for i in range(0, maxSite):

        myCall = input() # introducem de la tastatură link-ul/-urile dorite

        myList.append(myCall) # se realizează adăugarea link-ului/-urilor în lista noastră â

    # cu ajutorul următoarelor patru instrucțiuni se realizează ”curățarea” de caractere speciale a link-urilor din listă

    myList = ' '.join(myList).replace(':','').split()

    myList = ' '.join(myList).replace('/','').split()

    myList = ' '.join(myList).replace('.','').split()

    myList = ' '.join(myList).replace('-','').split()

    # print(myList)

    for i in range(len(myList)):

        myFile = open(myList[i]+'.txt', 'r') # deschidem fișierul în modul read în care se găsesc datele produsului; numele fiind constituit din elementul de pe poziția i din lista nostră plus extensia .txt

        reader = myFile.readlines() # citim elementele din fișierul nostru

        # instrucțiunea folosită va returna o listă deci va trebui să extragem fiecare elemente din aceasta și mai departe să fie introdus într-alta specifică

        priceList = [reader[i] for i in range(0, len(reader), 4)] # se face extragerea prețului din lista ”reader” și introducerea în noua listă priceList

        fullDataList = [reader[i] for i in range(1, len(reader), 4)] # se face extragerea datei din lista ”reader” și introducerea în noua listă fullDataList

        priceList = ' '.join(priceList).replace('Lei\n', '').split() # se va face formatarea prețului deoarece când acesta este extras din listă va fi urmat de ”\n” sau când este extras din site poate fi urmat de orice altceva ( cazul de față moneda - Lei)

        fullDataList = ' '.join(fullDataList).replace('\n', '').split() # se va face formatarea datei deoarece când acesta este extrasă din listă va fi urmată de ”\n”
 
        # fullDataList este o listă în care data este împărțită în următorul fel: pe o poziție YYYY:MM:DD, iar pe următoarea HH:MM:SS; trebuie să extragem aceste două elemente în două liste, iar mai apoi introduse într-o nouă listă care să conțină pe fiecare poziție înregistrări ale datei în următorul format YYYY:MM:DD (spațiu) HH:MM:SS (acesta fiind formatul standard, am optat pentru formatul DD/MM HH:MM:SS)
        
        hourList = [fullDataList[i] for i in range(1, len(fullDataList), 2)] # se face extragerea HH:MM:SS
        

        dataList = [fullDataList[i] for i in range(0, len(fullDataList), 2)] # se face extragerea YYYY:MM:DD

        newDataList = [i + ' ' + j for i, j in zip(dataList, hourList)] # fuziunea celor două liste astfel încât să obținem formatul dorit al datei

        # print(priceList, '\n'*2, hourList, '\n'*2, dataList, '\n'*2, newDataList)

        myFile.close() # închidem fișierul din care s-a realizat citirea

        plt.plot_date(newDataList, priceList) # plotarea celor două liste

        plt.xlabel('Time: ') # denumirea axei x

        plt.ylabel('Price: lei') # denumirea axei y

        plt.title('Price monitoring') # denumirea titlului

        plt.grid(color='blue', linestyle='-', linewidth=0.25, alpha=0.5) # aplicarea unui grid care poate fi personalizat

        # plt.savefig('plot'+str(i)+'.png') 

    plt.savefig('plot.png') # salvarea automată a plotului

    plt.show() # afișarea plotului

firstThread = threading.Thread(target=myProgram, daemon=True)

secondThread = threading.Thread(target=myClient)

firstThread.start() # începe primul thread 

secondThread.start() # începe al doilea thread

firstThread.join(5.0) # așteaptă până se termină execuția primului thread (având un loop care rulează la infinit, se poate seta un nr de secunde după care acesta își poate înceta rularea)

secondThread.join() # așteaptă până se termină excuția celui de-al doilea thread

print("Asta a fost!")
