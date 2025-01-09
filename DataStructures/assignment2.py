# program : to manages votes where each voter can vote only once. It uses a set to track voters and a dictionary to count votes for candidates.
def voting_system():
    voters = set()
    votes = {}

    while True:
        print("\nVoting System:")
        print("1. Vote")
        print("2. View Results")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':  # Voting
            voter_id = input("Enter your voter ID: ")
            if voter_id in voters:
                print("You have already voted.")
            else:
                candidate = input("Enter candidate name to vote for: ")
                voters.add(voter_id)
                if candidate in votes:
                    votes[candidate] += 1
                else:
                    votes[candidate] = 1
                print(f"Vote for {candidate} recorded.")
                
        elif choice == '2':  # View results
            if votes:
                for candidate, count in votes.items():
                    print(f"{candidate}: {count} votes")
            else:
                print("No votes yet.")
        
        elif choice == '3':  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

voting_system()
