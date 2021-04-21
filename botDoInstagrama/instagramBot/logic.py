from bot import *


def start(login, haslo, accounts):

    print(accounts)
    bot = Bot(login, haslo)

    bot.loginn()
    for account in accounts:
        bot.chooseAccount(account)
        friends = bot.getFriends()
        numberOfAccountsForObs = len(friends) / 10

        i = 0
        for friend in friends:
            if(numberOfAccountsForObs > i):
                if(False == bot.isPrivate(friend)):
                    if(bot.checkingAccount()):
                        time.sleep(1)
                        bot.likePhoto()
                        i += 1
            else:
                break

    likes = bot.checkNotifications()
    for like in likes:
        bot.chooseAccount(like)
        time.sleep(3)
        bot.observation()
