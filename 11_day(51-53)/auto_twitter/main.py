from get_internet_speed import InternetSpeedTwitterBot


bot = InternetSpeedTwitterBot()

internet_speed = bot.get_internet_speed()

bot.twitter_login()

if internet_speed[0] < 150 or internet_speed[1] < 80:
    bot.tweet_at_provider(internet_speed)