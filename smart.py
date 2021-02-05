from api import *
import os
import joblib as jb
from data import _Model
from threading import Thread
import pyttsx3

os.system("cls")

system = jb.load("catalina.pkl")

obj = pyttsx3.init()
voices = obj.getProperty("voices")
obj.setProperty( "voice", voices[1].id )

def speak( text ):
    obj.say( text )
    obj.runAndWait()
    # winsound.PlaySound( f"{uc}.mp3", winsound.SND_FILENAME )
    # os.chdir("..")

retries = 0
while True:
    pwd = input("Catalina> Input The password: ")

    if ( pwd  == '0000' ):
        print( "\n\nCatalina> Access Granted\n\n" )
        break
    else:
        print( "Catalina> Thats not the password. Please try again\n" )
        if ( retries >= 3 ):
            print("Catalina> Who the fuck are you\n")
        retries += 1

def display( string ):
    print( f"Veronica> {string}" )
    speak( string )

while True:
    print("\n")
    j = input("You> ")
    print( "\n" )
    pred = system.classify( j )

    if ( pred[0]['score'] > 0.5 ):

        pred = pred[0]

        if ( pred['intent'] in responses ):

            respond = responses[ pred['intent'] ]()
            display( respond )

            if ( pred['intent'] == 'bye' ):
                sys.exit()
        
        elif ( pred['intent'] == 'define' ):

            response = Dictionary._english_interprete( j.split(" ")[-1] )

            for i in response:
                display( f"It could mean {i[2]}\n" )


        elif ( pred['intent']  == 'wiki' ):
            display( "searching %s" % ( j ) )
            try:
                respond = wiki( j )
                display( respond )
            except:
                display( "I think there's something wrong with the connection." )

        else:
            print(pred)
            # pass
    else:
        display( "Searching %s " % j )
        try:
            respond = wiki( j )
            display( respond )
        except:
                display("I think there's something wrong with the connection.")
            # speak( "I think there's something wrong with the connection." )
        # print("Hmmm. Sorry i didnt get that :/")