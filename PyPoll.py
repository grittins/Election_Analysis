# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes (list and dictionary)
candidate_options = []
candidate_votes = {}

# County options and county votes (list and dictionary)
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.  (if statements to determine winner)
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county with most votes
most_county_votes = 0
most_county_name = ""


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # performing the same for counties
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0 
        county_votes[county_name] += 1


    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        format = (
            f"\n"
            f"County Votes:\n")
        print(format)
        txt_file.write(format)
        # Print the each county results (percentage and turnout) to the terminal
        for county_name in county_votes:
            poll = county_votes[county_name]
            poll_percentage = (float(poll) / float(total_votes)) * 100
            county_results = (f"{county_name}: {poll_percentage:.1f}% ({poll})\n")
            print(county_results)
            # Write the percentage and turnout in the txt file
            txt_file.write(county_results)

            if (poll > most_county_votes):
                most_county_votes = poll
                most_county_name = county_name

        turnout = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {most_county_name}\n"
            f"-------------------------\n"
        )
        print(turnout)
        txt_file.write(turnout)        

        # To print vote percentages and winner
        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print each candidate, their voter count, and percentage to the
            # terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)           

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Write the winning candidate summary on txt file
        txt_file.write(winning_candidate_summary)
