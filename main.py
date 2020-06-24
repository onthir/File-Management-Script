# folder management software
from controller import Flodder


# read directory from text file
def readDir(file):
    with open(file, "r") as file:
        content = file.readlines()

    return content[0]


def file_manage(path_read):
    directories = {
        "1": "/Pictures/",
        "2": "/Videos/",
        "3": "/Music/",
        "4": "/Setup/",
        "5": "/Documents/",
        "6": "/Compressed/",
        "7": "",
        "8": "/Programming/",

    }

    scoreKeeper = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
    }
    # path
    path = path_read
    # create the flodder object
    classifier = Flodder()

    # breaker flag
    breaker = False

    # make default folders
    classifier.makeDefault(path)

    # all directories
    dirs = classifier.listAll(path)
    
    for directory in dirs:
        # classify
        code = classifier.classify(directory)
        DIRECTORY = path + "/" + directory 
        
        # get the code and move to respective directories
        temp = path + directories[code] + "/" + directory
        classifier.move(DIRECTORY, temp)
        scoreKeeper[code] += 1
    scoreReader(scoreKeeper, directories)

def scoreReader(current, fromt):
    print("Summary\n")
    for key in current.keys():
        if key != "7":
            newKey = fromt[key].replace("/", "")
            print(newKey + ": " + str(current[key]) + " files.")
