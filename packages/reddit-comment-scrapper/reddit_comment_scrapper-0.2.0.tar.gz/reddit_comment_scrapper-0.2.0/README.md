# Usage

Run 
```
pip install reddit-comment-scrapper
```

Provide the details
```
reddit-comment-scrapper Reddit_ID Reddit_Secret name_subreddit post_category , number_of_posts

## Structure of JSON File

- Each Submission has two entries
    - Submission Body
    - List of Dictionary of top level Replies 
- Each reply has 3 enteries
    - id of reply
    - Body of Reply
    - List of Dictionary of second level Replies

And this goes on Recursively in a depth first search manner till a reply with no further reply is found

JSON File always stored in a comments.json