Hostsharing Utilities
=====================

A python package with some useful functions for working in a webspace or managed server of [Hostsharing eG](https://hostsharing.net).

Why
---

We have multiple uses for such functions, and it is useful to have them in one place.

Getting started
---------------

Installing:

    pip install hsutilities

A simple example:

```python
from hsutilities import domains as hsdomains
from hsutilities import users as hsusers

pac = hsusers.get_current_pac()
domains = hsdomains.get_domains_of_user(pac)
```
