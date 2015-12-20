def findUniqueWords(theList):
    newList = []
    words = []

    # Read a line at a time
    for item in theList:
        # Remove any punctuation from the line
        cleaned = cleanUp(item)

        # Split the line into separate words
        words = cleaned.split()

        # Evaluate each word
        for word in words:
            # Count each unique word
            if word not in newList:
                newList.append(word)

    answer = sorted(newList)
    return answer

def cleanUp(phrase):
    item = str(phrase).replace(".","")
    item = str(item).replace(",","")
    item = str(item).replace(":","")
    item = str(item).replace("'","")
    item = str(item).replace("\n","")
    return item

def main():
    fileName = raw_input("Enter a filename: ")
    list = open(fileName,'r')

    finalList = findUniqueWords(list)
    print finalList


main()

