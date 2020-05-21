# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

from unittest import mock

import grpc
import math
import pytest

from google import auth
from google.api_core import client_options
from google.api_core import grpc_helpers
from google.auth import credentials
from google.cloud.texttospeech_v1beta1.services.text_to_speech import TextToSpeechClient
from google.cloud.texttospeech_v1beta1.services.text_to_speech import transports
from google.cloud.texttospeech_v1beta1.types import cloud_tts
from google.oauth2 import service_account


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert TextToSpeechClient._get_default_mtls_endpoint(None) is None
    assert (
        TextToSpeechClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    )
    assert (
        TextToSpeechClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        TextToSpeechClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        TextToSpeechClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert TextToSpeechClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


def test_text_to_speech_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = TextToSpeechClient.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = TextToSpeechClient.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == "texttospeech.googleapis.com:443"


def test_text_to_speech_client_client_options():
    # Check that if channel is provided we won't create a new one.
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_transport_class"
    ) as gtc:
        transport = transports.TextToSpeechGrpcTransport(
            credentials=credentials.AnonymousCredentials()
        )
        client = TextToSpeechClient(transport=transport)
        gtc.assert_not_called()

    # Check mTLS is not triggered with empty client options.
    options = client_options.ClientOptions()
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_transport_class"
    ) as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = TextToSpeechClient(client_options=options)
        transport.assert_called_once_with(
            credentials=None, host=client.DEFAULT_ENDPOINT
        )

    # Check mTLS is not triggered if api_endpoint is provided but
    # client_cert_source is None.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.TextToSpeechGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = TextToSpeechClient(client_options=options)
        grpc_transport.assert_called_once_with(
            api_mtls_endpoint=None,
            client_cert_source=None,
            credentials=None,
            host="squid.clam.whelk",
        )

    # Check mTLS is triggered if client_cert_source is provided.
    options = client_options.ClientOptions(
        client_cert_source=client_cert_source_callback
    )
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.TextToSpeechGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = TextToSpeechClient(client_options=options)
        grpc_transport.assert_called_once_with(
            api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
            client_cert_source=client_cert_source_callback,
            credentials=None,
            host=client.DEFAULT_ENDPOINT,
        )

    # Check mTLS is triggered if api_endpoint and client_cert_source are provided.
    options = client_options.ClientOptions(
        api_endpoint="squid.clam.whelk", client_cert_source=client_cert_source_callback
    )
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.TextToSpeechGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = TextToSpeechClient(client_options=options)
        grpc_transport.assert_called_once_with(
            api_mtls_endpoint="squid.clam.whelk",
            client_cert_source=client_cert_source_callback,
            credentials=None,
            host="squid.clam.whelk",
        )


def test_text_to_speech_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.TextToSpeechGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = TextToSpeechClient(client_options={"api_endpoint": "squid.clam.whelk"})
        grpc_transport.assert_called_once_with(
            api_mtls_endpoint=None,
            client_cert_source=None,
            credentials=None,
            host="squid.clam.whelk",
        )


def test_list_voices(transport: str = "grpc"):
    client = TextToSpeechClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = cloud_tts.ListVoicesRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_voices), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_tts.ListVoicesResponse()

        response = client.list_voices(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_tts.ListVoicesResponse)


def test_list_voices_flattened():
    client = TextToSpeechClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_voices), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_tts.ListVoicesResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.list_voices(language_code="language_code_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].language_code == "language_code_value"


def test_list_voices_flattened_error():
    client = TextToSpeechClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_voices(
            cloud_tts.ListVoicesRequest(), language_code="language_code_value"
        )


def test_synthesize_speech(transport: str = "grpc"):
    client = TextToSpeechClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = cloud_tts.SynthesizeSpeechRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.synthesize_speech), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_tts.SynthesizeSpeechResponse(
            audio_content=b"audio_content_blob"
        )

        response = client.synthesize_speech(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_tts.SynthesizeSpeechResponse)
    assert response.audio_content == b"audio_content_blob"


