Common Subcommand Options
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the global options, several ``nncli`` options apply to
multiple subcommands. They are:

.. option:: --verbose, -v

Print verbose logging information to ``stdout``

.. option:: --nosync, -n

Operate only on the local notes cache. Do not reach out to the server.

.. option:: --regex, -r

For subcommands that accept a search string, treat the search string as
a regular expression.

.. option:: --key, -k

The ID of the note to operate on. This option is required for many of
the subcommands.
