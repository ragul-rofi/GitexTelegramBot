# Gitex Bot

Gitex Bot is an intelligent, user-friendly Telegram bot designed to help developers quickly discover GitHub repositories relevant to their project ideas. Simply describe your project or enter a query, and Gitex Bot will search the vast collection of repositories on GitHub and provide you with a curated list of the most relevant results. This automation simplifies the process of finding useful codebases and innovative projects, allowing you to focus on building rather than searching. This project has been developed with persistence and dedication to automate the process of finding useful repositories using both GitHub API and Telegram Bot API.

## Features

- **Instant GitHub Search**: Automatically searches GitHub repositories based on the project idea or keyword you provide.
- **Detailed Repo Information**: Returns repository links, star counts, forks, and descriptions directly in the Telegram chat.
- **Markdown-Formatted Replies**: Clean, organized output that is easy to read and interact with.
- **Real-Time Interaction**: Powered by Telegram's API for seamless and real-time responses.
- **Continuous Deployment**: Hosted on Render, ensuring the bot remains live and accessible around the clock.

## Technologies Used

- **Python**: The core programming language for the bot's logic and operations.
- **Telegram Bot API**: Manages communication between users and the bot.
- **GitHub API**: Utilized to fetch relevant repository data based on user queries.
- **Render**: Provides continuous deployment and hosting services, ensuring that the bot remains operational 24/7.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ragul-rofi/GitexTelegramBot.git
cd GitexTelegramBot
```

### 2. Install dependencies

You need to have Python installed. Then, install the required packages by running:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:

```bash
pip install python-telegram-bot
pip install requests
pip install python-dotenv
```

### 4. Run the bot locally

You can run the bot locally by executing:
```bash
python Gitex.py
```

### 5. Deploying on Render

The bot is deployed on Render for continuous operation. To deploy your bot on Render:
1. Create a new web service on Render.
2. Link your GitHub repository to Render.
3. Add the necessary environment variables on Render’s dashboard.
4. Set the command to run the bot:
   
    ```bash
    python Gitex.py
    ```

## Bot Link

- [![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://t.me/RepoGitEX_BOT)

## Usage

1. **Start the Bot**: Type `/start` in your Telegram chat with Gitex Bot to begin.
2. **Share Your Idea**: Enter your project idea or query to find relevant repositories.
3. **Get Results**: The bot will return a list of GitHub repositories that match your request.

---

## Contributing

Contributions are welcome! Here’s how you can help:

- **Report Issues**: If you find a bug or have a suggestion, open an issue in the repository.
- **Submit Pull Requests**: Feel free to fork the repository, make improvements, and submit a pull request.

Your help is appreciated!

---

## License

This project is licensed under the MIT License. You can use, modify, and distribute it freely, as long as you retain the original copyright and license notices.

