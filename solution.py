import json


# =============================================================================================================#
# QEUSTION ==> 1
# =============================================================================================================#
# 1. Number of URLH which are overlapping (Common) in two files.


def question1():
    # crateing list to store individudal json data
    todaysData = []
    yesterdaysData = []

    # retriving data from json to list
    with open("today.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            todaysData.append(itemDic)

    with open("yesterday.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            yesterdaysData.append(itemDic)

    # taking urlhs from todaysdata
    urlhToday = []
    for obj in todaysData:
        urlhToday.append(obj['urlh'])

    # taking urlhs from yesterdaysdata
    urlhYesterday = []
    for obj in yesterdaysData:
        urlhYesterday.append(obj['urlh'])

    print(len(urlhToday), len(urlhYesterday))

    # common urlhs in both files
    inter = list(set(urlhYesterday) & set(urlhToday))

    print(f" number of urhs common in both the files are {len(inter)}")


# question1()


# =============================================================================================================#
#  QEUSTION ==> 3
# =============================================================================================================#
# 3. Number of Unique categories in both files.


def question3():
    # creating empty list to get data from today and yeasterday files
    todaysData = []
    yesterdaysData = []

    # retriving data from json to list for today file
    with open("today.json") as f:
        # getting each object from file
        for eachObj in f:
            # taking json object as dictionary
            itemDic = json.loads(eachObj)
            # appending item item dictionary to the todays data
            todaysData.append(itemDic)

    # retriving data from json to list for yesterday file
    with open("yesterday.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            yesterdaysData.append(itemDic)

    # taking urlhs from todaysdata
    catToday = []
    for obj in todaysData:
        catToday.append(obj['category'])

    # taking urlhs from yesterdaysdata
    catYesterday = []
    for obj in yesterdaysData:
        catYesterday.append(obj['category'])

    # merging two categories lists
    mergedList = catToday + catYesterday

    # taking set to remove duplicates from the mergedList
    finalCat = set(mergedList)
    print(f"Number of unique categories in both the files are {len(finalCat)}")

# question3()


# =============================================================================================================#
# QEUSTION ==> 4
# =============================================================================================================#
# 4 Display List of categories which is not overlapping (Common) from two given files


def question4():
    todaysData = []
    yesterdaysData = []

    # retriving data from json to list
    with open("today.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            todaysData.append(itemDic)

    with open("yesterday.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            yesterdaysData.append(itemDic)

    # taking categories from todaysdata
    catToday = []
    for obj in todaysData:
        catToday.append(obj['category'])

    # taking categories from yesterdaysdata
    catYesterday = []
    for obj in yesterdaysData:
        catYesterday.append(obj['category'])

    # taking uncommon categories from both the sets of today's categories and yesterday's categories
    # and xor it to get the uncommon categories if any exists
    uncommon = set(catToday) ^ set(catYesterday)
    print(
        f" List of categories which is not overlapping(Common) from two given files are {len(uncommon)}")

# question4()


# =============================================================================================================#
# QEUSTION ==> 5
# =============================================================================================================#
# 5. Generate the stats with count of urlh for all taxonomies(taxonomy is concatenation of category and subcategory separated by " > ") for today's file.
# Eg:
# Cat1 > Subcat1: 3500
# Cat1 > Subcat2: 2000
# Cat2 > Subcat3: 8900


def question5():
    todaysData = []
    catData = []

    # retriving data from json to list
    with open("today.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            todaysData.append(itemDic)
            # taking only categories in the catData list
            catData.append(itemDic['category'])

    # making list of unique category
    catData = list(set(catData))

    # traversaing each unique categories from catData
    for cat in catData:
        # initialize empty list to get all subcategories for the current category
        currentSubCatList = []

        # traversing through today's data to get all category which match the current category
        for i in todaysData:
            # if category matches the current category will add it's subcategory to the current sub cat list
            if i['category'] == cat:
                currentSubCatList.append(i['subcategory'])

        # creating set to get all unique sub categories
        anotherset = list(set(currentSubCatList))

        # traversing through uniquely created sub cat list and printing count of that sub cat list with main category
        for i in anotherset:
            print(f"{cat} >  {i} : {currentSubCatList.count(i)}")


# question5()


# =============================================================================================================#
# QEUSTION ==> 6
# =============================================================================================================#
# 6. Generate a new file where mrp is normalized. If there is a 0 or a non-float value or the key doesn't exist, make it "NA".

def question6():
    todaysData = []
    with open("today.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            todaysData.append(itemDic)

    for i in todaysData:
        # checking mrp values for validity according to question
        if type(i['mrp']) == int or i['mrp'] == "0" or i['mrp'] == None:
            temp = {'mrp': "NA"}
            i.update(temp)

    print("wait creating the file......")
    # writing the changed data (mrp) to the file
    fs = open("mrp.json", "w")
    for obj in todaysData:
        json.dump(obj, fs, indent=4)

    print("Thank You, Your file is ready with the name mrp.json")


# question6()


# =============================================================================================================#
# QEUSTION ==> 7
# =============================================================================================================#
# 7. Display the title and price of 10 items having least price.
# Eg:
# Title1 - -> its price
# Title2 - -> its price
# upto 10


def question7():
    todaysData = []
    with open("today.json") as f:
        for eachObj in f:
            itemDic = json.loads(eachObj)
            # taking data only which has available price and title value as non null
            if itemDic['available_price'] != None or itemDic['title'] != None:
                item = [itemDic['available_price'], itemDic['title']]
                todaysData.append(item)

    # sorting the data according to the available price
    sort = sorted(todaysData)

    # printing 10 items
    for i in range(10):
        print(f"{sort[i][1]} =>  {sort[i][0]}")

# question7()


# =============================================================================================================#
# QEUSTION ==> 8
# =============================================================================================================#
# 8. Display the top 5 subcategory having highest items.


def question8():
    todaysData = []

    with open("today.json") as f:
        for obj in f:
            dic = json.loads(obj)
            # taking only subcategories from dictionary
            todaysData.append(dic['subcategory'])

    # taking set to make uniques subcategories
    extra = set(todaysData)

    # making empty list to store the sub categories and its values how many time it is in file
    listItems = []
    for i in extra:
        item = [todaysData.count(i), i]
        listItems.append(item)

    # sorting the list in reverse to print highest items for sub categories
    sort = sorted(listItems, reverse=True)

    for i in range(5):
        print(f"{sort[i][1]} => {sort[i][0]}")

# question8()


# =============================================================================================================#
# QEUSTION ==> 9
# =============================================================================================================#
# 9. Display stats of how many items have failed status (http_status other than 200 is to be considered as failure).
# Eg.
# http_status     count
# 500             23
# 404             12


def question9():
    yesterdayData = []

    with open("yesterday.json") as f:
        for obj in f:
            dic = json.loads(obj)
            # taking only the codes which has errors and failure
            if dic['http_status'] > "200":
                yesterdayData.append(dic['http_status'])

    # taking set to remove duplication in http status code
    codes = set(yesterdayData)

    # traversing and printing the count for that http status code
    for i in codes:
        print(f"{i} => {yesterdayData.count(i)}")

# question9()


# =============================================================================================================#
# QEUSTION ==> 2
# =============================================================================================================#
# 2. For all the URLH which are overlapping, calculate the price difference (wrt available_price) if there is any between yesterday's and today's crawls (scraped data). There might be duplicate URLHs in which case you can choose the first valid (with http_status 200) record.


def question2():
    tod = []  # empty lists to store urlh data from today file
    yest = []  # empty lists to store urlh data from yesterday file
    with open("today.json") as file:
        for obj in file:  # read each json obj and store in a temp dict
            dic = json.loads(obj)
            tod.append(dic)
    with open("yesterday.json") as file2:
        for obj in file2:
            dic = json.loads(obj)
            yest.append(dic)

    # creating two empty dictionaries to get all urlhs and its status code and available prices
    main_yest = {}
    main_tod = {}

    # traversing through the yesterday data
    for i in yest:
        # if the urlh as a key exists in the main yesterday dictionary will move to inner if clause
        if i["urlh"] in main_yest.keys():
            # checking three conditions
            #  1 > current urlh key should not have status code of 200
            #  2 > in yesterday file status code should be 200
            #  3 > even the available price should not be null in the yesterday file
            #  if all condition matches true will change the http_status and available_price for that current urlh
            if (main_yest[i["urlh"]][0] != 200) and (i["http_status"] == 200) and (i["available_price"] != None):
                main_yest[i["urlh"]] = [i["http_status"], i["available_price"]]
        # if the key doesn't exist and available_price is not null
        #  will add new key value pair to the main yesterday dictionary
        elif i["available_price"] != None:
            temp = {i["urlh"]: [i["http_status"], i["available_price"]]}
            main_yest.update(temp)

    for i in tod:
        if i["urlh"] in main_tod.keys():
            if (main_tod[i["urlh"]][0] != 200) and (i["http_status"] == 200) and (i["available_price"] != None):
                main_tod[i["urlh"]] = [i["http_status"], i["available_price"]]
        elif i["available_price"] != None:
            temp = {i["urlh"]: [i["http_status"], i["available_price"]]}
            main_tod.update(temp)

    # taking all the keys of the main yesterday file as list
    unlist = list(main_yest.keys())

    diff = {}

    for i in unlist:
        # checking if the key exist in main today dictionary keys
        if i in main_tod.keys():
            # calculating the difference for today and yesterday available_price values
            diffval = float(main_tod[i][1])-float(main_yest[i][1])
            # updating the difference dictionary with urlh(key) and value as list of status code and difference in prices
            temp = {i: [main_tod[i][0], diffval]}
            diff.update(temp)

    for i in diff.items():
        print(i)


# question2()


def codeRunner():

    while(True):
        choice = int(
            input("======Enter the question number to run: && to exit enter 0 ====>  "))
        print("\n")
        if choice == 0:
            exit()
        elif choice == 1:
            question1()
        elif choice == 2:
            question2()
        elif choice == 3:
            question3()
        elif choice == 4:
            question4()
        elif choice == 5:
            question5()
        elif choice == 6:
            question6()
        elif choice == 7:
            question7()
        elif choice == 8:
            question8()
        elif choice == 9:
            question9()
        else:
            print("Please enter numbers between 1 to 9")
        print("\n")


codeRunner()
