Import a JSON-formatted note. nncli can import notes from raw json
data (via stdin or editor). Allowed fields are *content*, *category*,
*favorite*, and *modified*. If *-* is specified, the note content is
read from *stdin*. The note syncs to the server after the command
completes.
