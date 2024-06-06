# ai_rasa

This project is a Rasa-based chatbot integrated with OpenAI's GPT API. The bot handles various intents and uses GPT API to generate responses to complex questions.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Training](#training)
- [Running the Bot](#running-the-bot)
- [Project Structure](#project-structure)
- [Adding New Intents](#adding-new-intents)
- [License](#license)

## Installation

### Prerequisites
- Python 3.7 or later
- pip
- An OpenAI API key

### Steps
1. Clone the repository:
```sh
git clone https://github.com/yx-fan/ai_rasa.git
cd ai_rasa
```

2. Create a virtual environment and activate it:
```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Install `python-dotenv` for loading environment variables from a `.env` file:
```sh
pip install python-dotenv
```

## Configuration

### OpenAI API Key
Create a `.env` file in the root directory of your project and add your OpenAI API key:
```sh
OPENAI_API_KEY=your_openai_api_key
```

### Rasa Configuration
- **NLU and Policies**: Configured in `config.yml`
- **Domain**: Defined in `domain.yml`
- **Intents and Responses**: Defined in `data/nlu.yml`, `data/stories.yml`, and `domain.yml`

### Action Server Configuration
Ensure `endpoints.yml` is configured correctly:
```yaml
action_endpoint:
  url: "http://localhost:5055/webhook"
```

## Training
Train the Rasa model with the following command:
```sh
rasa train
```
This command will create a model in the `models` directory.

## Running the Bot
1. Start the Rasa server:
```sh
rasa run
```

2. Start the action server:
```sh
rasa run actions
```

3. (Optional) To interact with the bot using Rasa Shell:
```sh
rasa shell
```

## Project Structure
```
ai_rasa/
├── actions/                # Custom actions
│   ├── __init__.py
│   ├── actions.py
│   └── actionUseGPT.py     # Action to use OpenAI's GPT API
├── data/
│   ├── nlu.yml             # NLU training data
│   ├── stories.yml         # Conversation training data
├── models/                 # Trained models
├── .env                    # Environment variables
├── config.yml              # Rasa configuration
├── domain.yml              # Domain configuration
├── endpoints.yml           # Action server configuration
├── requirements.txt        # Python dependencies
└── README.md
```

## Adding New Intents
1. Add new intents to `data/nlu.yml`:
```yaml
nlu:
- intent: greet
  examples: |
    - Hi
    - Hello
    - Hey
```

2. Add responses to `domain.yml`:
```yaml
responses:
  utter_greet:
    - text: "Hello! How can I help you today?"
```

3. Add stories to `data/stories.yml`:
```yaml
stories:
- story: greet
  steps:
  - intent: greet
  - action: utter_greet
```

4. Register custom actions in `domain.yml`:
```yaml
actions:
    - actionUseGPT
```

5. Define custom actions in `actions/actions.py`:

6. Train the model:
```sh
rasa train
```

7. Run the bot:
```sh
rasa run
rasa run actions
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
