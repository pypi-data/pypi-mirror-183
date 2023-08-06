.. note::

   At this time, nncli does not yet support 256-color terminals and is
   limited to just 16-colors. Color names that can be specified in the
   ``config`` file are listed |here|.

The following pairs of configuration values represent the foreground and
background colors for different elements of the console GUI. In each
case the configuration value corresponding to the foreground color ends
in ``_fg``, and the configuration value corresponding to the
background color ends in ``_bg``. The default color values are listed in
foreground/background format.

.. describe:: clr_default_fg

.. describe:: clr_default_bg

   The default foreground/background colors.

   Default values: ``default/default``

.. describe:: clr_status_bar_fg

.. describe:: clr_status_bar_bg

   The foreground/background colors for the status bar.

   Default values: ``dark gray/light gray``

.. describe:: clr_log_fg

.. describe:: clr_log_bg

   The foreground/background colors for the log.

   Default values: ``dark gray/light gray``

.. describe:: clr_user_input_bar_fg

.. describe:: clr_user_input_bar_bg

   The foreground/background colors for the input bar.

   Default values: ``white/light red``

.. describe:: clr_note_focus_fg

.. describe:: clr_note_focus_bg

   The foreground/background colors for the selected note.

   Default values: ``white/light red``

.. describe:: clr_note_title_day_fg

.. describe:: clr_note_title_day_bg

   The foreground/background colors for notes edited within the past 24
   hours.

   Default values: ``light red/default``

.. describe:: clr_note_title_week_fg

.. describe:: clr_note_title_week_bg

   The foreground/background colors for notes edited within the past
   week,

   Default values: ``light green/default``

.. describe:: clr_note_title_month_fg

.. describe:: clr_note_title_month_bg

   The foreground/background colors for notes edited within the past
   month.

   Default values: ``brown/default``

.. describe:: clr_note_title_year_fg

.. describe:: clr_note_title_year_bg

   The foreground/background colors for notes edited within the past
   year.

   Default values: ``light blue/default``

.. describe:: clr_note_title_ancient_fg

.. describe:: clr_note_title_ancient_bg

   The foreground/background colors for notes last edited more than one
   year ago.

   Default values: ``light blue/default``

.. describe:: clr_note_date_fg

.. describe:: clr_note_date_bg

   The foreground/background colors for the note date (i.e. the ``%D``
   portion of :confval:`cfg_format_note_title`).

   Default values: ``dark blue/default``

.. describe:: clr_note_flags_fg

.. describe:: clr_note_flags_bg

   The foreground/background colors for the note flags (i.e., the ``%F``
   portion of :confval:`cfg_format_note_title`).

   Default values: ``dark magenta/default``

.. describe:: clr_note_category_fg

.. describe:: clr_note_category_bg

   The foreground/background colors for the note category (i.e., the
   ``%T`` portion of :confval:`cfg_format_note_title`).

   Default values: ``dark red/default``

.. describe:: clr_note_content_fg

.. describe:: clr_note_content_bg

   The foreground/background colors for the note content as displayed
   in the internal pager.

   Default values: ``default/default``

.. describe:: clr_note_content_focus_fg

.. describe:: clr_note_content_focus_bg

   The foreground/background colors for focused content within the
   internal pager.

   Default values: ``white/light red``

.. describe:: clr_note_content_old_fg

.. describe:: clr_note_content_old_bg

   The foreground/background colors for old note content as displayed
   within the internal pager.

   Default values: ``yellow/dark gray``

.. describe:: clr_note_content_old_focus_fg

.. describe:: clr_note_content_old_focus_bg

   The foreground/background colors for old note focused content as
   displayed within the internal pager.

   Default values: ``white/light red``

.. describe:: clr_help_focus_fg

.. describe:: clr_help_focus_bg

   The foreground/background colors for focused content in the help
   screen.

   Default values: ``white/light red``

.. describe:: clr_help_header_fg

.. describe:: clr_help_header_bg

   The foreground/background colors for header content in the help
   screen.

   Default values: ``dark blue/default``

.. describe:: clr_help_config_fg

.. describe:: clr_help_config_bg

   The foreground/background colors for configuration option name (e.g.,
   ``clr_help_focus_bg``) in the help screen.

   Default values: ``dark green/default``

.. describe:: clr_help_value_fg

.. describe:: clr_help_value_bg

   The foreground/background colors for the value of a configuration
   option as set in ``config``.

   Default values: ``dark red/default``

.. describe:: clr_help_descr_fg

.. describe:: clr_help_descr_bg

   The foreground/background colors for the configuration options
   description in the help screen.

   Default values: ``default/default``
