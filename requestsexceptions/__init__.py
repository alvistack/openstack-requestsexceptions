# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import warnings

try:
    from requests.packages.urllib3.exceptions import InsecurePlatformWarning
except ImportError:
    try:
        from urllib3.exceptions import InsecurePlatformWarning
    except ImportError:
        InsecurePlatformWarning = None

try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except ImportError:
    try:
        from urllib3.exceptions import InsecureRequestWarning
    except ImportError:
        InsecureRequestWarning = None

try:
        from requests.packages.urllib3.exceptions import SubjectAltNameWarning
except ImportError:
    try:
        from urllib3.exceptions import SubjectAltNameWarning
    except ImportError:
        SubjectAltNameWarning = None


def squelch_warnings(insecure_requests=True):
    if SubjectAltNameWarning:
        warnings.filterwarnings('ignore', category=SubjectAltNameWarning)
    if InsecurePlatformWarning:
        warnings.filterwarnings('ignore', category=InsecurePlatformWarning)
    if insecure_requests and InsecureRequestWarning):
        warnings.filterwarnings('ignore', category=InsecureRequestWarning)
