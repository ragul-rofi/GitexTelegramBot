# Gitex Bot

Gitex Bot is a Telegram bot that helps users find relevant GitHub repositories based on their project ideas.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your system.
- **pip** for installing Python packages.
- A Telegram bot token (generated through BotFather).
- A GitHub token (generated from your GitHub account).

## Installation

1. **Clone the Repository**:
   Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a `.env` File**:
   Create a file named `.env` in the project directory and add your tokens:
   ```plaintext
   TELEGRAM_TOKEN=your_telegram_token
   GITHUB_TOKEN=your_github_token
   ```

3. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install python-telegram-bot requests
   ```

## Running the Bot

To run the bot, follow these steps:

1. **Open your terminal** and navigate to the project directory.
   
2. **Run the Python script**:
   ```bash
   python Gitex.py
   ```

3. **Start the Bot**:
   Open Telegram and find your bot. Start a chat and type your project idea. The bot will respond with relevant GitHub repository links.

## Usage

- Type a project idea or topic into the chat.
- The bot will search GitHub and return links to relevant public repositories.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
