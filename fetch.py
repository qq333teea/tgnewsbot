import os
from datetime import datetime, timedelta
from telethon import TelegramClient, events, sync

# number of messages to get
FETCHCOUNT = 10
# time period (def. week)
PERIOD = 7

# friendly debug reminder
errorcount = 0

# channels = ['bloknot_vrn', 'neuralmeduza', 'sosicka', 'shot_shot']
channels = ['sosicka']


def login(api_creds):
    api_id = int(api_creds[0])
    api_hash = api_creds[1]

    return TelegramClient('session_name', api_id, api_hash)


def get_week(channel):
    news = []
    lastweek = datetime.today() - timedelta(days=PERIOD)

    for message in channel:
        # cringe
        thisweek = \
            lastweek.replace(tzinfo=None) \
            < message.date.replace(tzinfo=None)

        if thisweek:
            news.append(message)

    return news


def rateposts(messages):
    global errorcount
    ratings = []

    for message in messages:
        try:
            total = 0
            for reaction in message.reactions.results:
                total += reaction.count

            if not message.video or message.poll:
                ratings.append([message, total])
        except:
            print('Something went wrong! Well anyway...')
            errorcount += 1

    bestposts = sorted(ratings, key=lambda x: x[1], reverse=True)[:3]

    return [post[0] for post in bestposts]


def save(post):
    postdir = os.path.join(os.getcwd(), 'news', str(post.id))

    if not os.path.exists(postdir):
        os.makedirs(postdir)

    # if media save media
    if post.photo:
        post.download_media(file=postdir)

    # save text
    if post.text:
        open(os.path.join(postdir, 'msg'), 'w').write(post.text)

    return 0


def main():
    client = login(open(".api", "r").readlines())
    client.start()
    
    # create channel list including only messages from last week
    for channel in channels:
        messages = client.get_messages(channel, FETCHCOUNT)
        lastweekmsgs = get_week(messages)
        posts = rateposts(lastweekmsgs)

        for post in posts:
            save(post)

    print('Wow, only ', errorcount, 'errors today! FIX YOUR SHIT')


if __name__ == '__main__':
    main()
