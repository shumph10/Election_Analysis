# Election_Analysis
Local election results and trends analysis with python.

--------------------------------------

## **Project Overview**
A Colorado Board of Education employee asked for report of total number of votes cast, and total votes and percent of votes for each cadidate and county in a local election. From this information the winner based on popular vote would be declared. The county with the largest voter turn out and it's number of votes was also determined. This type of program would be devolped for use in the future, in both local and larger scale elections. Ballots were collected and information was pulled from an excel file into VS code for analysis with python.

--------------------------------------

##**Resources**
-Data Source: [election_results.csv](https://github.com/shumph10/Election_Analysis/blob/main/Resources/election_results.csv)
-Software: Python 3.9.7, Visual Studio Code 1.65.2

--------------------------------------

##**Results**
The analysis of the election show that:
-There were 369,711 total votes cast.
The counties included:
-Jefferson
-Denver
-Arapahoe
The results for number of votes in each county were:
-Jefferson: 38,855 (10.5%)
-Denver: 603,055 (82.8%
-Arapahoe: 24,24,801
-The county with largest number of votes was Denver with 306,055 votes, 82.8% of total votes.
-The candidates included:
   -Charles Casper Stockham
   -Diana DeGette
   -Raymon Anthony Doane
-The candidate's results were:
   -Charles Casper Stockham received 23.0% of votes and 85,213 number of votes.
   Diana DeGetter received 73.8% of votes and 272,892 number of votes.
   Raymon Anthony Doane received 3.1% of votes and 11,606 number of votes.
-The winner of the election was therefore:
   -Diana Degette with 73.8% (272,892) of total votes.
   
![Election_Analysis_results_txt_file_screenshot](https://user-images.githubusercontent.com/100040705/160430655-b9461ec7-3780-441c-be57-c97b3cf42610.png)


The following code was written with Python in VS Code to analyze the election data and output results to the election analysis text document displayed above. Comments throughout code are indicated in green with the # symbol and dictate what each line of code below will accomplish. Print() statements will output to git bash or terminal and txt_file.write() statement will output to the text file. 


![Screenshot_Election_Analysis_Code_1](https://user-images.githubusercontent.com/100040705/160434119-40a78993-641d-4a82-acf3-0ab8a68eeb88.png)
![Screenshot_Election_Analysis_Code_2](https://user-images.githubusercontent.com/100040705/160434128-e223acc7-0eba-44a4-a056-cf521b73000e.png)
![Screenshot_Election_Analysis_Code_3](https://user-images.githubusercontent.com/100040705/160434138-a42d77fb-7ddb-46b4-8489-cf6055a79deb.png)
![Screenshot_Election_Analysis_Code_4](https://user-images.githubusercontent.com/100040705/160434153-8912f77c-db16-4b3c-a26f-6698a5bc4f6e.png)

--------------------------------------

##**Summary**
This script has been shown to accurately and efficentially provide results for local election vote tallies. From the data the candiate and counties vote tallies were pulled to calcuate highest participation and winner of the election. This script could be applied to other local and state elections. The script could be modified to count votes for each candidate within each county, showing perfered winner for each area. It could additionally be modified to loop through election results and ensure no ballot was counted twice by ensuring the ballot ID number only occurs in the data once. If ballot ID numbers are connected to methods of voting, the script could be editted to show which method is most often used. With the results of ballot casting type efforts could be made to make other methods more accessable if needed within the community. 

--------------------------------------

##**Contact Me**

Email: sarahhumphrey2016@outlook.com </br>
[LinkedIn](https://www.linkedin.com/in/sarah-humphrey-data-analyst/)
