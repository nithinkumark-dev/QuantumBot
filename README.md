# QuantumChatBot

QuantumChatBot is an AI-powered conversational assistant designed to provide interactive and intelligent responses. Built with Python and Streamlit, it leverages advanced language models to simulate human-like conversations. The application is deployed and accessible via [Streamlit Cloud](https://quantum-ai-chat.streamlit.app/).

## Demo

Experience the chatbot live: [https://quantum-ai-chat.streamlit.app/](https://quantum-ai-chat.streamlit.app/)

## Features

- **Conversational AI**: Utilizes advanced language models to generate coherent and context-aware responses.
- **Streamlit Interface**: Provides a user-friendly web interface for seamless interactions.
- **Modular Design**: Structured codebase with separate modules for utilities and main application logic.
- **Environment Configuration**: Uses environment variables for secure and flexible configuration.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nithinkumark-dev/QuantumChatBot.git
   cd QuantumChatBot
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   - Rename `.env.example` to `.env`.
   - Populate the `.env` file with the necessary API keys and configurations.

5. **Run the Application**

   ```bash
   streamlit run main.py
   ```

## Deployment

QuantumChatBot is deployed using Streamlit Cloud, enabling easy sharing and accessibility. To deploy your own version:

1. **Push to GitHub**: Ensure your code is committed and pushed to a GitHub repository.

2. **Set Up Streamlit Cloud**:
   - Sign in to [Streamlit Cloud](https://streamlit.io/cloud).
   - Click on "New App" and connect your GitHub repository.
   - Configure the main file path (e.g., `main.py`) and environment variables.

3. **Deploy**: Click "Deploy" to launch your application.

For more detailed guidance, refer to the [Streamlit Deployment Documentation](https://docs.streamlit.io/streamlit-cloud).

## Project Structure

```
QuantumChatBot/
├── .env.example       # Template for environment variables
├── .gitignore         # Specifies files to ignore in Git
├── main.py            # Main application script
├── requirements.txt   # Python dependencies
├── story.txt          # Sample conversation or data
├── utils.py           # Utility functions
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
