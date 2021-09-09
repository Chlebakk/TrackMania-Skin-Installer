import os
import shutil
import colorama
import ctypes

from os import path
from termcolor import cprint

version = "0.2"  # Version of TMSI
ctypes.windll.kernel32.SetConsoleTitleW("TrackMania Skin Installer " + version)  # Set window title

colorama.init()  # Make colors in terminal work

operationchoice = "none"

getcwd = os.getcwd()
cwdconverted = str(getcwd)
cwdconverted.replace(r'\\', '/')
cwdslash = cwdconverted.replace(os.sep, '/')

username = os.getlogin()  # Get Windows username to specify documents folder location
tmfolderlocation = r"C:/Users/" + username + r"/Documents/TrackMania/"
tmskinfolderlocation = tmfolderlocation + r"Skins/Vehicles/"

# tm_island_skinfolder = r"SportCar/"
# tm_bay_skinfolder = r"BayCar/"
# tm_coast_skinfolder = r"CoastCar/"
# tm_american_skinfolder = r"American/"
# tm_snow_skinfolder = r"SnowCar/"
# tm_rally_skinfolder = r"Rally/"
tm_stadium_skinfolder = r"StadiumCar/"

tmsi_skins_folder_content = os.listdir(cwdslash + "/Skins/")  # List of skins to install
tmsi_skinspath = r"" + cwdslash + "/Skins/"
tm_docs_skins_folder_content = os.listdir(tmskinfolderlocation + tm_stadium_skinfolder)  # List of skins to remove
tm_docs_skinspath = r"" + tmskinfolderlocation + tm_stadium_skinfolder

file_count_skinstoinstall = sum(len(files) for _, _, files in os.walk(tmsi_skinspath))
file_count_skinstoremove = sum(len(files) for _, _, files in os.walk(tm_docs_skinspath))


# Select env to install skin in
def selectenv():
    # cprint("\nSelect environment:\n1. Stadium", "blue") Removed env selection until environment support is not added
    # envchoice = input("Choice: ")

    envchoice = str("1")

    if envchoice == str("1"):  # Stadium
        if not path.exists(tmskinfolderlocation + tm_stadium_skinfolder):
            cprint("\nCouldn't find Stadium skins folder. Creating one right now!", "yellow")
            os.makedirs(tmskinfolderlocation + tm_stadium_skinfolder)
        updateskinlist()
    else:
        cprint("\nCannot found '" + envchoice + "' environment. Please make sure you selected one from the list.",
               "red")
        restartm = input("Press enter to restart program.")
        foldercheck()


