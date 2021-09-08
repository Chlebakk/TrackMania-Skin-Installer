import os
import shutil
import colorama
from os import path
from termcolor import cprint

colorama.init()

getcwd = os.getcwd()
cwdconverted = str(getcwd)
cwdconverted.replace(r'\\', '/')
cwdslash = cwdconverted.replace(os.sep, '/')

username = os.getlogin()
tmfolderlocation = r"C:/Users/" + username + r"/Documents/TrackMania/"
tmskinfolderlocation = tmfolderlocation + r"Skins/Vehicles/"

tm_island_skinfolder = r"SportCar/"
tm_bay_skinfolder = r"BayCar/"
tm_coast_skinfolder = r"CoastCar/"
tm_american_skinfolder = r"American/"
tm_snow_skinfolder = r"SnowCar/"
tm_rally_skinfolder = r"Rally/"
tm_stadium_skinfolder = r"StadiumCar/"

# dir_path = os.path.dirname(os.path.realpath(__file__))
skinstoinstallpath = os.listdir(cwdslash + "/Skins/")
skinspath = r"" + cwdslash + "/Skins/"

selectedskin = "none"

file_count = sum(len(files) for _, _, files in os.walk(skinspath))


# Select env to install skin in
def selectenv():
    cprint("\nSelect enviroment:\n1. Stadium", "blue")
    envchoice = input("Choice: ")

    if envchoice == str("1"):  # Stadium
        if not path.exists(tmskinfolderlocation + tm_stadium_skinfolder):
            cprint("\nCouldn't find Stadium skins folder. Creating one right now!", "yellow")
            os.makedirs(tmskinfolderlocation + tm_stadium_skinfolder)
        select_stadium()


# Selecting car to install
def select_stadium():
    if len(skinstoinstallpath) == 0:  # Check if there are any files in Skins folder.
        cprint("\nCannot found skins in Skins folder! Please move installed skins to Skins directory in TMSI "
               "installation folder.", "red")
        restartm = input("Press enter to restart program.")
        updatedirs()
    else:
        cprint("\nPlease select one skin from the list that you would want to install:", "green")
        cprint("WARNING! ALL SKINS MUST HAVE .ZIP FORMAT.\n", "red")
        startnumber = -1

        for i in range(file_count):
            startnumber += 1
            cprint(str(startnumber) + ". " + skinstoinstallpath[startnumber], "yellow")  # Print a list of skins

        skinlistselectionstr = input("Choice: ")
        skinlistselectionint = int(skinlistselectionstr)
        selectedskin = skinstoinstallpath[skinlistselectionint]

        def installskin():
            cprint("\n\n\n\n\n\n\nSelected skin to install: " + selectedskin, "yellow")
            cprint("\nInstalling skin. It can take from few miliseconds to few minutes.", "green")

            # Move skins in Skins folder to TrackMania skins folder
            shutil.move(r"" + skinspath + selectedskin, tmskinfolderlocation + tm_stadium_skinfolder + selectedskin)

            cprint("Skin installation successful! Now you can launch your game and change your skin.", "green")
            restartm = input("Press Enter to restart this program.")
            updatedirs()
        installskin()


# Menu
def menu():
    cprint("Welcome to TM Skin Installer v0.11 by Chlebak!\nPlease select an option:\n\n1. Install skin\n2. Folder "
           "check & update variables\n3. Exit", "yellow")
    menuchoice = input("Choice: ")

    if menuchoice == "1":  # Install skin
        selectenv()
    # if menuchoice == "0":  # Remove skin
    #   pass
    if menuchoice == "2":  # Folder check and update variables
        updatedirs()
    if menuchoice == "3":  # Exit
        exit()


# Check if TrackMania folder exists
def foldercheck():
    cprint("TrackMania documents path: " + tmfolderlocation, "blue")
    cprint("TrackMania skins path: " + tmskinfolderlocation, "blue")
    cprint("TMSI location: " + cwdslash, "blue")
    if path.exists(tmfolderlocation):  # Check if TrackMania folder in Documents exists.
        if not path.exists(tmskinfolderlocation):  # Check if Skins folder in TrackMania Folder exists
            cprint("\nCannot found Skins folder! Making one right now...\n", "yellow")
            os.makedirs(tmskinfolderlocation)
        else:
            cprint("Found TrackMania folder and Skins folder.\n", "green")
    else:
        print("Cannot found TrackMania folder! Please make sure you have properly installed TrackMania Forever.")
        restartm = input("Press enter to restart program.")
        updatedirs()
    menu()

def updatedirs():
    cprint("Updating variables...", "yellow")
    getcwd = os.getcwd()
    cwdconverted = str(getcwd)
    cwdconverted.replace(r'\\', '/')
    cwdslash = cwdconverted.replace(os.sep, '/')
    username = os.getlogin()
    tmfolderlocation = r"C:/Users/" + username + r"/Documents/TrackMania/"
    tmskinfolderlocation = tmfolderlocation + r"Skins/Vehicles/"
    tm_island_skinfolder = r"SportCar/"
    tm_bay_skinfolder = r"BayCar/"
    tm_coast_skinfolder = r"CoastCar/"
    tm_american_skinfolder = r"American/"
    tm_snow_skinfolder = r"SnowCar/"
    tm_rally_skinfolder = r"Rally/"
    tm_stadium_skinfolder = r"StadiumCar/"
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    skinstoinstallpath = os.listdir(cwdslash + "/Skins/")
    skinspath = r"" + cwdslash + "/Skins/"
    selectedskin = "none"
    file_count = sum(len(files) for _, _, files in os.walk(skinspath))
    foldercheck()


updatedirs()
