Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_, and this project adheres to
`Semantic Versioning`_.

`Unreleased`_
-------------
Changed

Added

Fixed

Removed

`v0.3.6`_ - 2022-12-30
----------------------
Changed
 - docs: Major refactor to provide manual pages
 - docs: Change to material theme
 - README: Add reference to mailing list
 - Update pyproject.toml
 - Convert Makefiles to POSIX style
 - consolidate tool configs in pyproject.toml
 - update requirements-dev.txt
 - cli: Modify edit to accept from_stdin flag

Added
 - Add community guidelines
 - Add stdin flag to edit subcommand
 - Add TODO

Fixed
 - cli: Fix (un)favorite
 - nncli: Always check do_server_sync before syncing

Removed
 - docs: Remove CI badge
 - docs: Don't build PDF
 - Remove Pipenv in favor of the simpler pip-tools

`v0.3.5`_ - 2021-12-10
----------------------
Changed
 - Update copyright info in docs
 - Make filtered_notes_sort public
 - Use $VISUAL instead of $EDITOR
 - clipboard: Silence calls to 'which'
 - Smarten up the way we set defaults for cfg_editor
 - Add mailmap
 - Allow syncing in Python 3.8 and later
 - Constrain pytest version

Added
 - clipboard: Add support for xclip
 - Add initial hack at a manual
 - Tox: Add py38 testing

Fixed
 - Fixed 'nncli create' to work without any arguments (credit: lifesbest23)
 - clipboard: Fix line continuations


`v0.3.4`_ - 2019-03-08
----------------------
Changed
 - Fix crashing bug in view_log.py
 - Refactor gui.py based on pylint findings

Removed
 - Pipfile.lock

`v0.3.3`_ - 2019-02-25
----------------------
Added
 - Documentation

   - TODO and CHANGELOG formatting
   - docutils.conf
   - sitemap
   - Canonical URL
   - robots.txt

Changed
 - Changed SafeConfigParser to ConfigParser
 - Reversed test logic in _log_timeout to avoid popping off on an empty
   stack. This bug was leading to fatal crashes.

`v0.3.2`_ – 2018-12-01
----------------------
Added
 - CHANGELOG.rst
 - TODO.txt
 - clear_ids.py contrib script

Changed
 - References to Github repo changed to point to git.danielmoch.com
 - Fixed exception in nncli sync

`v0.3.1`_ – 2018-10-30
----------------------
Added
 - Partial unit testing for nncli.py module

Changed
 - Refactored code (addressing pylint findings)
 - Fixed bad exception handling in Python 3.4

`v0.3.0`_ – 2018-09-07
----------------------
Added
 - Documentation as PDF format

Changed
 - Numerous documentation corrections

`v0.2.0`_ – 2018-09-03
----------------------
Added
 - .travis.yml
 - Pytest, tox, et all added to support automated testing
 - Both tox and Travis testing back to Python 3.4

`v0.1.2`_ – 2018-08-30
----------------------
Added
 - Support for --version flag

Changed
 - requirements.txt replaced with Pipfile{,.lock}

`v0.1.1`_ – 2018-08-07
----------------------
Added
 - README content included in PyPI

Changed
 - README content and formatting
 - Fix nncli import command

v0.1.0 – 2018-07-31
-------------------
Changed
 - Hard fork of sncli

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html
.. _Unreleased: https://git.danielmoch.com/nncli/diff/?id=master&id2=v0.3.6
.. _v0.3.6: https://git.danielmoch.com/nncli/diff/?id=v0.3.6&id2=v0.3.5
.. _v0.3.5: https://git.danielmoch.com/nncli/diff/?id=v0.3.5&id2=v0.3.4
.. _v0.3.4: https://git.danielmoch.com/nncli/diff/?id=v0.3.4&id2=v0.3.3
.. _v0.3.3: https://git.danielmoch.com/nncli/diff/?id=v0.3.3&id2=v0.3.2
.. _v0.3.2: https://git.danielmoch.com/nncli/diff/?id=v0.3.2&id2=v0.3.1
.. _v0.3.1: https://git.danielmoch.com/nncli/diff/?id=v0.3.1&id2=v0.3.0
.. _v0.3.0: https://git.danielmoch.com/nncli/diff/?id=v0.3.0&id2=v0.2.0
.. _v0.2.0: https://git.danielmoch.com/nncli/diff/?id=v0.2.0&id2=v0.1.2
.. _v0.1.2: https://git.danielmoch.com/nncli/diff/?id=v0.1.2&id2=v0.1.1
.. _v0.1.1: https://git.danielmoch.com/nncli/diff/?id=v0.1.1&id2=v0.1.0
