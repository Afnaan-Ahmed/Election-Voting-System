# Keep track of total votes, individual votes:

available_votes = 20
party1votes = 0
party2votes = 0
party3votes = 0
party4votes = 0

# Voting process:

def voting_process():
    global available_votes,party1votes,party2votes,party3votes,party4votes
    while available_votes != 0:
        vote = input("Which party would you like to vote for? ")
        
        if vote == "1":
            party1votes +=1
            available_votes -= 1
        elif vote == "2":
            party2votes +=1
            available_votes -= 1
        elif vote == "3":
            party3votes +=1
            available_votes -= 1
        elif vote == "4":
            party4votes +=1
            available_votes -= 1
        else:
            print("Enter a valid input.")
            print("Available inputs: 1,2,3,4.")
voting_process()

# Analyzing the result and deciding the winner:

if party1votes > party2votes and party3votes and party4votes:
    print("Party 1 has won the election.")
elif party2votes > party1votes and party3votes and party4votes:
    print("Party 2 has won the election.")
elif party3votes > party2votes and party1votes and party4votes:
    print("Party 3 has won the election.")
elif party4votes > party2votes and party3votes and party1votes:
    print("Party 4 has won the election.")
else:
    print("No winner this time.")
    