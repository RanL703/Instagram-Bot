from instagrapi import Client
import time

# Login credentials
USERNAME = 'your_username'
PASSWORD = 'your_pass'

# Message to send
DM_MESSAGE = "Hey there! Heard you wanted coding tips. Here's a link to my YT video and my github!"

# Post URL or ID
POST_URL = 'https://www.instagram.com/p/your_postID'

def login_to_instagram():
    client = Client()
    client.login(USERNAME, PASSWORD)
    return client

def get_post_id(client, post_url):
    # Get post ID from URL
    media_id = client.media_pk_from_url(post_url)
    return media_id

def fetch_comments(client, media_id):
    # Get comments from a specific post
    comments = client.media_comments(media_id)
    return comments

def send_dm_to_users(client, users):
    for user in users:
        try:
            user_id = int(user.pk)  # Ensure user ID is an integer
            client.direct_send(DM_MESSAGE, [user_id])
            print(f"Sent DM to {user.username}")
            time.sleep(10)  # Sleep to avoid rate limiting
        except Exception as e:
            print(f"Error sending DM to {user.username}: {e}")

def main():
    client = login_to_instagram()
    media_id = get_post_id(client, POST_URL)
    comments = fetch_comments(client, media_id)
    
    # Filter users who commented "gib"
    users_to_dm = set()
    for comment in comments:
        if "gib" in comment.text.lower():
            users_to_dm.add(comment.user)

    send_dm_to_users(client, users_to_dm)

if __name__ == "__main__":
    main()