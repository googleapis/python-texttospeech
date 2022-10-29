# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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


from google.cloud.texttospeech_v1.services.text_to_speech.async_client import (
    TextToSpeechAsyncClient,
)
from google.cloud.texttospeech_v1.services.text_to_speech.client import (
    TextToSpeechClient,
)
from google.cloud.texttospeech_v1.types.cloud_tts import (
    AudioConfig,
    AudioEncoding,
    CustomVoiceParams,
    ListVoicesRequest,
    ListVoicesResponse,
    SsmlVoiceGender,
    SynthesisInput,
    SynthesizeSpeechRequest,
    SynthesizeSpeechResponse,
    Voice,
    VoiceSelectionParams,
)

__all__ = (
    "TextToSpeechClient",
    "TextToSpeechAsyncClient",
    "AudioConfig",
    "CustomVoiceParams",
    "ListVoicesRequest",
    "ListVoicesResponse",
    "SynthesisInput",
    "SynthesizeSpeechRequest",
    "SynthesizeSpeechResponse",
    "Voice",
    "VoiceSelectionParams",
    "AudioEncoding",
    "SsmlVoiceGender",
)
