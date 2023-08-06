nncli.config(5)
===============

.. include:: configuration/intro.rst
.. |here| replace:: in the Urwid manual

Configuration File
------------------

nncli pulls in configuration from the *config* file located in the
standard location for your platform:

.. describe:: macOS

  $HOME/Library/Preferences/nncli

.. describe:: Linux/BSD

  $XDG_CONFIG_HOME/nncli/config or $HOME/.config/nncli/config

The following directives are accepted within the *config* file:

General Options
~~~~~~~~~~~~~~~

.. include:: configuration/genopts.rst

Keybindings
~~~~~~~~~~~

.. include:: configuration/keybindings.rst

Colors
~~~~~~

.. include:: configuration/colors.rst

Examples
--------

At the very least, the following example *config* will get you going
(using your account information):

::

   [nncli]
   cfg_nn_username = lebowski@thedude.com
   cfg_nn_password = nihilist
   cfg_nn_host     = nextcloud.thedude.com

See Also
--------

:manpage:`nncli(1)`

The Urwid Manual, Display Attributes, 16 Standard Foreground Colors
