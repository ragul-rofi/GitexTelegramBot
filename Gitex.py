import logging
import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


load_dotenv()

TELE_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GIT_TOKEN = os.getenv('GITHUB_TOKEN')


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

if not TELE_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN is not set in the environment variables.")
    exit(1)

if not GIT_TOKEN:
    logger.error("GITHUB_TOKEN is not set in the environment variables.")
    exit(1)



async def start(update: Update, context):
    await update.message.reply_text(
        'Welcome to Gitex Bot! Give me your project idea, and I will find relevant GitHub repositories.')



def search_git_repo(query: str) -> list:
    headers = {
        'Authorization': f'token {GIT_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/search/repositories?q={query}+in:name,description&per_page=7'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        logger.error(f"Error fetching repos: {response.status_code}, {response.text}")
        return []



async def handle_msg(update: Update, context):
    query = update.message.text
    await update.message.reply_text(f'Searching for GitHub repos related to: {query}...')
    repos = search_git_repo(query)

    if repos:
        reply_msg = "Here are some repositories I found:\n\n"
        for repo in repos:
            reply_msg += f"{repo['name']}: {repo['html_url']}\n"
    else:
        reply_msg = "Sorry, I couldn't find any repositories related to your query."

    await update.message.reply_text(reply_msg)



def main():
    app = ApplicationBuilder().token(TELE_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

    app.run_polling()


if __name__ == '__main__':
    main()
