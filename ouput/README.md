# w205-assignment-2-updated


Readme / Procedure

Step 1: Acquire Data from Twitter

This code, w205-3.py leverages the Tweepy library to pull up to one week’s worth of Tweets from Twitter using their Rest API and stores the results as text files in a local directly. I used the TweetSerializer provided by Luis in Github to create and open a new text file, write the corresponding tweets, and close the file once complete. For simplicity, I modified the naming convention to include the corresponding hashtag being captured for easier search once complete.

The function that actually uses the Twitter API to capture tweets is called pullTweets and requires a desired string (in this case, “#Trump #GOP”, “#Trump”, “#GOP”) across a corresponding set up dates (as far back as one week due to Twitter API restrictions). To assist with the language analysis, I restricted tweets to the English language. This loop operates until there are no more tweets and the loop will break to continue with its program. The Tweepy library should prevent you from reaching a time-out error, however, I included a 5 minute break in the event a time out error is received for the sake of resiliency.

I initially wanted to chunk in sets of 100 tweets but the number of files relative to their size produced an inefficient result. Instead, I opted to chunk into 1,000 tweets (please note, I restricted my collection to only the tweet text and not any corresponding metadata). I used a modulus function to calculate when 1,000 tweets was reached and the file could be closed. If there are more tweets needing capture after the text file has closed, the Tweet Serializer will open an additional empty text file and continue recording tweets.

I included the three individual call functions in the script to avoid the need to manually run once the function is complete.

Step 2: Uploading to AWS S3

My first attempt at this assignment included an automatic upload to S3. However, I am still working on the appropriate syntax, as such, I manually uploaded my files to S3.

Step 3: Lexicon Analysis and Histogram

I created a second file, frequencyplot.py, that leverages the FreqDist function within NLTK. For time sake I consolidated my earlier files into master files to easily run through the code. I read each file individually, tokenized the words, converted to lowercase (kept getting variations of standard stopwords before doing this), and removed any stopwords. Please note that I appended my stopwords file with the following words, RT, http, https to mitigate risk of irrelevant results. I created an empty dictionary to be filled with the most common words identified by NLTK. I then used the top 50 of these to fill the dictionary and plotted them as a histogram. I made sure to angle the x-axis label at 90 degrees for readability and removed empty space on the sides of the axis by limiting the x-axis range.


S3 Link

https://console.aws.amazon.com/s3/home?region=us-west-2#&bucket=w205-a2-update&prefix=Assignment2-Update/