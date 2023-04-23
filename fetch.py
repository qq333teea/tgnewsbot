import os
from datetime import datetime, timedelta
from telethon import TelegramClient, events, sync

# number of messages to get
FETCHCOUNT = 100
# time period (def. week)
PERIOD = 7

# friendly debug reminder
errorcount = 0

channels = ['bloknot_vrn', 'neuralmeduza', 'sosicka', 'shot_shot', 'tonnakreativa']
horo = 'neural_horo'

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


def picfirst(posts):
    for i, post in enumerate(posts):
        if post.photo:
            del posts[i]
            return [post] + posts


def gendate(date):
    return '\n\n' + date.strftime("%d.%m.%Y %H:%M")

def gentitle(title, channel):
    return '\\byline{' + title + '}{' + channel + '}\n\n'


def photopost(photo, date, text):
    if len(text) > 100:
        return '\\begin{window}[0,r,\\includegraphics[width=1.0in]{' \
            + photo + '}, \\centerline{}] ' + text + date + '\\end{window}\n'
    else:
        return '\\begin{window}[0,c,\\includegraphics[width=2.2in]{' \
            + photo + '}, \\centerline{}]' + date + ' \\end{window}\n'

# place elements insde tex syntax
def gentex(post, fig):
    try:
        title,text = post.raw_text.split("\n", 1)
    except:
        title = post.raw_text
        text = ''

    date = gendate(post.date)
    latex = gentitle(title, post.chat.title)

    if post.photo:
        # post.download returns filepath
        photo = post.download_media(file=fig).split('/')
        latex += photopost('fig/' + photo[len(photo)-1], date, text)
    else:
        latex += text + date

    latex += '\\closearticle\n'

    return latex


def textempl(tex):
    return '''
\\documentclass{article}
\\usepackage[utf8x]{inputenc}
\\usepackage[T2A]{fontenc}
\\usepackage[russian]{babel}
\\usepackage{microtype}
\\usepackage{newspaper}
\\date{\\today}
\\currentvolume{1}
\\currentissue{666}
\\SetPaperName{Acid'n'Shit}
\\SetHeaderName{Acid'n'Shit}
\\SetPaperLocation{Hlevnoe DC}
\\SetPaperSlogan{``Что может быть хуже...''}
\\SetPaperPrice{Zero Rubles}
\\usepackage{graphicx}
\\usepackage{multicol}
\\usepackage{picinpar}
\\usepackage{lipsum}
\\usepackage{fontspec}
\\setmainfont{Symbola}
\\begin{document}
\\maketitle
\\begin{multicols}{3}
''' + tex + '''
\\end{multicols}
\\end{document}
'''

def main():
    posts = []
    lpath = os.path.join(os.getcwd(), 'latex')
    latex = ''

    # open telegram session
    client = login(open(".api", "r").readlines())
    client.start()
    
    # create channel list including only messages from last week
    for channel in channels:
        messages = client.get_messages(channel, FETCHCOUNT)
        lastweekmsgs = get_week(messages)
        posts += rateposts(lastweekmsgs)

    # find first post with a picture 
    posts = picfirst(posts)

    # append ai horoscope
    posts.append(client.get_messages(horo, 1)[0])

    # generate latex source
    for post in posts:
        latex += gentex(post, os.path.join(lpath, 'fig'))

    # write tex source
    open(os.path.join(lpath, 'news.tex'), 'w').write(textempl(latex))

    print(posts)
    
    print('Wow, only ', errorcount, 'errors today! FIX YOUR SHIT')


if __name__ == '__main__':
    main()
