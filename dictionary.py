import requests

def dictionary(word):
    word = requests.utils.quote(word)
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(api)
    data = response.json()
    
    try:
        details = "--**Word Details**--\n"
        
        for i in data:
            details += "\n**Word:** " + i["word"] + "\n"
            
            # Pronunciations
            if ("phonetics" in i) and (len(i["phonetics"]) > 0):
                details += "\n**Pronunciation{}".format("s:**\n" if (len(i["phonetics"])>1) else ":**")
                for phonetic in i["phonetics"]:
                    details += "- "
                    if "text" in phonetic:
                        if ("audio" in phonetic) and (phonetic["audio"] != ""):
                            details += f"[{phonetic['text']}]({phonetic['audio']})"
                        else:
                            details += f"{phonetic['text']}"
                    elif ("audio" in phonetic) and (phonetic["audio"] != ""):
                        details += f"{phonetic['audio']}"
                    details += "\n"
            
            # Meanings
            for meaning in i["meanings"]:
                details += "\n"
                details += "**Part of Speech:** " + meaning["partOfSpeech"] + "\n"
                # Definitions
                for definition in meaning["definitions"]:
                    details += f"- Definition: `{definition['definition']}`\n"
                    if "example" in definition:
                        details += f"  Example: `{definition['example']}`\n"
    
    except:
        details = "No details found for the word."
    return details
