import os
import nextcord
import ast
import requests
import logging
import asyncio
import random
import subprocess
from typing import Optional
from dotenv import load_dotenv
from urlextract import URLExtract
from nextcord import Interaction, SlashOption, FFmpegPCMAudio
from nextcord.ext import commands, tasks
from datetime import datetime
from bs4 import BeautifulSoup


intents = nextcord.Intents.all()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix= '!', intents=intents)

load_dotenv()
SUBSCRIPTIONS = ast.literal_eval(os.getenv('SERVER_ID'))
TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CH = os.getenv('WELCOME_CH')
MEMBER_COUNT_CH = os.getenv('MEMBER_COUNT_CH')
EPIC_CHANNEL = os.getenv('EPIC_CHANNEL')
GAMES_FILE = os.getenv('GAMES_FILE') #games.txt
KLEI_LINKS = os.getenv('KLEI_LINKS') #KleiLinks.txt
SET_ROLE_MESSAGE = os.getenv('SET_ROLE_MESSAGE')

Bot_version = "0.4"