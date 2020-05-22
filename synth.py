# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""
import re

import synthtool as s
from synthtool import gcp
from synthtool.languages import python

gapic = gcp.GAPICMicrogenerator()
common = gcp.CommonTemplates()
versions = ["v1beta1", "v1"]

# ----------------------------------------------------------------------------
# Generate texttospeech GAPIC layer
# ----------------------------------------------------------------------------
for version in versions:
    library = gapic.py_library(service="texttospeech", version=version,)
    s.move(library, excludes=["setup.py", "docs/index.rst"])

# Fix bad docstrings.
s.replace("**/gapic/*_client.py", r'\\"(.+?)-\*\\"', r'"\1-\\*"')

# Sphinx interprets `*` as emphasis
s.replace(
    ["google/cloud/**/client.py", "google/cloud/**/cloud_tts.py"],
    "((en)|(no)|(nb)(cmn)|(yue))-\*",
    "\g<1>-\*",
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(unit_cov_level=85, cov_level=85, samples=True)
s.move(templated_files)

# Modifications for microgenerator code
s.replace("noxfile.py",
"""if os\.path\.exists\("samples"\):
    BLACK_PATHS\.append\("samples"\)""",
"")

s.replace("noxfile.py",
"""python=\["2\.7", """,
"""python=[""")

s.replace("noxfile.py",
"""python=\["3\.5", """,
"""python=[""")

# Expand flake errors permitted to accomodate the Microgenerator
# TODO: remove extra error codes once issues below are resolved
# F401: https://github.com/googleapis/gapic-generator-python/issues/324
# F841: local variable 'client'/'response' is assigned to but never use
s.replace(".flake8", "ignore = .*", "ignore = E203, E266, E501, W503, F401, F841")

# ----------------------------------------------------------------------------
# Samples templates
# ----------------------------------------------------------------------------
python.py_samples(skip_readmes=True)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
