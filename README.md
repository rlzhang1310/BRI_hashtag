# BRI_hashtag

## Research Question 
What are the most frequently tweeted hashtags in each dataset?

How similar are the hashtags between APAC datasets?
## File Overview

### hashtag_data
results for each dataset

### TMRC14_hashtag.ipynb
code to extract the most frequently tweeted hashtags in the TMRC dataset

run this file by inputting your access_key_id and secret_access_key in cell 2

make sure to install all necessary libraries in cell 1

specify the right path for downloading the data in the last cell

### TMRC14_jaccard.ipynb
code to find the Jaccard's similarity of hashtags and retweets between APAC datasets

make sure to have data downloaded and specify the correct path in cell 2 (comment out retweet data in cell 3 if unneeded)

### case_insensitive_combiner.py
python code which turns hashtag data into case insensitive

Note: This code will replace your original file !!

specify the path correctly in line 6

### twitterei_hashtag.ipynb
code to extract the most frequently tweeted hashtags in the twitterei dataset

run this file by inputting your access_key_id and secret_access_key in cell 2

make sure to install all necessary libraries in cell 1

specify the right path for downloading the data in the last cell
