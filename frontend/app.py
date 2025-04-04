import streamlit as st
import requests
import os
import random
from dotenv import load_dotenv
from src.voice_utils import VoiceProcessor

class VoiceComedicApp:
    def __init__(self):
        """Initialize the comedy club"""
        load_dotenv()
        self.backend_url = os.getenv('BACKEND_URL', 'http://localhost:8000')
        self.voice_processor = VoiceProcessor()
        self.joke_styles = {
            "self-deprecating": "🤦",
            "observational": "👀", 
            "shock": "😱",
            "awkward": "😅",
            "roast": "🔥",
            "pun": "💀"
        }

    def generate_comedy_response(self, situation):
        """Get professionally crafted joke"""
        with st.spinner("🎭 Consulting the comedy gods..."):
            try:
                response = requests.post(
                    f"{self.backend_url}/generate-comedy",
                    json={
                        "situation": situation,
                        "style": random.choice(list(self.joke_styles.keys()))
                    },
                    timeout=12
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                return {
                    "comedy_response": f"My joke writer quit! {e}",
                    "style": "awkward"
                }

    def run(self):
        """Run the comedy show"""
        st.title("🎤 The Roastmaster 3000")
        
        
        if 'history' not in st.session_state:
            st.session_state.history = []
        if 'recording_status' not in st.session_state:
            st.session_state.recording_status = "🤫 Psst... tell me something embarrassing"
        
        
        with st.expander("🎭 Open Mic Night", expanded=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                
                st.subheader("🎤 Improv Set")
                st.write(st.session_state.recording_status)
                
                if st.button("🎙️ Grab Mic"):
                    user_input, audio_path = self.voice_processor.speech_to_text()
                    
                    if user_input:
                        
                        joke_data = self.generate_comedy_response(user_input)
                        reaction_emoji = self.voice_processor.deliver_response(
                            joke_data["comedy_response"]
                        )
                        
                        
                        style_emoji = self.joke_styles.get(joke_data.get("style"), "🎭")
                        combined_emoji = f"{style_emoji} {reaction_emoji}"
                        
                        st.session_state.history.append(
                            (user_input, joke_data["comedy_response"], combined_emoji)
                        )
                        
                        st.markdown(f"**You:** _{user_input}_")
                        st.audio(audio_path, format='audio/wav')
                        st.markdown(f"**🤖 {combined_emoji}:** {joke_data['comedy_response']}")
                
                
                st.subheader("📝 Submit Joke")
                text_input = st.text_area("Or type your setup...")
                if st.button("🚀 Punchline!"):
                    if text_input:
                        joke_data = self.generate_comedy_response(text_input)
                        reaction_emoji = self.voice_processor.deliver_response(
                            joke_data["comedy_response"]
                        )
                        style_emoji = self.joke_styles.get(joke_data.get("style"), "🎭")
                        
                        st.session_state.history.append(
                            (text_input, joke_data["comedy_response"], f"{style_emoji} {reaction_emoji}")
                        )
                        st.markdown(f"**🤖 {style_emoji} {reaction_emoji}:** {joke_data['comedy_response']}")

            
            with col2:
                st.subheader("📜 Set List")
                if not st.session_state.history:
                    st.write("No bits yet... break the ice!")
                for i, (setup, punchline, emojis) in enumerate(st.session_state.history):
                    st.markdown(f"**{i+1}. {emojis}**")
                    st.caption(f"_{setup}_")
                    st.write(punchline)
                    st.divider()

def main():
    app = VoiceComedicApp()
    app.run()

if __name__ == "__main__":
    main()