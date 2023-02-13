import tkinter
available_votes = 20
party1_votes = 0
party2_votes = 0
party3_votes = 0
party4_votes = 0

###########################################################  FUNCTION DEFINITIONS  ####################################################

def output(x):
    message['text'] = x

def vote_p1():
    global available_votes,party1_votes
    if (available_votes>0):
        party1_votes += 1
        available_votes -=1
        available_votes_gui['text'] = available_votes
        party1_votes_gui['text'] = party1_votes
    else:
        output("No more votes")
    
def vote_p2():
    global available_votes,party2_votes
    if (available_votes>0):
        party2_votes += 1
        available_votes -=1
        available_votes_gui['text'] = available_votes
        party2_votes_gui['text'] = party2_votes
    else:
        output("No more votes")
    
def vote_p3():
    global available_votes,party3_votes
    if (available_votes>0):
        party3_votes += 1
        available_votes -=1
        available_votes_gui['text'] = available_votes
        party3_votes_gui['text'] = party3_votes
    else:
        output("No more votes")
    
def vote_p4():
    global available_votes,party4_votes
    if (available_votes>0):
        party4_votes += 1
        available_votes -=1
        available_votes_gui['text'] = available_votes
        party4_votes_gui['text'] = party4_votes
    else:
        output("No more votes")
    
def submit():
    
    global available_votes,party1_votes,party2_votes,party3_votes,party4_votes
    
    if party1_votes > party2_votes and party1_votes > party3_votes and party1_votes > party4_votes:
        output("Party 1 has won the election.")
    elif party2_votes > party1_votes and party2_votes > party3_votes and party2_votes > party4_votes:
        output("Party 2 has won the election.")
    elif party3_votes > party2_votes and party3_votes > party1_votes and party3_votes > party4_votes:
        output("Party 3 has won the election.")
    elif party4_votes > party2_votes and party4_votes > party3_votes and party4_votes > party1_votes:
        output("Party 4 has won the election.")
    else:
        output("No winner this time.")
        


##########################################################   GUI PART    ##################################################################

base = tkinter.Tk()
base.geometry('500x500')
base.title("Election")

b1 = tkinter.Button(text='Party 1',command=vote_p1)
b2 = tkinter.Button(text='Party 2',command=vote_p2)
b3 = tkinter.Button(text='Party 3',command=vote_p3)
b4 = tkinter.Button(text='Party 4',command=vote_p4)
b1.place(x=140,y=200)
b2.place(x=200,y=200)
b3.place(x=260,y=200)
b4.place(x=320,y=200)

l1 = tkinter.Label(base,text= "Available Votes:")
l1.place(x=180,y=40)
available_votes_gui = tkinter.Label(base,text = available_votes)
available_votes_gui.place(x=280,y=40)

l2 = tkinter.Label(base,text= "Party 1 Votes:")
l2.place(x=180,y=60)
party1_votes_gui = tkinter.Label(base,text = party1_votes)
party1_votes_gui.place(x=280,y=60)

l3 = tkinter.Label(base,text= "Party 2 Votes:")
l3.place(x=180,y=80)
party2_votes_gui = tkinter.Label(base,text = party2_votes)
party2_votes_gui.place(x=280,y=80)

l4 = tkinter.Label(base,text= "Party 3 Votes:")
l4.place(x=180,y=100)
party3_votes_gui = tkinter.Label(base,text = party3_votes)
party3_votes_gui.place(x=280,y=100)

l5 = tkinter.Label(base,text= "Party 4 Votes:")
l5.place(x=180,y=120)
party4_votes_gui = tkinter.Label(base,text = party4_votes)
party4_votes_gui.place(x=280,y=120)

message = tkinter.Label(base,text='')
message.place(x=250,y=300,anchor="center")

submit = tkinter.Button(base,text='Submit',command=submit)
submit.place(x=225,y=250)

base.mainloop()