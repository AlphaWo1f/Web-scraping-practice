import requests
from bs4 import BeautifulSoup


#create list for champions/items
thing = []

#create list of buff or nerf
changes = []

#patchnotes go from   10.1 10.25  to   11.1 11.24  to   12.1 12.23  to   13.1 13.14
num1 = 13
num2 = 2


user = input("Which champion or item would you like the most recent patchnotes for?: ")


for i in range(12):

# REMOVE THE PATCHNOTE THAT MESSES UP THE ORDER
    URL = "https://www.leagueoflegends.com/en-us/news/game-updates/patch-" +str(num1)+ "-" +str(num2)+ "-notes/#patch-champions"
    page = requests.get(URL)



    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all('div', class_ = 'patch-change-block white-stone accent-before')


    counter = 0

    for results in results:
        name = results.find("h3", class_ = 'change-title')
        context = results.find('blockquote', class_ = 'blockquote context')

        if (name is not None) and ((str(name.text) in str(thing)) != True) :
            thing.append(name.text)
            #print(name.text)
        if context is not None:
            changes.append(context.text)
            #print(context.text)


        
        counter += 1
    
    
    #print("CHANGES: ", changes[2])
    num2+=1

temp = 0
#for i in range(25):
#    print(temp)
#    print(changes[temp])
#    
#    temp+=1
#
#print(len(changes))

#print("THING: ", changes)
#print()
index = thing.index(user)
print(thing[index], " ", changes[index])
print(index)



