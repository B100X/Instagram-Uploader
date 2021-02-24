# pip install instabot

from instabot import Bot


bot = Bot()

bot.login(username = "user_name",
          password = "user_password")
bot.upload_photo("Your_Post.jpg",
                 caption = "Caption of post here")
