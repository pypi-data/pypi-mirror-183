.. _configuration:
.. |here| replace:: :ref:`here<urwid:16-standard-foreground>`

Configuration
=============

.. include configuration/intro.rst

.. index:: single: configuration file

.. _config-file:

Configuration File
------------------

nncli pulls in configuration from the *config* file located in the
standard location for your platform:

- Windows: ``%USERPROFILE%\AppData\Local\djmoch\nncli``

- macOS: ``$HOME/Library/Preferences/nncli``

- \*nix: ``$XDG_CONFIG_HOME/nncli/config`` or
  ``$HOME/.config/nncli/config``

The following directives are accepted within the *config* file:

.. index:: pair: configuration file; general options

General Options
~~~~~~~~~~~~~~~

.. include:: configuration/genopts.rst

.. index:: pair: configuration file; keybindings

Keybindings
~~~~~~~~~~~


.. index:: pair: configuration file; colors

Colors
~~~~~~

nncli utilizes the Python Urwid_ module to implement the console user
interface.

.. include:: configuration/colors.rst

.. _Urwid: http://urwid.org

Examples
--------

At the very least, the following example ``config`` will get you going
(using your account information):

.. code-block:: ini

   [nncli]
   cfg_nn_username = lebowski@thedude.com
   cfg_nn_password = nihilist
   cfg_nn_host     = nextcloud.thedude.com

Start nncli with no arguments which starts the console GUI mode. nncli
will begin to sync your existing notes and you'll see log messages at
the bottom of the console. You can view these log messages at any time
by pressing the ``l`` key.

View the help by pressing ``h``. Here you'll see all the keybinds and
configuration items. The middle column shows the config name that can be
used in your ``config`` to override the default setting.

See example configuration file below for more notes.

::

   [nncli]
   cfg_nn_username = lebowski@thedude.com
   cfg_nn_password = nihilist
   cfg_nn_host     = nextcloud.thedude.com

   ; as an alternate to cfg_nn_password you could use the following config item
   ; any shell command can be used; its stdout is used for the password
   ; trailing newlines are stripped for ease of use
   ; note: if both password config are given, cfg_nn_password will be used
   cfg_nn_password_eval = gpg --quiet --for-your-eyes-only --no-tty --decrypt ~/.nncli-pass.gpg

   ; see http://urwid.org/manual/userinput.html for examples of more key
   ; combinations
   kb_edit_note = space
   kb_page_down = ctrl f

   ; note that values must not be quoted
   clr_note_focus_bg = light blue

   ; if this editor config value is not provided, the $EDITOR env var will be
   ; used instead
   ; warning: if neither $EDITOR or cfg_editor is set, it will be impossible to
   ; edit notes
   cfg_editor = nvim

   ; alternatively, {fname} and/or {line} are substituted with the filename and
   ; current line number in nncli's pager.
   ; If {fname} isn't supplied, the filename is simply appended.
   ; examples:
   cfg_editor = nvim {fname} +{line}
   cfg_editor = nano +{line}

   ; this is also supported for the pager:
   cfg_pager = less -c +{line} -N {fname}
