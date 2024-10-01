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
    await update.message.reply_text('Welcome to Gitex Bot! Provide me with a project idea, and I will search for relevant GitHub repositories.')

def search_git_repo(query: str) -> list:
    headers = {
        'Authorization': f'token {GIT_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/search/repositories?q={query}+in:name,description&per_page=7'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get('items', [])
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
    return []

async def handle_msg(update: Update, context):
    query = update.message.text.strip()
    
    if not query:
        await update.message.reply_text("Please provide a valid query.")
        return
    
    await update.message.reply_text(f'Searching for GitHub repositories related to: {query}...')
    
    repos = search_git_repo(query)
    
    if repos:
        reply_msg = "Here are some repositories I found:\n\n"
        for repo in repos:
            repo_name = repo.get('name', 'N/A')
            repo_url = repo.get('html_url', 'N/A')
            stars = repo.get('stargazers_count', 'N/A')
            forks = repo.get('forks_count', 'N/A')
            description = repo.get('description', 'No description available')
            
            reply_msg += f"🔹 *{repo_name}*\n"
            reply_msg += f"   🌟 Stars: {stars} | 🍴 Forks: {forks}\n"
            reply_msg += f"   🔗 [Link]({repo_url})\n"
            reply_msg += f"   📝 Description: {description}\n\n"
    else:
        reply_msg = "Sorry, I couldn't find any repositories related to your query or an error occurred."

    await update.message.reply_text(reply_msg, parse_mode='Markdown')

def main():
    app = ApplicationBuilder().token(TELE_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

    app.run_polling()

if __name__ == '__main__':
    main()
