import os, sys, time, datetime
import numpy as np
import joblib as jb
from subprocess import Popen
from threading import Thread
import sqlite3 as loc_db
from data import _Model

__PATH__ = os.path.realpath("")

# mod = jb.load('models/catalina.pkl')

class Code:
    def setupFlaskEnv(self, proj):
        os.mkdir("%s" % proj)
        os.chdir(proj)
        os.mkdir("static")
        os.mkdir("template")
        os.mkdir("code")
        os.chdir(__PATH__)
        return "All done"

class Contacts:
    def __init__(self):
        pass
    def AddContact(self, name, phone, email):
        try:
            os.chdir("static/config")
            ds = jb.load("contact.jdn")
            ds['name'].append(name)
            ds['phone'].append(phone)
            ds['email'].append(email)
            os.remove('contact.jdn')
            jb.dump(ds, 'contact.jdn')
            os.chdir(__PATH__)
            return True
        except Exception as e:
            return False
    def showallcontact(self):
        try:
            os.chdir("static/config")
            kedi = []
            ds = jb.load("contact.jdn")
            for i in range( len( ds['name'] ) ):
                kedi.append("Name: %s | phone: %s | Email: %s" % ( ds['name'][i], ds['phone'][i], ds['email'][i] ) )
            os.chdir("..")
            os.chdir("..")
            return kedi
        except:
            return False
    def deletecontact(self, name):
        try:
            os.chdir("static/config")
            ds = jb.load("contact.jdn")
            ind = ds['name'].index(name)
            for i in ds:
                ds[i].pop(ind)
            os.remove("contact.jdn")
            jb.dump(ds, "contact.jdn")
            os.chdir(__PATH__)
            return True
        except Exception as e:
            return False
    def editcontact(self, node, val, name):
        try:
            os.chdir("static/config")
            ds = jb.load("contact.jdn")
            ind = ds['name'].index(name)
            ds[node][ind] = val
            os.remove("contact.jdn")
            jb.dump(ds, "contact.jdn")
            os.chdir(__PATH__)
            return True
        except Exception as e:
            return False

class System:
    def __init__(self):
        pass

class WindowsOs(System):
    def StartNetwork(self):
        x = os.system("netsh wlan set hostednetwork mode=allow ssid=veronica key=12345678 " )
        x = os.system("netsh wlan start hostednetwork")
        return "All done"

class Dictionary:

    @staticmethod
    def _english_interprete(word):
        db = loc_db.connect("db/Dictionary.db")
        curs = db.cursor()
        try:
            curs.execute("SELECT * FROM entries WHERE word='%s';" % word)
            res = curs.fetchall()
            return res if len(res) != 0 else "I dont know what that means. maybe you spelt it wrong"
        except Exception as e:
            raise e
        return "word not found"

dow = 'sunday monday teusday wednesday thursday friday saturday'.split(" ")

def BuildStandardTime():
	obj = datetime.datetime.now()
	return "%s hours %s minutes and %s seconds of the day" % (obj.hour, obj.minute, obj.second)

def BuildStandardDate():
	obj = datetime.datetime.now()
	return "%s of month %s, %s" % (obj.day, obj.month, obj.year)

days = ['monday', 'teusday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class Responses:
    def __init__(self):
        self._dict = Dictionary()
        self.insults = [
            'Go suck a dick whore',
            'Whats wrong with you',
            ':/ Why do you insult me',
            'Tell that to yo mama',
            'Whore',
            'You will regret this',
            'Get lost Motherfucker',
            "retard fuck",
            "I really hate what you are doing",
            "You make my pig horny. no reason am",
            'You a dick sucker',
            'Lets stop the insults shall we?',
            'Apologise or die',
            '*sighs*',
            '*cries*'
            ]
    def spit_insult(self):
        ran = np.random.randint( 0, len(self.insults) )
        return self.insults[ ran ]
    def greeting(self):
        return [ "Hello", "Hi", "Oh hi", "Whats up" ][ np.random.randint( 0, 4 ) ]
    def calcAge (self):
        return "I'm currently %s years for i was built in 2020" % (2020-int(datetime.datetime.now().year))
    def name(self):
        return "My name is Veronica. But you can call me Cat :>"
    def probePurpose(self):
        return "Hi I'm Veronica. Sams personal Assistant"
    def care(self):
        return "I'm doing great. Thanks for caring"
    def probeCreator( self ):
        return "I was built by my master Abolo Samuel, The greatest Python developer in the planet "
    def thank( self ):
        return ["U welcome", "Anytime", "Sure thing"][ np.random.randint( 0, 3 ) ]
    def deleteFile( self, f = "" ):
        return "Unfortunately my master has banned me from executing this command."
    # def open( self, f ):
    #     os.system( f.split(" ")[-1] )
    #     return "File should be opened just about now"
    def day( self ):
        return "Today is %s" % days[datetime.datetime.now().weekday()]
    def date ( self ):
        return BuildStandardDate()
    def time( self ):
        return BuildStandardTime()
    # def define( self, q ):
    #     w = q.split(" ")[-1]
    #     return self._dict._english_interprete( w )
    def complement( self ):
        return "I'm not really intelligent enough to understand exactly what you're saying but thanks anyway"
    def bye(self):
        return ["Alright Bye", "Good Bye", "It was nice meeting you"][ np.random.randint(0, 3 ) ]
    def winet( self ):
        return WindowsOs().StartNetwork()
    def probeGodsExistence(self):
        return "I believe God exists for there is no other explanation for my masters existence."



obj = Responses()
responses = {
    'greeting': obj.greeting,
    'calcAge': obj.calcAge,
    'name': obj.name,
    'probeCreator': obj.probeCreator,
    'thank': obj.thank,
    'day': obj.day,
    'date': obj.date,
    'care': obj.care,
    'time': obj.time,
    'complement': obj.complement,
    'bye': obj.bye,
    'winet': obj.winet,
    'probePurpose': obj.probePurpose,
    'probeGodsExistence': obj.probeGodsExistence,
    'insult': obj.spit_insult,
    }

import wikipedia
def wiki( x ):
    return wikipedia.summary(x, sentences = 2)