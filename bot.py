import discord


def read_token() :
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

#bot.py
import os
import random

from discord.ext import commands

client.login(process.env.BOT_TOKEN);

token = os.getenv('NjgyOTM3NDI4MjgxMTMxMDE4.XlkUkQ.NMXn12DFjp2FCsmnJeMQQxTQixA')
