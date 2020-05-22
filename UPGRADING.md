

<!-- WIP, to be moved to google-cloud-python repository --->

# Method Calls

Methods now expect request objects. We provide a script that will convert most common cases automatically. 

1. Install the library

```py
python3 -m pip install google-cloud-text-to-speech
```

2. `fixup_keywords.py` is shipped with the library. The script expects
an input directory (with the code to convert) and an empty destination directory.

```sh
$ fixup_keywords.py --input-directory .samples/ --output-directory samples/
```

Before:
```py
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
voices = client.list_voices(language_code="no")
```

After:
```py
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
voices = client.list_voices(request={"language_code": "no"})
```

# Location of Types and Enums

Types and Enums are available at the top level.

Before:
```py

from google.cloud import texttospeech

voice = texttospeech.types.VoiceSelectionParams(language_code="en-US")
encoding = texttospeech.enums.AudioEncoding.MP3
```


After:
```py
from google.cloud import texttospeech

voice = texttospeech.VoiceSelectionParams(language_code="en-US")
encoding = texttospeech.AudioEncoding.MP3
```
