:program:`nncli export` exports notes in raw, JSON format. The JSON
format is a superset of the format outlined in the NextCloud Notes API
specification with information added for managing the local notes
cache. If *search_string* is specified, it is used to filter the notes
prior to export.

.. note::

  :program:`nncli` already stores all notes locally in the cache
  directory, so for easy backups, it may be easier/quicker to simply
  backup this entire directory.
