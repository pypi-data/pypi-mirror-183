nncli(1)
========

Synopsis
--------

**nncli** [*options*] *subcommand* [*subcommand-options*] [*args*]...

Description
-----------

:program:`nncli` gives you access to your NextCloud notes account via
the command line. You can access your notes via a customizable console
GUI that implements vi-like keybinds or via a simple, scriptable command
line interface.

Notes can be viewed/created/edited in *both an* **online** *and*
**offline** *mode*. All changes are saved to a local cache on disk and
automatically sync'ed when nncli is brought online.

Options
-------

.. include:: usage/genopts.rst
.. include:: usage/subopts.rst

Subcommands
-----------

:program:`nncli` provides the following subcommands:

- :manpage:`nncli-sync(1)`
- :manpage:`nncli-list(1)`
- :manpage:`nncli-export(1)`
- :manpage:`nncli-dump(1)`
- :manpage:`nncli-create(1)`
- :manpage:`nncli-import(1)`
- :manpage:`nncli-edit(1)`
- :manpage:`nncli-delete(1)`
- :manpage:`nncli-favorite(1)`
- :manpage:`nncli-cat(1)`


Environment Variables
---------------------

.. describe:: VISUAL

  Used to determine which program to open when editing a note.

.. describe:: EDITOR

  Used when VISUAL is not defined to determine which program to open
  when editing a note. If neither is defined, :manpage:`vim(1)` is
  used.

.. describe:: PAGER

  Used to specify the program used to open notes for reading. If not
  defined, the default is **less -c**.

.. describe:: XDG_CACHE_HOME

  Used to determine the location of the local notes database. If not
  specified, *$HOME/.cache* will be used.

.. describe:: XDG_CONFIG_HOME

  Used to determine the location of the configuration file. If not
  specified, *$HOME/.config* will be used.


See also
--------

:manpage:`less(1)`,
:manpage:`nncli.config(5)`
