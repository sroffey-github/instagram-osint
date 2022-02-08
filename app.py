from instaloader import Profile, Post
from dotenv import load_dotenv
import instaloader, os, sys

load_dotenv()

USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')

try:
    target = sys.argv[1] # instangram account
except:
    print('[!] Error, no target supplied.')
    exit()

instance = instaloader.Instaloader()

#login
print('[i] Logging in...')
instance.login(user=USERNAME, passwd=PASSWORD)

# target profile
profile = Profile.from_username(instance.context, username=target)

# download entire profile
instance.download_profile(profile_name=target)

# download stories
instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))

# download hightlights
for highlight in instance.get_highlights(user=profile):
    for item in highlight.get_items():
        instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

# download saved posts
instance.download_saved_posts()