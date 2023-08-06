.. describe:: cfg_nn_host

   Sets the URL of the NextCloud instance to connect to.

   Required.

.. describe:: cfg_nn_username

   The user name to log in as.

   Required.

.. describe:: cfg_nn_password

   The password to use for log in.

   Optional. Overrides :confval:`cfg_nn_password_eval` if both are
   specified.

   .. note::

      For security reasons, use of the ``cfg_nn_password_eval`` option
      is recommended

.. describe:: cfg_nn_password_eval

   A command to run to retrieve the password. The command should return
   the password on ``stdout``.

   Optional. Required if :confval:`cfg_nn_password` is not specified.

.. describe:: cfg_db_path

   Specifies the path of the local notes cache.

   Optional. Default value:

   - Windows: ``%USERPROFILE%\AppData\Local\djmoch\nncli\Cache``

   - macOS: ``~/Library/Caches/nncli``

   - \*nix: ``$XDG_CACHE_HOME/nncli`` or ``$HOME/.cache/nncli``

.. describe:: cfg_search_categories

   Set to ``yes`` to include categories in searches. Otherwise set to
   ``no``.

   Optional. Default value: ``yes``

.. describe:: cfg_sort_mode

   Sets how notes are sorted in the console GUI. Set to ``date``
   to have them sorted by date (newest on top). Set to ``alpha`` to have
   them sorted alphabetically.

   Optional. Default value: ``date``

.. describe:: cfg_favorite_ontop

   Determines whether notes marked as favorite are sorted on top.

   Optional. Default value: ``yes``

.. describe:: cfg_tabstop

   Sets the width of a tabstop character.

   Optional. Default value: ``4``

.. describe:: cfg_format_strftime

   Sets the format of the note timestamp (``%D``) in the note title. The
   format values are the specified in :py:func:`time.strftime`.

   Optional. Default value: ``%Y/%m/%d``

.. describe:: cfg_format_note_title

   Sets the format of each line in the console GUI note list. Various
   formatting tags are supported for dynamically building the title
   string. Each of these formatting tags supports a width specifier
   (decimal) and a left justification (``-``) like that supported by
   printf:

   .. code-block:: none

      %F - flags (fixed 2 char width)
           X - needs sync
           * - favorited
      %T - category
      %D - date
      %N - title

   The default note title format pushes the note category to the far
   right of the terminal and left justifies the note title after the
   date and flags.

   Optional. Default value: ``[%D] %F %-N %T``

   Note that the ``%D`` date format is further defined by the strftime
   format specified in :confval:`cfg_format_strftime`.

.. describe:: cfg_status_bar

   Sets whether or not the status bar is visible at the top of the
   console GUI.

   Optional. Default value: ``yes``

.. describe:: cfg_editor

   Sets the command to run when opening a note for editing. The special
   values ``{fname}`` and ``{line}`` can be used to specify respectively
   the file name and line number to pass to the command.

   Optional. Default value: ``$VISUAL`` or ``$EDITOR`` if defined in the
   user's environment (preferring ``$VISUAL``), else ``vim {fname} +{line}``.

.. describe:: cfg_pager

   Sets the command to run when opening a note for viewing in an
   external pager.

   Optional. Default value: ``$PAGER`` if defined in the user's
   environment, else ``less -c``.

.. describe:: cfg_max_logs

   Sets the number of log events to display together in the consule GUI
   footer.

   Optional. Default value: ``5``

.. describe:: cfg_log_timeout

   Sets the rate to poll for log events. Unit is seconds.

   Optional. Default value: ``5``

.. describe:: cfg_log_reversed

   Sets whether or not the log is displayed in reverse-chronological
   order.

   Optional. Default value: ``yes``

.. describe:: cfg_tempdir

   Sets a directory path to store temporary files in. ``nncli`` uses
   :func:`tempfile.mkstemp` under the hood, and the most nuanced
   description of how this value is used can be found in the discussion
   of the ``dir`` keyword argument there. Basically you should not
   specify this if you want to use the platform-standard temporary
   folder.

   Optional. Default value: *[blank]*
