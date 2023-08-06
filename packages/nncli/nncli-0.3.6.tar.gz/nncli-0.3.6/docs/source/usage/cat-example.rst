::

   # Retrieve note category (e.g. "category1")
   $ nncli -k 42 cat get
   category1

   # Add a category to a note, overwriting any existing one
   nncli -k 42 cat set "category3"

   # Remove a category from a note
   nncli -k 42 cat rm
