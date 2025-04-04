import speech_recognition as sr
import pyttsx3
import streamlit as st
import tempfile
import random
import time

class VoiceProcessor:
    def __init__(self):
        """Initialize voice processing with comedic timing"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
        
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'david' in voice.name.lower() or 'zira' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        # Comedic timing settings:
        self.engine.setProperty('rate', 155)
        self.engine.setProperty('volume', 1.0)
        
        # Sound effects matched to joke types:
        self.joke_reactions = {
            "self-deprecating": ("Womp womp... 🥁", 0.7),
            "observational": ("Oh ho ho! 🤭", 0.8),
            "shock": ("NO WAY! 😲", 1.2), 
            "awkward": ("Yiiiikes... 🙈", 0.6),
            "roast": ("BURN! 🔥", 1.1),
            "pun": ("Groan... 😩", 0.5)
        }

    def _analyze_joke_type(self, text):
        """Determine what kind of joke this is"""
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

    def deliver_response(self, text):
        """Deliver joke with perfect comedic timing"""
        try:
            # Analyzing joke type 
            joke_type = self._analyze_joke_type(text)
            reaction, speed = self.joke_reactions[joke_type]
            
            # Setup pause before punchline
            if "..." in text or "?" in text:
                parts = text.split("...") if "..." in text else text.split("?")
                setup = parts[0] + ("..." if "..." in text else "?")
                punchline = parts[1]
                
                
                self.engine.setProperty('rate', 145)
                self.engine.say(setup)
                self.engine.runAndWait()
                
                time.sleep(0.8) # Dramatic pause
                
                self.engine.setProperty('rate', 165)
                self.engine.say(punchline)
                self.engine.runAndWait()
            else:
                
                self.engine.say(text)
                self.engine.runAndWait()
            
            # Adding a reaction
            self.engine.setProperty('rate', int(155 * speed))
            self.engine.say(reaction)
            self.engine.runAndWait()
            
            return reaction.split()[-1]  # Return just the emoji
            
        except Exception as e:
            st.warning(f"Comedy malfunction: {str(e)}")
            return "🤖"  # Default emoji on error

    def speech_to_text(self):
        """Record user input with comedic prompt"""
        with sr.Microphone() as source:
            st.session_state.recording_status = "🎤 Set up your joke... I'm ready!"
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=7, phrase_time_limit=15)
                
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    f.write(audio.get_wav_data())
                    temp_path = f.name
                
                text = self.recognizer.recognize_google(audio)
                st.session_state.recording_status = "✅ Got it! Processing hilarity..."
                return text, temp_path
                
            except sr.UnknownValueError:
                st.session_state.recording_status = "🤨 That's not a joke... try again?"
                return None, None
            except Exception as e:
                st.session_state.recording_status = f"🤖 Technical oopsie: {str(e)}"
                return None, None