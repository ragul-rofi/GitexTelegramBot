
# Gitex Bot

## Project Description

Gitex Bot is a Telegram bot that helps you find relevant GitHub repositories for your projects. Simply tell the bot your project idea, and it will search GitHub to provide you with a list of repositories that match your query.

This project was developed with persistence and dedication to automate the process of finding useful repositories using the GitHub API.

## Features
- Searches GitHub repositories based on user input.
- Provides links to relevant repositories directly on Telegram.
- Continuously runs the bot using Render web services for seamless uptime.

## Technologies Used
- **Python**: For the bot logic.
- **Telegram Bot API**: To interact with Telegram users.
- **GitHub API**: To search for repositories.
- **Render**: For continuous deployment and hosting.

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

## Usage
- Start the bot by typing `/start` in your Telegram chat with the bot.
- Enter your project idea or query, and the bot will return a list of GitHub repositories that match your query.

## Contributing
Feel free to open issues or submit pull requests for improvements and features.

## License
This project is licensed under the MIT License.
