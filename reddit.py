import praw
from datetime import datetime
import json
import os
# Debug: Print Python and PRAW versions

# Initialize PRAW
try:
    reddit = praw.Reddit(
        client_id="KEMwe-SsNMaGB8AXPVckSQ",          
        client_secret="ig2Wf6TtX9pShb7bwzTfvcMuBHD0Ug",  
        user_agent="windows:ai_reddit_bot:v1.0 (by /u/New-Baseball7341)"     # Replace with your user agent
    )
    print("PRAW initialized successfully!")
except Exception as e:
    print(f"Error initializing PRAW: {e}")
    exit()

# Specify the subreddit
try:
    subreddit = reddit.subreddit("cybersecurity")
    print(f"Accessing subreddit: {subreddit.display_name}")
except Exception as e:
    print(f"Error accessing subreddit: {e}")
    exit()

# List to store post data
posts_data = []

# Fetch hot posts (you can change to .new(), .top(), etc.)
try:
    for post in subreddit.hot(limit=10):  # Adjust the limit as needed
        # Extract post details
        post_details = {
            "title": post.title,
            "score": post.score,
            "date": datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            "post_text": post.selftext  # Text content of the post
        }
        posts_data.append(post_details)
    print("Posts fetched successfully!")
except Exception as e:
    print(f"Error fetching posts: {e}")
    exit()

# Save the data to a new JSON file
output_file = "reddit_posts.json"
if os.path.exists(output_file):
    # Load existing data
    with open(output_file, "r") as json_file:
        existing_data = json.load(json_file)
    # Append new data to existing data
    existing_data.extend(posts_data)
    # Save the updated data back to the file
    with open(output_file, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)
else:
    # If the file doesn't exist, create it and write the new data
    with open(output_file, "w") as json_file:
        json.dump(posts_data, json_file, indent=4)

print(f"Data saved to {output_file}")