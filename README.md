 # Python Challenge:  Py Me Up, Charlie
UCF Data Analytics and Visualization Boot Camp - Homework 3

This homework encompasses a real-world situation where Python scripting skills come in handy.

## PyBank

 For this challenge, we created a Python script for analyzing the financial records of a company. The set of financial data is given in a file called budget_data.csv.  The dataset is composed of two columns: `Date` and `Profit/Losses`.

 The Python script analyzes the records and calculates each of the following:

  * The total number of months included in the dataset.

  * The net total amount of "Profit/Losses" over the entire period.

  * The changes in "Profit/Losses" over the entire period, then finds the average of those changes.

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

 The script is run from the command line:
  ```
  $python main.py
  ```
  
  Producing the following output:
  
    ```
    Financial Analysis
    --------------------------------------
    Number of Months: 86
    Total profit/loss: 38382578.00
    Average profit/loss change : -2315.12
    Greatest Increase in Profits: 1926159.0, occurred on Feb-2012.
    Greatest Decrease in Profits: -2196167.0, occurred on Sep-2013.
    --------------------------------------
    ```

 The script also sends this output to a text file (.\Resources\pybank_analysis.txt) with these results.

## PyPoll

 In this challenge, we help a rural town modernize its vote counting process.

 The input is a set of poll data called election_data.csv. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The script analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

 The script is run from the command line as: 
  ```
  $python main.py
  ```
  
  Producing the following output:

  ```
	Election Results
	-------------------------
	Total Votes: 3521001
	-------------------------
	Khan : 63.000 (2218231)
	Correy : 20.000 (704200)
	Li : 14.000 (492940)
	O'Tooley : 3.000 (105630)
	-------------------------
	Winner: Khan 
	-------------------------
  ```

 The script also sends this output a text (.\Resources\election_results.txt) file with these results.