knowledge = dict()
main_msg = "1.Learn new fact\n2.Ask question\n3.Show knowledge\n4.Exit\nChoose your option:\n"
#***********************************************************************************

def mainMenu():
    user_input = input(main_msg)
    if user_input == '1':
        learn_new_fact()
    elif user_input == '2':
        ask_question()
    elif user_input == '3':
        show_knowledge()
    elif user_input == '4':
        pass
    else:
        mainMenu()
        
#***********************************************************************************
def learn_new_fact():
    key = input("Enter fact name:\n")
    val = input("Enter fact Value\n")
    knowledge.update({key:val})
    print("Fact was created")
    mainMenu()
    
#***********************************************************************************
def ask_question():
    question = input("What do you want to know?\n")
    found_answer = False
    for key in knowledge.keys():
        if key == question:
            found_answer = True
            print(question, 'is', knowledge[question])
            break
    if not found_answer:
        print("Unavailable Information!")
    mainMenu()
#***********************************************************************************

def show_knowledge():
    for key in knowledge.keys():
        print(key, ":", knowledge[key])
    mainMenu()
    
#***********************************************************************************
mainMenu()
