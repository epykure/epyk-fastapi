


from epyk.core.html.templates import HtmlTmplBase

from epyk.core.css import Defaults as css_defaults
from epyk.core.html import Defaults as html_defaults


HtmlTmplBase.STATIC_PAGE = '''
<!DOCTYPE html>
<html lang="en" style="height:100%%">
<head>
%(header)s
%(jsImports)s
%(cssImports)s
<style>
%(cssStyle)s
</style>
</head>
%(body)s
<script>
%(jsFrgs)s
</script>
</html>
'''


class Font(object):
  size, header_size, unit = 20, 14, "px"
  family = "Calibri"


css_defaults.Font = Font

