Hostsharing Utilities
=====================

A python package with some useful functions for working in a webspace or managed server of [Hostsharing eG](https://hostsharing.net).

Why
---

We have multiple uses for such functions, and it is useful to have them in one place.

Getting started
---------------

Installing:

    pip install hostsharing_utilities

A simple example:

```python
import hostsharing_utiltiies as hs

pac = hs.users.get_current_pac()
domains = hs.domains.get_domains_of_user(pac)
```
