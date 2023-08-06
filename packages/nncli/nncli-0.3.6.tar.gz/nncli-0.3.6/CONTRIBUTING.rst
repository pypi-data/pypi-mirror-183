Contribution Guide
==================

Thanks for your interest in contributing to nncli(1). This guide
attempts to document everything you need to know to participate in the
development community. As with everything else in this repository,
suggestions are welcome.

Community Guidelines
--------------------

Given that the nncli(1) community is still in the early stages of
formation, community guidelines have yet to be rigidly codified. For
the time being, the following general expectations should be
considered normative:

- Participants should do their part to make this a welcoming
  community, free from harassment and discrimination, where everyone
  feels safe to contribute. Any behavior that threatens this will not
  be tolerated, and repeated violations will result in expulsion from
  the community. Anyone who egregiously violates this principle, for
  instance by doxxing another community member, whether in official
  community channels or elsewhere, will be immediately and permanently
  banned.

- The goal in providing official community channels (e.g., the mailing
  list), is to provide a public space for the development of nncli(1)
  with high signal-to-noise ratio. Persuant to this, community members
  should understand that disagreements naturally arise from time to
  time. If they don't pertain to nncli(1), then they should be
  discussed outside official community channels. This is not a
  judgment about the importance of any given topic, merely a
  recognition that this community cannot sustain discussion about
  anything and everything.

- Maintainers shall be selected from the community as-needed based on
  their ability to productively contribute to nncli(1). Productivity
  in this context is measured *both* in terms of code contributions
  *and* ability to forge consensus in community discussions.

- Decisions regarding the development of nncli(1) fall to the
  maintainers collectively. When the maintainers are not able to form
  a consensus on the best path forward, the lead maintainer shall be
  the final authority on decisions.

Getting Started
---------------

To get started with the code, you will need to clone it and install
development dependencies. We recommend the isolating your development
environment with ``venv`` Python module. We also recommend using
``pip-tools`` to manage dependencies. Its use is expected when
updating requirements files.

::

   $ git clone https://git.danielmoch.com/nncli.git
   $ cd nncli
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   (.venv)$ pip install pip-tools
   (.venv)$ pip-sync requirements-dev.txt

Discussion and Requests
-----------------------

All discussion takes place on the public `mailing list`_. The list's
archive can be found at https://lists.danielmoch.com/nncli-dev. Emails
can be sent to the following addresses to manage your subscription to
the mailing list.

- nncli-dev+subscribe@
- nncli-dev+unsubscribe@
- nncli-dev+help@

Patches and pull requests are welcome, preferably via emailed output
of `git-request-pull(1)`_ sent to the mailing list. Bug reports should
also be directed to the mailing list.

If you aren't hosting a fork anywhere online, you can also send patches
using `git-format-patch(1)`_.

Releases
--------

Releases are published to PyPI_. Signed source tarballs are maintained
at https://dl.danielmoch.com/nncli. Instructions for verifying
tarballs are in the README file at the previous link.

.. _PyPI: https://pypi.org/project/nncli/
.. _mailing list: nncli-dev@danielmoch.com
.. _git-format-patch(1): https://www.git-scm.com/docs/git-format-patch
.. _git-request-pull(1): https://www.git-scm.com/docs/git-request-pull
