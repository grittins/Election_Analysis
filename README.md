# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
Data Source: election_results.csv                
Software: Python Visual Code Studio Version: 1.67.2 (Universal)

## Overview of Election Audit
The purpose of this election audit analysis is to read the election results from a csv file and count the number of votes received by each candidate alongside the county where the votes were casted. Running the analysis on this csv file shows the total number of votes, how many votes the candidates received, turnout of votes in each county and determining the winner of the election. 

## Election-Audit Results

- Total Votes: 369,711
- County Votes:                     
Jefferson: 10.5% (38855)              
Denver: 82.8% (306055)                
Arapahoe: 6.7% (24801)              
- Largest County Turnout: Denver
- Candidate Results:                       
  Charles Casper Stockham: 23.0% (85,213)             
  Diana DeGette: 73.8% (272,892)              
  Raymon Anthony Doane: 3.1% (11,606)             
- Election Winner: Diana DeGette              
  Vote Count: 272,892                 
  Percentage: 73.8%

## Election-Audit Summary
This analysis can be used to run the results for any election using the same format of the csv file i.e. a csv file with candidate name as the second index and county name in the third index. In case, the indexes are changed, the code needs to be modified to give accurate results. 
