#Global
name = "This is a global string"

def greet():
    #Enclosing
    name = 'Sammy'

    def hello():
        #Local
        name = 'me'
        print('Hello' + " " + name)
    
    hello()

greet()

#Notes: If we comment out the variables