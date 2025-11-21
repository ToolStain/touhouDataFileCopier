import json
import os

with open("TouhouInfos.json", 'r') as file:
    thTable = json.load(file)

shingaiAliceAppDataFolder = "C:\\Users\\lang_\\AppData\\Roaming\\ShanghaiAlice"
targetFolder = "C:\\Users\\lang_\\Downloads\\Touhou Project"

appliedFolder = "G:\\BackupStuff\\Touhou Project"
backupFolder = "G:\\BackupStuff\\Touhou Project\\z_backupOldScores"

checkTable = [
    shingaiAliceAppDataFolder,
    targetFolder,
    appliedFolder,
    backupFolder
]
for folder in checkTable:
    check = os.path.exists(folder)
    if check == False:
        input(f"!!! Missing Folder: {folder}")
        quit()



input(f"Transferring Touhou Data from [{targetFolder}] > [{appliedFolder}], yes?")

def dataRead(dataFileLoc):
    print("Reading...")
    with open(dataFileLoc, 'rb') as file:
        readData = file.read()
        return readData
    
def dataWrite(dataFileLoc, data):
    print("Writing...")
    with open(dataFileLoc, 'wb') as file:
        file.write(data)

def dataBackup(dataFileLoc, data):
    print("Backing up...")
    with open(dataFileLoc, 'wb') as file:
        file.write(data)
    
folderExist = os.path.exists(f"{backupFolder}\\ShanghaiAlice")
if folderExist == False:
    os.mkdir(f"{backupFolder}\\ShanghaiAlice")

try:
    for touhouData in thTable:
        print(f"> Managing {touhouData['folderName']}")
        if touhouData['varient'] == 1:
            scoreFileName = "score.dat"
            currentDataLoc = f"{targetFolder}\\{touhouData['folderName']}\\{scoreFileName}"
            appliedDataLoc = f"{appliedFolder}\\{touhouData['folderName']}\\{scoreFileName}"
            backupLoc = f"{backupFolder}\\score_{touhouData['num']}_.dat"

            data = dataRead(currentDataLoc)
            dataWrite(appliedDataLoc, data)
            dataBackup(backupLoc, data)

        elif touhouData['varient'] == 2:
            scoreFileName = touhouData['scoreFileName']
            currentDataLoc = f"{targetFolder}\\{touhouData['folderName']}\\{scoreFileName}"
            appliedDataLoc = f"{appliedFolder}\\{touhouData['folderName']}\\{scoreFileName}"
            backupLoc = f"{backupFolder}\\{scoreFileName}"
            
            data = dataRead(currentDataLoc)
            dataWrite(appliedDataLoc, data)
            dataBackup(backupLoc, data)

        elif touhouData['varient'] == 3:
            scoreFileName = touhouData['scoreFileName']
            currentDataLoc = f"{shingaiAliceAppDataFolder}\\{touhouData['folderName']}\\{scoreFileName}"
            appliedDataLoc = f"{backupFolder}\\ShanghaiAlice\\{scoreFileName}"
            data = dataRead(currentDataLoc)
            dataBackup(appliedDataLoc, data)

        else:
            input("Couldn't find!")
except Exception as error:
    input(f'ERROR: {error}')

input("Successfully overwritten data!")
