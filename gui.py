import easygui
#
# easygui.ynbox('Shall I continue?', 'Title', ('yes', 'no'))
#
#
#
# easygui.msgbox('Hello World', 'Title')
#
# var = easygui.buttonbox('Click on your favorite flavor', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
# print var


# msg = "What is your favorite flaver?"
# title = "Ice Cream Survey"
# choices = ['Vanilla', 'Chocolate', 'Strawberry', 'Rocky Road']
# var = easygui.choicebox(msg, title, choices)
# print var
#

#
# easygui.enterbox('Input your name', "What's your Name?")


msg = "Input your informations"
title = "Sign up"
fieldNames = ["Mail", "Name", "Age", "Sex", "Country"]
fieldValues = easygui.multenterbox(msg, title, fieldNames)
informations = "Your Mail is %s \nName  is %s \nnAge is %s \nSex is %s \nCountry is %s" % \
               (fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3], fieldValues[4])
easygui.msgbox(informations, 'Welcome')
