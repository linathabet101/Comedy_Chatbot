# 🎤 The Roastmaster 3000 - NLP Comedy Chatbot


![Capture d'écran 2025-04-04 105759](https://github.com/user-attachments/assets/d3d9b717-56fc-46e6-8656-6627cdfb778e)



An AI-powered stand-up comedy bot that turns your embarrassing moments into hilarious roasts using advanced NLP techniques.

## About the Project

This project combines:
- **Natural Language Processing** (Groq's Llama 3 model)
- **Voice Processing** (speech-to-text and text-to-speech)
- **Comedic Timing Algorithms**
- **Joke Classification System**

The bot analyzes user input (text or voice) and generates contextually appropriate jokes with perfect comedic delivery.

##  NLP Components

### Core NLP Techniques

1. **Joke Generation**:
```python
# Using Groq's API with carefully crafted prompts
payload = {
    'model': 'llama-3.2-90b-vision-preview',
    'messages': [
        {
            'role': 'system', 
            'content': 'You are a witty stand-up comedian who specializes in turning everyday mishaps into hilarious jokes. Your responses should be:\n- Clever and unexpected\n- Short and punchy\n- Appropriate for general audience\n- Focused on finding humor in the situation'
        },
        {
            'role': 'user', 
            'content': f'Turn this awkward situation into a hilarious joke: {situation}'
        }
    ],
    'max_tokens': 200,
    'temperature': 0.7,  # Creativity level
    'top_p': 0.9        # Diversity of response
}
```
2. **Joke Classification**:
```python
def _analyze_joke_type(self, text):
    """Classifies jokes into 6 categories using lexical analysis"""
    text = text.lower()
    if " i " in text or " me " in text:
        return "self-deprecating"
    elif "?" in text or "why" in text:
        return "observational"
    elif "!" in text or "no way" in text:
        return "shock"
    elif "awkward" in text or "cringe" in text:
        return "awkward"
    elif "you " in text or "your " in text:
        return "roast"
    else:
        return "pun"
```
3. **Comedic Timing System**:
```python
# Dramatic pause implementation
if "..." in text or "?" in text:  # Detects setup-punchline structure
    parts = text.split("...") if "..." in text else text.split("?")
    setup = parts[0] + ("..." if "..." in text else "?")
    punchline = parts[1]
    
    self.engine.setProperty('rate', 145)
    self.engine.say(setup)
    self.engine.runAndWait()
    
    time.sleep(0.8)  # Pause for comedic effect
    
    self.engine.setProperty('rate', 165)
    self.engine.say(punchline)
    self.engine.runAndWait()
```
## Installation
1. **Clone the repository**:
```python
git clone https://github.com/yourusername/roastmaster-3000.git
cd roastmaster-3000
```
2. **Install dependencies**:
```python
pip install -r requirements.txt
```
3. **Create and configure your .env file**:
```python
# Create new .env file
touch .env

# Add these variables (replace with your actual values)
GROQ_API_KEY=your_groq_api_key_here
BACKEND_URL=http://localhost:8000
```
## Usage
1. **Start the backend server**:
```bash
python run_backend.py
```
2. **In a new terminal, start the frontend**:
```bash
python run_frontend.py
```
3. **Interact with the bot**:

- Click "🎙️ Grab Mic" to record your voice

- Or type your setup in the text box

- Press "🚀 Punchline!" to get roasted

##  NLP Model Details

### Base Models
- **Primary**: Groq's Llama 3 (70B parameter variant)
- **Fallback**: Llama 3 8B for faster responses

### Prompt Engineering
- Specialized system prompts for different comedy styles:
  - Roast
  - Pun 
  - Observational
- Contextual memory for follow-up jokes

### Response Parameters
- **Temperature**: 0.7 (optimal creativity)
- **Top-p**: 0.9 (balanced diversity) 
- **Max tokens**: 200 (keeps jokes concise)

### Voice Processing
- Speech-to-text via Google's recognizer
- Text-to-speech with comedic timing adjustments

## Project Structure

```bash
JOKE_ROAST_CHATBOT/
├── backend/                # API server
│   ├── __pycache__/
│   ├── __init__.py
│   └── main.py             # FastAPI endpoints
│
├── frontend/               # User interface
│   ├── __pycache__/
│   ├── __init__.py
│   └── app.py              # Streamlit application
│
├── src/                    # Core functionality
│   ├── __pycache__/
│   ├── __init__.py
│   ├── chatbot.py          # Joke generation logic
│   └── voice_utils.py      # Voice processing
│
├── .env                    # Environment configuration
├── requirements.txt        # Python dependencies
├── run_backend.py          # Backend launcher
└── run_frontend.py         # Frontend launcher
```
## Example
![image](https://github.com/user-attachments/assets/4138c787-5f8e-401a-aaa4-e18a2f20d000)
