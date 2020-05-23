import csv

load = "/Users/hugogarcia/Desktop/Data BootCamp/python-challenge/PyPoll/election_data.csv"
output = "/Users/hugogarcia/Desktop/Data BootCamp/python-challenge/PyPoll/election_analysis.txt"

total_votes = 0
candidate = []
candidate_votes = {}

winner_candidate = ""
winner_count = 0

with open(load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
        
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] = candidate_votes[candidate_name]+1

with open(output, "w") as txt_file:

    election_results = (
        f"Election Results"
        f"Total Votes: {total_votes} "
    )
    print(election_results)

    txt_file.write(election_results)

    for candidates in candidate_votes:
        votes = candidate_votes.get(candidates)
        vote_percentage = float(votes) / float(total_votes) *100

    if(votes > winner_count):
        winner_count = votes
        winner_candidate = candidates

    voter_output = f"{candidates}: {vote_percentage: }% ({votes})"
    print(voter_output)

    txt_file.write(voter_output)

    winner_summary = (
    f"Winner: {winner_candidate}"
    )

    print(winner_summary)

    txt_file.write(winner_summary)