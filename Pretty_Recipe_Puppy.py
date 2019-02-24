#We used the Recipe Puppy API :)
api_key = "01c7a5dd19fe082baf1a1bd40c11bd9f"
#We also used these three modules
import webbrowser
import json
import urllib.request

def foodFind():
    y={}
    x = input("Would you like to search by 1)Keywords or by 2)Ingredients? ")
    if x == "1":
        print(y)
        return searchRecipes()
    elif x == "2":
        return searchRecipesByIngredients()
    else:
        print("Please enter 1 or 2")
        foodFind()
def searchRecipes():
    x = input("Search: ")
    x = x.replace(" ", "%20")
    f = urllib.request.urlopen("http://www.recipepuppy.com/api/?q=" + str(x) + "&p=1")
    mydict = json.loads(f.read())
    smalldict = mydict['results']
    i = 0
    for dict in smalldict:
        smallerdict = smalldict[i]
        evensmallerdict = smallerdict['href']
        otherdict = smallerdict['title']
        print(otherdict + ": " + evensmallerdict)
        i += 1
    #return webbrowser.open_new("http://www.recipepuppy.com/api/?q=" + str(x) + "&p=1")
def searchRecipesByIngredients():
    def enter_ingredients():
        ingredients = []
        input_ingredients = input("Enter Ingredients: ")
        while input_ingredients != "":
            input_ingredients = input_ingredients.replace(' ',"%20")
            ingredients.append(input_ingredients)
            input_ingredients = input("Any More? ")
        return ingredients

    def get_recipes_from_ingredients1(a):
        f = urllib.request.urlopen("http://www.recipepuppy.com/api/?i=" + str(a) + "&page=1")
        mydict = json.loads(f.read())
        smalldict = mydict['results']
        i = 0
        for dict in smalldict:
            smallerdict = smalldict[i]
            evensmallerdict = smallerdict['href']
            otherdict = smallerdict['title']
            print(otherdict + ": " + evensmallerdict)
            i += 1
        #return webbrowser.open_new("http://www.recipepuppy.com/api/?i=" + str(a) + "&page=1")

    def get_recipes_from_ingredients2(a, b):
        f = urllib.request.urlopen("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "&page=1")
        mydict = json.loads(f.read())
        smalldict = mydict['results']
        i = 0
        for dict in smalldict:
            smallerdict = smalldict[i]
            evensmallerdict = smallerdict['href']
            otherdict = smallerdict['title']
            print(otherdict + ": " + evensmallerdict)
            i += 1
        #return webbrowser.open_new("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "&page=1")

    def get_recipes_from_ingredients3(a, b, c):
        f = urllib.request.urlopen("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "&page=1")
        mydict = json.loads(f.read())
        smalldict = mydict['results']
        i = 0
        for dict in smalldict:
            smallerdict = smalldict[i]
            evensmallerdict = smallerdict['href']
            otherdict = smallerdict['title']
            print(otherdict + ": " + evensmallerdict)
            i += 1
        #return webbrowser.open_new("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "&page=1")

    def get_recipes_from_ingredients4(a, b, c, d):
        f = urllib.request.urlopen("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "&page=1")
        mydict = json.loads(f.read())
        smalldict = mydict['results']
        i = 0
        for dict in smalldict:
            smallerdict = smalldict[i]
            evensmallerdict = smallerdict['href']
            otherdict = smallerdict['title']
            print(otherdict + ": " + evensmallerdict)
            i += 1
        #return webbrowser.open_new("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "&page=1")

    def get_recipes_from_ingredients5(a, b, c, d, e):
        f = urllib.request.urlopen("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + str(e) + "&page=1")
        mydict = json.loads(f.read())
        smalldict = mydict['results']
        i = 0
        for dict in smalldict:
            smallerdict = smalldict[i]
            evensmallerdict = smallerdict['href']
            otherdict = smallerdict['title']
            print(otherdict + ": " + evensmallerdict)
            i += 1
        #return webbrowser.open_new("http://www.recipepuppy.com/api/?i=" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + str(e) + "&page=1")

    def number_of_ingredients(x):
        length_of_ingredients = len(x)
        if length_of_ingredients == 1:
            return get_recipes_from_ingredients1(x[0])
        elif length_of_ingredients == 2:
            return get_recipes_from_ingredients2(x[0], x[1])
        elif length_of_ingredients == 3:
            return get_recipes_from_ingredients3(x[0], x[1], x[2])
        elif length_of_ingredients == 4:
            return get_recipes_from_ingredients4(x[0], x[1], x[2], x[3])
        elif length_of_ingredients == 5:
            return get_recipes_from_ingredients5(x[0], x[1], x[2], x[3], x[4])

    return number_of_ingredients(enter_ingredients())


# Run Function:
foodFind()