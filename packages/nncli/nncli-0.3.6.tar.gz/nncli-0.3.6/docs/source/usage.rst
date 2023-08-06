Usage
=====

.. include:: usage/genopts.rst

Subcommands
-----------

There are a variety of subcommands available from the command line when
using ``nncli``. The intent is for these subcommands to enable
scripting against your NextCloud Notes database. The subcommands are:

- sync

- list

- export

- dump

- create

- import

- edit

- delete

- (un)favorite

- cat {get,set,rm}

These subcommands and the options available to them are described below.

.. _general-options:
.. include:: usage/genopts.rst
.. include:: usage/subopts.rst

nncli sync
~~~~~~~~~~

.. program:: nncli sync

Command format: ``nncli sync``

.. include:: usage/sync-desc.rst

nncli list
~~~~~~~~~~

.. program:: nncli list

Command format: :program:`nncli list` [*options*] [*search_string*]

.. include:: usage/list-desc.rst

Options are as follows:

.. include:: usage/list-args.rst

nncli export
~~~~~~~~~~~~

.. program:: nncli export

Command format: :program:`nncli export` [*options*] [*search_string*]

.. include:: usage/export-desc.rst

Options are as follows:

.. include:: usage/export-args.rst

Example:

.. include:: usage/export-example.rst

nncli dump
~~~~~~~~~~

.. program:: nncli dump

Command format: :program:`nncli dump` [search_string]``

.. include:: usage/dump-desc.rst

Options are as follows:

.. include:: usage/dump-args.rst

nncli create
~~~~~~~~~~~~

.. program:: nncli create

Command format: program:`nncli create` [*-*]

.. include: usage/create-desc.rst

Example:

.. include:: usage/create-example.rst

nncli import
~~~~~~~~~~~~

.. program:: nncli import

Command format: ``nncli import [-]``

.. include:: usage/import-desc.rst

Example:

.. include:: usage/import-example.rst

nncli edit
~~~~~~~~~~

.. program:: nncli edit

Command format: :program:`nncli` [*--key|-k*] *KEY edit*

.. include:: usage/edit-desc.rst

Options are as follows:

.. include:: usage/edit-args.rst

nncli delete
~~~~~~~~~~~~

.. program:: nncli delete

Command format: :program:`nncli` [*--key|-k*] *KEY delete*

.. include:: usage/delete-desc.rst

Options are as follows:

.. include:: usage/delete-args.rst

nncli favorite
~~~~~~~~~~~~~~

.. program:: nncli favorite

Command format: :program:`nncli` *--key|-k KEY favorite|unfavorite*

.. include:: usage/favorite-desc.rst

Options are as follows:

.. include:: usage/favorite-args.rst

nncli cat
~~~~~~~~~

.. program:: nncli cat

Command format: :program:`nncli` *--key|-k KEY cat get|set|rm* [*category_name*]

.. include:: usage/cat-desc.rst

Options are as follows:

.. include:: usage/cat-args.rst

Example:

.. include:: usage/cat-example.rst

Console GUI Usage
-----------------

.. index:: single: searching

Searching
~~~~~~~~~

nncli supports two styles of search strings. First is a Google style
search string and second is a Regular Expression.

A Google style search string is a group of tokens (separated by spaces)
with an implied *AND* between each token. This style search is case
insensitive. For example:

.. code-block:: none

   /category:category1 category:category2 word1 "word2 word3" category:category3

Regular expression searching also supports the use of flags (currently
only case-insensitive) by adding a final forward slash followed by the
flags. The following example will do a case-insensitive search for
``something``:

.. code-block:: none

   (regex) /something/i

.. index:: single: modelines

Modelines
~~~~~~~~~

Advanced text editors usually tailor their behavior based on the file
type being edited. For such editors, notes opened through nncli should
be treated as Markdown by default. However, you can change this
on a per-note basis through the use of modelines. In Vim, for instance,
a modeline is a comment line conforming to the pattern below::

   :: vim: ft=rst

Now when you edit this note Vim will automatically load the rst plugin.