def test_synthesize_speech_flattened():
    client = TextToSpeechClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.synthesize_speech), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_tts.SynthesizeSpeechResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.synthesize_speech(
            input=cloud_tts.SynthesisInput(text="text_value"),
            voice=cloud_tts.VoiceSelectionParams(language_code="language_code_value"),
            audio_config=cloud_tts.AudioConfig(
                audio_encoding=cloud_tts.AudioEncoding.LINEAR16
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].input == cloud_tts.SynthesisInput(text="text_value")
        assert args[0].voice == cloud_tts.VoiceSelectionParams(
            language_code="language_code_value"
        )
        assert args[0].audio_config == cloud_tts.AudioConfig(
            audio_encoding=cloud_tts.AudioEncoding.LINEAR16
        )


def test_synthesize_speech_flattened_error():
    client = TextToSpeechClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.synthesize_speech(
            cloud_tts.SynthesizeSpeechRequest(),
            input=cloud_tts.SynthesisInput(text="text_value"),
            voice=cloud_tts.VoiceSelectionParams(language_code="language_code_value"),
            audio_config=cloud_tts.AudioConfig(
                audio_encoding=cloud_tts.AudioEncoding.LINEAR16
            ),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.TextToSpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    with pytest.raises(ValueError):
        client = TextToSpeechClient(
            credentials=credentials.AnonymousCredentials(), transport=transport
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.TextToSpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    client = TextToSpeechClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = TextToSpeechClient(credentials=credentials.AnonymousCredentials())
    assert isinstance(client._transport, transports.TextToSpeechGrpcTransport)


def test_text_to_speech_base_transport():
    # Instantiate the base transport.
    transport = transports.TextToSpeechTransport(
        credentials=credentials.AnonymousCredentials()
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = ("list_voices", "synthesize_speech")
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())


def test_text_to_speech_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        TextToSpeechClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",)
        )


def test_text_to_speech_host_no_port():
    client = TextToSpeechClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="texttospeech.googleapis.com"
        ),
        transport="grpc",
    )
    assert client._transport._host == "texttospeech.googleapis.com:443"


def test_text_to_speech_host_with_port():
    client = TextToSpeechClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="texttospeech.googleapis.com:8000"
        ),
        transport="grpc",
    )
    assert client._transport._host == "texttospeech.googleapis.com:8000"


def test_text_to_speech_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")

    # Check that if channel is provided, mtls endpoint and client_cert_source
    # won't be used.
    callback = mock.MagicMock()
    transport = transports.TextToSpeechGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=callback,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert not callback.called


@mock.patch("grpc.ssl_channel_credentials", autospec=True)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_text_to_speech_grpc_transport_channel_mtls_with_client_cert_source(
    grpc_create_channel, grpc_ssl_channel_cred
):
    # Check that if channel is None, but api_mtls_endpoint and client_cert_source
    # are provided, then a mTLS channel will be created.
    mock_cred = mock.Mock()

    mock_ssl_cred = mock.Mock()
    grpc_ssl_channel_cred.return_value = mock_ssl_cred

    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    transport = transports.TextToSpeechGrpcTransport(
        host="squid.clam.whelk",
        credentials=mock_cred,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=client_cert_source_callback,
    )
    grpc_ssl_channel_cred.assert_called_once_with(
        certificate_chain=b"cert bytes", private_key=b"key bytes"
    )
    grpc_create_channel.assert_called_once_with(
        "mtls.squid.clam.whelk:443",
        credentials=mock_cred,
        ssl_credentials=mock_ssl_cred,
        scopes=("https://www.googleapis.com/auth/cloud-platform",),
    )
    assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "api_mtls_endpoint", ["mtls.squid.clam.whelk", "mtls.squid.clam.whelk:443"]
)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_text_to_speech_grpc_transport_channel_mtls_with_adc(
    grpc_create_channel, api_mtls_endpoint
):
    # Check that if channel and client_cert_source are None, but api_mtls_endpoint
    # is provided, then a mTLS channel will be created with SSL ADC.
    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    # Mock google.auth.transport.grpc.SslCredentials class.
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        mock_cred = mock.Mock()
        transport = transports.TextToSpeechGrpcTransport(
            host="squid.clam.whelk",
            credentials=mock_cred,
            api_mtls_endpoint=api_mtls_endpoint,
            client_cert_source=None,
        )
        grpc_create_channel.assert_called_once_with(
            "mtls.squid.clam.whelk:443",
            credentials=mock_cred,
            ssl_credentials=mock_ssl_cred,
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
        )
        assert transport.grpc_channel == mock_grpc_channel
