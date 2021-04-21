from selenium import webdriver
from xpathlist import *
import time
import random


class Bot():

    def __init__(self, login, haslo):
        self.login = login
        self.haslo = haslo
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.instagram.com/")

    # Funkcje glowne

    def loginn(self):
        # klikanie cookie
        cookie = self.browser.find_element_by_xpath(xpathlist.cookie)
        cookie.click()
        time.sleep(3)

        # wpisywanie loginu
        pLogin = self.browser.find_element_by_xpath(xpathlist.pLogin)
        self.browser.execute_script("arguments[0].click();", pLogin)
        pLogin.send_keys(self.login)

        # wpisywanie hasla
        pPassword = self.browser.find_element_by_xpath(xpathlist.pPassword)
        self.browser.execute_script("arguments[0].click();", pPassword)
        pPassword.send_keys(self.haslo)

        # klikanie loguj
        submit = self.browser.find_element_by_xpath(xpathlist.submit)
        submit.click()
        time.sleep(3)

    def getFriends(self):
        # zczytywanie observacych konta
        self.allFoll = self.prefixToString(
            self.browser.find_element_by_xpath(xpathlist.allFollow).text)

        # wyswietlanie okna z obsami
        watched = self.browser.find_element_by_xpath(
            xpathlist.watchedWindow).click()
        time.sleep(2)

        # przewijanie i pobieranie nazw kont wszystkich obsow
        for i in range(int((self.allFoll)/300)):
            self.scrollWindow(20, "isgrP")
            time.sleep(random.randint(500, 1000)/1000)

        # przepisywanie nazw kont z listy na tablice
        friends = self.browser.find_elements_by_class_name('FPmhX')
        tab = []
        for y in range(len(friends)):
            tab.append(friends[y].text)
            print("index ", y, tab[y])
        return tab

    def checkingAccount(self):
        time.sleep(1)
        # pobieranie observacych i obserwowanych
        observacych = self.browser.find_element_by_xpath(
            xpathlist.follower).text
        obserwowani = self.browser.find_element_by_xpath(
            xpathlist.watched).text

        # usuwanie z observacych i obserwowanych odstepów i "tys." i "mln"
        observacych = self.prefixToString(observacych)
        print("Ilosc observacych: " + str(observacych))
        obserwowani = self.prefixToString(obserwowani)
        print("Ilosc obserwowanych: " + str(obserwowani))

        # podejmowanie decyzji o tym czy konto spelnia warunki
        if (observacych > 10 and observacych < obserwowani):
            return True
        else:
            return False

    def likePhoto(self):

        time.sleep(1)
        # sprawdzanie ilości postów
        numberPost = self.browser.find_element_by_xpath(
            xpathlist.numberPost).text
        numberPost = numberPost.replace(" ", "")
        print("Ilosc postow: " + numberPost)
        numberPost = int(numberPost)

        if(numberPost > 5):
            # sprawdzanie obecnosci story i klikanie zdjecia
            if(self.browser.find_elements_by_class_name("EcJQs")):
                chosePhoto = self.browser.find_element_by_xpath(
                    xpathlist.chosePhotoWithStory)
                chosePhoto.click()

            else:
                chosePhoto = self.browser.find_element_by_xpath(
                    xpathlist.chosePhotoWithoutStory)
                chosePhoto.click()
            time.sleep(3)

            # odnalezienie przesuwana w bok
            skipPhotoButton = self.browser.find_element_by_xpath(
                xpathlist.skipPhotoButton)

            # laikowanie 3 kolejnych zdjec
            for i in range(1, random.randint(3, 5)):
                time.sleep(0.5)
                heart = self.browser.find_element_by_xpath(
                    xpathlist.heartOne)
                time.sleep(1)
                heart.click()
                time.sleep(1)
                skipPhotoButton.click()
                time.sleep(1)

            time.sleep(2)
            heart = self.browser.find_element_by_xpath(xpathlist.heartOne)
            heart.click()

    def checkNotifications(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(2)

        # odrzucanie propozycji powiadomien
        notnow = self.browser.find_element_by_xpath(xpathlist.notNowButton)
        notnow.click()
        time.sleep(1)

        # klikanie gornego serduszka
        time.sleep(1)

        # self.scrollWindow(100, "_01UL2")
        self.browser.get('https://www.instagram.com/accounts/activity/')
        time.sleep(10)
        self.scroll()

        # wyciaganie tresci z powiadomien o obsach i laikach
        content = self.browser.find_elements_by_class_name("yrJyr")
        tab1 = []
        y = 0
        time.sleep(2)
        for y in range(len(content)):
            tab1.append(content[y].text)
         # przepisywanie do 2 tablicy usuwajac powtorzenia i sprawdzajac warunek
        tab2 = []
        for values in content:
            if (tab1.count(values.text) > 2 and not(values.text in tab2)):
                tab2.append(values.text)
        return tab2
    #
    #
    # Funkcje pomocnicze
    #
    #

    def chooseAccount(self, account):
        accont = str(account)
        self.browser.get('https://www.instagram.com/' + accont + '/')

    def isPrivate(self, account):
        self.browser.get('https://www.instagram.com/' + account + '/')
        if(self.browser.find_elements_by_class_name("rkEop")):
            print("Konto prywatne")
            return True
        else:
            return False

    def prefixToString(self, a):
        a = a.replace(" ", "")

        if("," in a):
            self.y = "00"
        else:
            self.y = "000"
        a = a.replace(",", "")

        if("tys." in a):
            a = a.replace("tys.", "")
            a = a + self.y
        elif("mln" in a):
            a = a.replace("mln", "")
            self.y = self.y + "000"
            a = a + self.y

        a = a.replace(" ", "")
        return int(a)

    def scrollWindow(self, y, okno):
        upscroll = 0
        for i in range(1, y):
            i = i + upscroll
            x = str(i)
            time.sleep(0.001)
            window = self.browser.find_element_by_class_name(okno)
            self.browser.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", window)
        upscroll = int(x)

    def scroll(self):

        last_height = self.browser.execute_script(
            "return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def observation(self):
        watch = self.browser.find_element_by_xpath(xpathlist.watch)
        if (watch.text == "Obserwuj"):
            watch.click()
