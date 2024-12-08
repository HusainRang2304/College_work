#
# The content of this file will be filled in with meaningful data when creating an archive using `git archive` or by
# downloading an archive from github, e.g., from github.com/.../archive/develop.zip
#
rev = "7f9e43a7b1"  # abbreviated commit hash
commit = "7f9e43a7b176e13e237cabbd25537e43c99b6128"  # commit hash
date = "2021-10-11 08:16:08 +0200"  # commit date
author = "Rok Mandeljc <rok.mandeljc@gmail.com>"
ref_names = "HEAD -> develop"  # incl. current branch
commit_message = """tests: conftest: increase executable timeout to 3 minutes

Increase the timeout for individual executable from 1 minute to
3 minutes. Also tweak the "TIMED OUT!" message to make it more
obvious that it is coming from our fixture and not from
pytest-timeout.
"""