# Selecting car to install
def selectskinfromlist(operation):
    if operation == "install":
        if len(tmsi_skins_folder_content) == 0:  # Check if there are any files in Skins folder.
            cprint("\nCannot found skins in Skins folder! Please move downloaded skins to Skins directory in TMSI "
                   "installation folder.", "red")
            restartm = input("Press enter to restart program.")
            foldercheck()
        else:
            cprint("\nPlease select one skin from the list that you would want to install:", "green")
            cprint("WARNING! ALL SKINS MUST HAVE .ZIP FORMAT.", "red")
            cprint("Type 'back' to return to menu\n", "magenta")
            startnumber = -1

            for i in range(file_count_skinstoinstall):
                startnumber += 1
                # Print a list of skins
                cprint(str(startnumber) + ". " + tmsi_skins_folder_content[startnumber], "yellow")

            skinlistselectionstr = input("Choice: ")

            if skinlistselectionstr == "back":
                menu()

            skinlistselectionint = int(skinlistselectionstr)
            selectedskin = tmsi_skins_folder_content[skinlistselectionint]

            def installskin():
                cprint("\n\n\n\n\n\n\nSelected skin to remove: " + selectedskin, "yellow")
                cprint("\nInstalling skin. It can take from few miliseconds to few minutes.", "green")

                # Move skins in Skins folder to TrackMania skins folder
                shutil.move(r"" + tmsi_skinspath + selectedskin, tmskinfolderlocation + tm_stadium_skinfolder +
                            selectedskin)

                cprint("Skin installation successful! Now you can launch your game and change your skin.", "green")
                restartm = input("Press Enter to restart this program.")
                foldercheck()
            installskin()
    if operation == "remove":
        if len(tm_docs_skins_folder_content) == 0:  # Check if there are any files in Skins folder.
            cprint("\nCannot found skins in TrackMania documents Skins folder to remove!", "red")
            restartm = input("Press enter to restart program.")
            foldercheck()
        else:
            cprint("\nPlease select one skin from the list that you would want to remove:", "cyan")
            cprint("Type 'back' to return to menu\n", "magenta")
            startnumber = -1

            for i in range(file_count_skinstoremove):
                startnumber += 1
                # Print a list of skins
                cprint(str(startnumber) + ". " + tm_docs_skins_folder_content[startnumber], "yellow")

            skinlistselectionstr = input("Choice: ")

            if skinlistselectionstr == "back":
                menu()

            skinlistselectionint = int(skinlistselectionstr)
            selectedskin = tm_docs_skins_folder_content[skinlistselectionint]

            def removeskin():
                cprint("\n\n\n\n\n\n\nSelected skin to remove: " + selectedskin, "yellow")
                cprint("\nRemoving skin. It can take from few miliseconds to few minutes.", "green")

                # Move skins in Skins folder to TrackMania skins folder
                #  shutil.move(r"" + tmsi_skinspath + selectedskin, tmskinfolderlocation +
                #  tm_stadium_skinfolder + selectedskin)

                os.remove(tm_docs_skinspath + selectedskin)

                cprint("Skin removal successful!", "green")
                restartm = input("Press Enter to restart this program.")
                foldercheck()

            removeskin()
        

def updateskinlist():
    # Update skins list
    global tmsi_skins_folder_content
    global tm_docs_skins_folder_content
    global file_count_skinstoinstall
    global file_count_skinstoremove
    tmsi_skins_folder_content = os.listdir(cwdslash + "/Skins/")
    tm_docs_skins_folder_content = os.listdir(tmskinfolderlocation + tm_stadium_skinfolder)
    file_count_skinstoinstall = sum(len(files) for _, _, files in os.walk(tmsi_skinspath))
    file_count_skinstoremove = sum(len(files) for _, _, files in os.walk(tm_docs_skinspath))
    print("Selected: " + operationchoice)
    selectskinfromlist(operationchoice)


# Menu
def menu():
    global operationchoice
    cprint("Welcome to TM Skin Installer " + version + " by Chlebak!\nPlease select an option:\n\n1. Install skin\n"
           "2. Remove skin\n3. Exit", "magenta")
    menuchoice = input("Choice: ")

    if menuchoice == "1":  # Install skin
        operationchoice = "install"
        updateskinlist()

    if menuchoice == "2":  # Remove skin
        operationchoice = "remove"
        updateskinlist()

    if menuchoice == "3":  # Exit
        operationchoice = "exit"
        exit()


# Check if TrackMania folder exists
def foldercheck():
    # cprint("TrackMania documents path: " + tmfolderlocation, "blue")
    # cprint("TrackMania skins path: " + tmskinfolderlocation, "blue")
    # cprint("TMSI location: " + cwdslash, "blue")
    if path.exists(tmfolderlocation):  # Check if TrackMania folder in Documents exists.
        if not path.exists(tmskinfolderlocation):  # Check if Skins folder in TrackMania Folder exists
            cprint("\nCannot found Skins folder! Making one right now...\n", "yellow")
            os.makedirs(tmskinfolderlocation)
        else:
            cprint("\nFound TrackMania folder and Skins folder.\n", "green")
    else:
        print("Cannot found TrackMania folder! Please make sure you have properly installed TrackMania Forever.")
        restartm = input("Press enter to restart program.")
        foldercheck()
    menu()


foldercheck()
