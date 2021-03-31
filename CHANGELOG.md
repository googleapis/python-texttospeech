# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-texttospeech/#history

## [2.3.0](https://www.github.com/googleapis/python-texttospeech/compare/v2.2.0...v2.3.0) (2021-03-31)


### Features

* add `from_service_account_info` to clients ([139e6e8](https://www.github.com/googleapis/python-texttospeech/commit/139e6e8511cdce4c0be7983520f7efc47092f3b1))
* Add ALAW support on client library and improve the ListVoiceRequest message's documentation ([#113](https://www.github.com/googleapis/python-texttospeech/issues/113)) ([8bbd380](https://www.github.com/googleapis/python-texttospeech/commit/8bbd38014fe796b30f4b12ae9432d3a05c130063))
* add common resource helper methods ([139e6e8](https://www.github.com/googleapis/python-texttospeech/commit/139e6e8511cdce4c0be7983520f7efc47092f3b1))
* support custom client info ([#82](https://www.github.com/googleapis/python-texttospeech/issues/82)) ([0612793](https://www.github.com/googleapis/python-texttospeech/commit/06127932a920f6318db8f25d6430755b35d09bb5))


### Bug Fixes

* change default retry and timeout settings ([139e6e8](https://www.github.com/googleapis/python-texttospeech/commit/139e6e8511cdce4c0be7983520f7efc47092f3b1))


### Documentation

* use sphinx-1.5.5 for sphinx-docfx-yaml ([#89](https://www.github.com/googleapis/python-texttospeech/issues/89)) ([feb04c5](https://www.github.com/googleapis/python-texttospeech/commit/feb04c50b56c2c3359b92d8b5887c8ee50be2b95))

## [2.2.0](https://www.github.com/googleapis/python-texttospeech/compare/v2.1.0...v2.2.0) (2020-08-10)


### Features

* incorporate upstream changes ([#73](https://www.github.com/googleapis/python-texttospeech/issues/73)) ([8ee5447](https://www.github.com/googleapis/python-texttospeech/commit/8ee544740f18497d9925bcf77e5ab96695503589))
    * support MULAW audio encoding
    * support MP3_64_KBPS audio encoding
    * support timepointing via SSML tag
    * support quota_project_id

## [2.1.0](https://www.github.com/googleapis/python-texttospeech/compare/v2.0.0...v2.1.0) (2020-06-20)


### Features

* add async client ([#53](https://www.github.com/googleapis/python-texttospeech/issues/53)) ([887d8d5](https://www.github.com/googleapis/python-texttospeech/commit/887d8d501ce9255fee44170b5fc40ebfb1ea953d))


### Documentation

* change relative URLs to absolute URLs to fix broken links ([#40](https://www.github.com/googleapis/python-texttospeech/issues/40)) ([b68df44](https://www.github.com/googleapis/python-texttospeech/commit/b68df446daa7983cad1d31553ece6df569c932b2))

## [2.0.0](https://www.github.com/googleapis/python-texttospeech/compare/v1.0.1...v2.0.0) (2020-06-01)


### ⚠ BREAKING CHANGES

* This release has breaking changes. See the [2.0.0 Migration Guide](https://github.com/googleapis/python-texttospeech/blob/master/UPGRADING.md#200-migration-guide) for details.

### Features

* regenerate with microgenerator ([#30](https://www.github.com/googleapis/python-texttospeech/issues/30)) ([3181b55](https://www.github.com/googleapis/python-texttospeech/commit/3181b55733da7aecde37009a0dd77117434deceb))


### Bug Fixes

* address PR comments ([65f903b](https://www.github.com/googleapis/python-texttospeech/commit/65f903b00395716fad272ca4fc973755735e1e20))

### [1.0.1](https://www.github.com/googleapis/python-texttospeech/compare/v1.0.0...v1.0.1) (2020-02-28)


### Bug Fixes

* update url in setup.py ([#13](https://www.github.com/googleapis/python-texttospeech/issues/13)) ([dc17707](https://www.github.com/googleapis/python-texttospeech/commit/dc17707c41feb885d94f1045ef14e4b9e0898716))

## [1.0.0](https://www.github.com/googleapis/python-texttospeech/compare/v0.5.0...v1.0.0) (2020-02-28)


### Features

* bump release status to GA ([#9](https://www.github.com/googleapis/python-texttospeech/issues/9)) ([03a639e](https://www.github.com/googleapis/python-texttospeech/commit/03a639e16256d9211c1fe88991440f2cc22eccd6))

## 0.5.0

07-24-2019 17:48 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8407](https://github.com/googleapis/google-cloud-python/pull/8407))
- Reformat protos, update nox session docs (via synth). ([#7941](https://github.com/googleapis/google-cloud-python/pull/7941))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add 'client_options' support (via synth). ([#8525](https://github.com/googleapis/google-cloud-python/pull/8525))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Repair top-level API reference page. ([#8435](https://github.com/googleapis/google-cloud-python/pull/8435))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))

### Internal / Testing Changes
- Pin black version (via synth). ([#8599](https://github.com/googleapis/google-cloud-python/pull/8599))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8367](https://github.com/googleapis/google-cloud-python/pull/8367))
- Add disclaimer to auto-generated template files (via synth).  ([#8331](https://github.com/googleapis/google-cloud-python/pull/8331))
- Blacken (via synth). ([#8281](https://github.com/googleapis/google-cloud-python/pull/8281))

## 0.4.0

02-07-2019 15:21 PST


### Implementation Changes
- Pick up stub docstring fix in GAPIC generator. ([#6984](https://github.com/googleapis/google-cloud-python/pull/6984))

### New Features
- Protoc updates to include effects_profile_id. ([#7097](https://github.com/googleapis/google-cloud-python/pull/7097))

### Documentation
- Fix `Client Library Documentation` link ([#7109](https://github.com/googleapis/google-cloud-python/pull/7109))

### Internal / Testing Changes
- Copy proto files alongside protoc versions.
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers and docstring quoting

## 0.3.0

12-18-2018 09:54 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6510](https://github.com/googleapis/google-cloud-python/pull/6510))
- Fix `client_info` bug, update docstrings. ([#6423](https://github.com/googleapis/google-cloud-python/pull/6423))
- Re-generate library using texttospeech/synth.py ([#5981](https://github.com/googleapis/google-cloud-python/pull/5981))
- Add gRPC Transport layer. ([#5959](https://github.com/googleapis/google-cloud-python/pull/5959))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))
- Avoid broken 'google-common-apis 1.5.4' release. ([#6355](https://github.com/googleapis/google-cloud-python/pull/6355))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Docs: Replace links to `/stable/` with `/latest/`. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))
- Fix docs links for TTS. ([#5483](https://github.com/googleapis/google-cloud-python/pull/5483))

### Internal / Testing Changes
- Add synth.metadata. ([#6870](https://github.com/googleapis/google-cloud-python/pull/6870))
- Update noxfile.
- blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add 'mock' to unit test dependencies for autogen libs. ([#6402](https://github.com/googleapis/google-cloud-python/pull/6402))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.2.0

### New Features

- Add the text-to-speech v1 API surface. (#5468)
- Re-generate the text-to-speech v1beta1 API surface. (#5468)

### Documentation

- Rename releases to changelog and include from CHANGELOG.md (#5191)

### Internal / Testing Changes

- Add Test runs for Python 3.7 and remove 3.4 (#5295)

## 0.1.0

### Interface additions

- Added text-to-speech v1beta1. (#5049)
