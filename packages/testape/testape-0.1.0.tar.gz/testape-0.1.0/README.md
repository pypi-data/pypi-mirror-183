# Testape SDK

[![PyPI - Version](https://img.shields.io/pypi/v/testape.svg)](https://pypi.org/project/testape)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/testape.svg)](https://pypi.org/project/testape)

---

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install testape
```

Then, in your code:

```python
from testape import TestapeClient

client = TestapeClient(api_key="<your_api_key>")

def func():
    client.send_event()
```

## License

`testape` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
