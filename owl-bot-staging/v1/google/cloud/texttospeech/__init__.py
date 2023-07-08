# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.texttospeech import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.texttospeech_v1.services.text_to_speech.client import TextToSpeechClient
from google.cloud.texttospeech_v1.services.text_to_speech.async_client import TextToSpeechAsyncClient
from google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.client import TextToSpeechLongAudioSynthesizeClient
from google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.async_client import TextToSpeechLongAudioSynthesizeAsyncClient

from google.cloud.texttospeech_v1.types.cloud_tts import AudioConfig
from google.cloud.texttospeech_v1.types.cloud_tts import CustomVoiceParams
from google.cloud.texttospeech_v1.types.cloud_tts import ListVoicesRequest
from google.cloud.texttospeech_v1.types.cloud_tts import ListVoicesResponse
from google.cloud.texttospeech_v1.types.cloud_tts import SynthesisInput
from google.cloud.texttospeech_v1.types.cloud_tts import SynthesizeSpeechRequest
from google.cloud.texttospeech_v1.types.cloud_tts import SynthesizeSpeechResponse
from google.cloud.texttospeech_v1.types.cloud_tts import Voice
from google.cloud.texttospeech_v1.types.cloud_tts import VoiceSelectionParams
from google.cloud.texttospeech_v1.types.cloud_tts import AudioEncoding
from google.cloud.texttospeech_v1.types.cloud_tts import SsmlVoiceGender
from google.cloud.texttospeech_v1.types.cloud_tts_lrs import SynthesizeLongAudioMetadata
from google.cloud.texttospeech_v1.types.cloud_tts_lrs import SynthesizeLongAudioRequest
from google.cloud.texttospeech_v1.types.cloud_tts_lrs import SynthesizeLongAudioResponse

__all__ = ('TextToSpeechClient',
    'TextToSpeechAsyncClient',
    'TextToSpeechLongAudioSynthesizeClient',
    'TextToSpeechLongAudioSynthesizeAsyncClient',
    'AudioConfig',
    'CustomVoiceParams',
    'ListVoicesRequest',
    'ListVoicesResponse',
    'SynthesisInput',
    'SynthesizeSpeechRequest',
    'SynthesizeSpeechResponse',
    'Voice',
    'VoiceSelectionParams',
    'AudioEncoding',
    'SsmlVoiceGender',
    'SynthesizeLongAudioMetadata',
    'SynthesizeLongAudioRequest',
    'SynthesizeLongAudioResponse',
)
