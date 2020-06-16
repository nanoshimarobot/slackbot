from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('私は(.*)です')
@respond_to('わたしは(.*)です')
def hello(message,something):
    message.reply('まぁ！あなた{0}さんっていいますのね!!'.format(something))

@respond_to('(.*)')
def other(message, something):
    m = re.search('にゃーん',something)
    if m:
        message.reply('貴様のような高専生の分際で猫様の鳴き声を真似るか小僧')
    else:
        message.reply('わいはおぜうさま')
