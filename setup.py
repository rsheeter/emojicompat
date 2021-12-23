# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

extras_require={
    "test": [
        "pytest",
    ],
    "lint": [
        "black",
        "pytype",
    ],
}
extras_require["dev"] = extras_require["test"] + extras_require["lint"]


def _echo(m, l):
  print("HELLO", m, l)
  return l

setup(
    name="emojicompat",
    use_scm_version={"write_to": "src/emojicompat/_version.py"},
    package_dir={
      "": "src",
    },
    packages=find_packages(where="src"),
    entry_points={"console_scripts": ["emojicompat=emojicompat.emojicompat:main"]},
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    install_requires=[
        "absl-py>=0.9.0",
        "fonttools>=4.28.0",
        "flatbuffers>=2.0",
    ],
    extras_require=extras_require,
    # this is so we can use the built-in dataclasses module
    python_requires=">=3.7",

    # this is for type checker to use our inline type hints:
    # https://www.python.org/dev/peps/pep-0561/#id18
    package_data={"emojicompat": ["py.typed"]},

    # metadata to display on PyPI
    author="Rod S",
    author_email="rsheeter@google.com",
    description=("Utility to insert emojicompat metadata into an emoji font"),
)