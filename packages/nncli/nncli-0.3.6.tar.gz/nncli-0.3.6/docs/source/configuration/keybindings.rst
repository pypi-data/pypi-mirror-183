Keybindings specify the behavior of the console GUI, and are never
required in the ``config`` file. However, they all have default values,
as outlined below. More information on specifying keybindings can be
found in the :ref:`Urwid documentation <urwid:keyboard-input>`.

.. describe:: kb_help

   Press to enter the help screen.

   Default value: ``h``

.. describe:: kb_quit

   Press to exit the console GUI.

   Default value: ``q``

.. describe:: kb_sync

   Press to force a full, bi-directional sync with the server.

   Default value: ``S``

.. describe:: kb_down

   Press to move down one row.

   Default value: ``j``

.. describe:: kb_up

   Press to move one row up.

   Default value: ``k``

.. describe:: kb_page_down

   Press to move one page down.

   Default value: ``space``

.. describe:: kb_page_up

   Press to move one page up.

   Default value: ``b``

.. describe:: kb_half_page_down

   Press to move one half-page down.

   Default value: ``ctrl d``

.. describe:: kb_half_page_up

   Press to move one half-page up.

   Default value: ``ctrl u``

.. describe:: kb_bottom

   Press to move to the last line.

   Default value: ``G``

.. describe:: kb_top

   Press to move to the first line.

   Default value: ``g``

.. describe:: kb_status

   Press to toggle the visibility of the status bar.

   Default value: ``s``

.. describe:: kb_create_note

   Press to create a new note and open in the configured editor (see
   :confval:`cfg_editor`).

   Default value: ``C``

.. describe:: kb_edit_note

   Press to edit the highlighted note in the configured editor (see
   :confval:`cfg_editor`).

   Default value: ``e``

.. describe:: kb_view_note

   Press to view the highlighted note in read-only mode.

   Default value: ``enter``

.. describe:: kb_view_note_ext

   Press to view the highlighted note in the configured pager (see
   :confval:`cfg_pager`).

   Default value: ``meta enter``

.. describe:: kb_view_note_json

   Press to view the raw JSON contents of the highlighted note in
   read-only mode.

   Default value: ``O``

.. describe:: kb_pipe_note

   Press to send the contents of the highlighted note to ``stdin`` of
   another program. A small command window opens at the bottom of the
   screen to enter the desired program.

   Default value: ``|``

.. describe:: kb_view_next_note

   Press to view the contents of the next note in read-only mode.

   Default value: ``J``

.. describe:: kb_view_prev_note

   Press to view the contents of the previous note in read-only mode.

   Default value: ``K``

.. describe:: kb_view_log

   Press to view the log.

   Default value: ``l``

.. describe:: kb_tabstop2

   Press to set the tabstop for the internal pager to a width of two
   characters.

   Default value: ``2``

.. describe:: kb_tabstop4

   Press to set the tabstop for the internal pager to a width of four
   characters.

   Default value: ``4``

.. describe:: kb_tabstop8

   Press to set the tabstop for the internal pager to a width of eight
   characters.

   Default value: ``8``

.. describe:: kb_search_gstyle

   Press to initiate a search of your notes against a Google-style
   search term. A command window will open at the bottom of the screen
   to enter your search term.

   Default value: ``/``

.. describe:: kb_search_regex

   Press to initiate a search of your notes against a regular
   expression. A command window will open at the bottom of the screen to
   enter your search term.

   Default value: ``meta /``

.. describe:: kb_search_prev_gstyle

   Press to initiate a reverse search of your notes against a
   Google-style search term. A command window will open at the bottom of
   the screen to enter your search term.

   Default value: ``?``

.. describe:: kb_search_prev_regex

   Press to initiate a reverse search of your notes against a regular
   expression.  A command window will open at the bottom of the screen
   to enter your search term.

   Default value: ``meta ?``

.. describe:: kb_search_next

   Press after a search has been initiated to move to the next match.

   Default value: ``n``

.. describe:: kb_search_prev

   Press after a search has been initiated to move to the previous
   match.

   Default value: ``N``

.. describe:: kb_clear_search

   Press to clear the current search.

   Default value: ``A``

.. describe:: kb_sort_date

   Press to display notes sorted by date.

   Default value: ``d``

.. describe:: kb_sort_alpha

   Press to display notes sorted alphabetically.

   Default value: ``a``

.. describe:: kb_sort_categories

   Press to display notes sorted by category.

   Default value: ``ctrl t``

.. describe:: kb_note_delete

   Press to delete a note. The note will be deleted locally and
   reflected on the server after the next full sync (see
   :confval:`kb_sync`).

   Default value: ``D``

.. describe:: kb_note_favorite

   Press to toggle the ``favorite`` flag for a note.

   Default value: ``p``

.. describe:: kb_note_category

   Press to set/edit the note category. A command window will appear at
   the bottom of the screen containing the current category (if it has
   one). Set to an empty string to clear the category.

   Default value: ``t``

.. describe:: kb_copy_note_text

   Press to copy the note text to the system clipboard.

   Default value: ``y``
