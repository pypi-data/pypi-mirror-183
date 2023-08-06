#import modules
import pyttsx3
import pandas as pd

def spreadsheet_tts(xlsxfile,lower_bound,upper_bound,header=None):
    """Text to speech from rows in Excel file. 

    Args:
        xlsxfile (_type_): Full path to Excel file.
        lower_bound (_type_): Which row should TTS engine start from?
        upper_bound (_type_): Which row should TTS engine end?
        header (_type_, optional): Does header exist in Excel file? Defaults to None.
    """
    
    #import Excel file
    raw_text = pd.read_excel(xlsxfile,header=header)
    
    #rm NaN rows
    raw_text = raw_text.dropna()
    
    #convert df col to list
    text = raw_text[0].tolist()[lower_bound:upper_bound]
    
    engine = pyttsx3.init()

    #TTS for selected rows
    for text in text:
        engine.say(text=text)
    engine.runAndWait()