import os
import csv
csvpath = os.path.join(".", "Resources", "election_data.csv")
output = os.path.join('.', 'analysis', 'election_results.txt')
candidate =[]
candidate_list = []
votecount = {}
winning_candidate = ""
winning_count = 0

# def print_poll_results(candidate_name):


# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# Initialize rowcount
rowcount = 0

with open(csvpath) as election_data:
    csvreader = csv.reader(election_data,delimiter=",")
    csvheader = next(csvreader)

    
    for row in csvreader:
#       count the number of rows to get the he total number of votes cast
        rowcount += 1
        candidate_name = row[2]
        
#       append any new candidates not already in the candidate list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votecount[candidate_name] = 0
        
        votecount[candidate_name] +=1
            
#     number_of_candidates = len(candidate_list)
#     print(number_of_candidates)
    
#     print(rowcount)
#     print(votecount)
    
    election_results=(
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total votes: {rowcount}\n"
        f"-----------------------------\n"
            )
    print(election_results, end ="")
    
    with open (output, "w") as txt_file:
        txt_file.write(election_results)
        
    
        for candidate in votecount:
            votes = votecount.get(candidate)
            vote_percentage = float(votes)/float(rowcount) * 100

            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output, end ="")
            txt_file.write(voter_output)

            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate

        winner_summary=(
            f"-----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"-----------------------------\n"
                )
        txt_file.write(winner_summary)
        print(winner_summary, end = "")


    