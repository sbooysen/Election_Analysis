# PyPoll Challenge

### By: Stacey Booysen


The goal in this challenge was to provide easily digestible results for an election audit. There were three main candidates and three main counties involved in the election. The task was to use ‘with’ and ‘for’ statements to help the data run together smoothly. We calculated both the total votes overall and the votes per candidate and per county. We then displayed the numbers in their percentages to help further illustrate the differences between the voting amounts.

* There were a total of 369,711 votes.
* Votes per Count:
    *	Jefferson: 10.5% (38,855)
    *	Denver: 82.8% (306,055)
    *	Arapahoe: 6.7% (24,801)
*	Denver had the highest turnout of all three counties.
*	Votes per Candidate:
    *	Charles Casper Stockham: 23.0% (85,213)
    *	Diana DeGette: 73.8% (272,892)
    *	Raymon Anthony Doane: 3.1% (11,606)
*	The winning candidate was Diana Degette with the following vote count and percentage:
    *	Vote Count: 272,892
    *	Percentage: 73.8%
    *	
All this can be seen in the outcome of the script below:

![Exampl](https://github.com/sbooysen/Election_Analysis/blob/6ad9ccc61ff41dbed8024c6fd273cb5ebf01e89a/Election%20Results%20Output.png)

To modify the python script for future use, there are a few things that will need to be altered. One item that would need to be changed per the dataset, is the source file that the code is working off of. The script needs to have clear access to the new file with the new data in order to run the necessary information. An example of the code formatting for reaching these files is below:
```
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

Another change that might need to be made is the addition or subtraction of loops. If only the number of votes for candidates are needed, then they would need to remove the section with the county votes. If they wanted to add more elements to the analysis, they would need to provide another loop.

Overall, this is a solid base to have for running election audits. While we only used it for three candidates, it is easily adapted for use with larger datasets. With an easy-to-read outcome, the election auditor and the committee they work with, should be able to run more and more of these scripts in the future. In the end, it made everything more concise, helping the results become more clean and clear-cut for anyone to assess.
