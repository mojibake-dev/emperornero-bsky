
import time
from atproto import Client
from atproto.xrpc_client.models import AppBskyFeedDefs

# Authenticate with your Bluesky account
client = Client()
client.login('your-handle.bsky.social', 'your-password')

def get_own_post_uris():
    """Fetch URIs of all posts made by the authenticated account."""
    feed = client.app.bsky.feed.get_author_feed({'actor': client.me.did})
    return [post.post.uri for post in feed.feed if hasattr(post, 'post')]

