import logging
from venv import logger
import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, MessageHandler, filters , ContextTypes

load_dotenv('config/.env')
tele_token = os.getenv('TELEGRAM_BOT_TOKEN')
git_token = os.getenv('GITHUB_TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to Gitex Bot! Tell me your project idea and let me find the relevant Git repo for you! ;-)')

def search_git_repo(query):
    headers = {
        'Authorization' : f'token {git_token}',
        'Accept' : 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/search/repositories?q={query}+in:name,description'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        logger.error(f"Error fetching repo my buddy! :-( : {response.status_code}, {response.text}")
        return []

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text
    await update.message.reply_text(f'Searching for the repo related to your query: {query}...')
    repos = search_git_repo(query)

    if repos:
        reply_msg = "I found some public repo:\n\n"
        for repo in repos[:7]:
            reply_msg += f"{repo['name']}: {repo['html_url']}\n"

    else:
        reply_msg = "No public repos found!"
    await update.message.reply_text(reply_msg)

def main() -> None:
    app = ApplicationBuilder().token(tele_token).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

    app.run_polling()
if __name__ == '__main__':
    main()




