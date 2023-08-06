#
#  Copyright (c) 2023.  Joël Larose
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#

import mypy_xml_score as mxs
from pathlib import Path

class TestMXS:
    def test_default_stylesheet_is_file(self):
        default_ss = mxs._default_xslt()
        assert Path(default_ss).is_file()
