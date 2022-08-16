#2020-08-17 WIP
from gtts import gTTS                                       # Import the required module for text to speech conversion
import os  

class w_tts:
    """Super class for Text 2 Speech. Contains <test> and <file> per instance.
    
    Args:
        text (str)
        file (str)
    Returns:
        <none> 
    """
    def __init__(self, a_text, a_file, a_language) -> None:
        self.w_text = a_text
        self.w_file = a_file
        self.w_language = a_language

    def __repr__(self) -> str:
        """Returns a string representation of the w_tss when print(self) is called."""
        return(f"Text : {self.w_text}\nFile: {self.w_file}")

    def convert_text_2_speech(self):
        myobj = gTTS(text=self.w_text, lang=self.w_language, slow=False)
        myobj.save(self.w_file)  

    def play_file(self):
        os.system(self.w_file)

    def update_text(self, a_text):
        w_text = a_text

    def update_file(self, a_file):
        w_file = a_file