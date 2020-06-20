


from epyk.core.html.templates import HtmlTmplBase

from epyk.core import css
from epyk.core import html
from epyk.core.js import Imports


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

# New core components
HTML_COMPONENTS_PATH = []

#s_modules = [js for js in Imports.JS_IMPORTS]
#print(js_modules)


# All the external packages defined in the framework
PACKAGES = [['accounting', 'underscore', 'promise-polyfill', 'babel-polyfill', 'bootstrap', 'moment', 'ag-grid', 'tabulator',
             'tabulator-inputs', 'tabulator-drop', 'tabulator-mutators-inputs', 'editors-inputs', 'editors-dates',
             'editors-selects', 'tabulator-icons', 'tabulator-editors', 'tabulator-numbers', 'font-awesome', 'datatables',
             'datatables-buttons', 'datatables-select', 'datatables-scroller', 'datatables-searchPanes', 'datatables-responsive',
             'datatables-keytable', 'datatables-autoFill', 'datatables-rows-group', 'datatables-row-group', 'datatables-fixed-columns',
             'datatables-fixed-header', 'datatables-export', 'datatables-col-order', 'jszip', 'json-formatter', 'pivot',
             'require.js', 'pivot-sub-total', 'pivot-c3', 'pivot-plotly', 'pivot-d3', 'jquery', 'qunit', 'jquery-sparklines',
             'jqueryui', 'jquery-brackets', 'timepicker', 'jquery-context-menu', 'jquery-scrollbar', 'pdfmake', 'jspdf',
             'clipboard', 'd3', 'd3-tip', 'd3-ease', 'd3-dispatch', 'd3-transition', 'd3-selection', 'd3-interpolate',
             'd3-time-format', 'd3-time', 'd3-array', 'd3-format', 'd3-collection', 'd3-scale', 'd3-color', 'plotly.js',
             'nvd3', 'c3', 'crossfilter', 'dc', 'billboard', 'Chart.js', 'chartjs-plugin-dragdata', 'chartjs-plugin-annotation',
             'chartjs-plugin-crosshair', 'chartjs-plugin-zoom', 'chartjs-pie-labels', 'chartjs-chart-geo', 'popper',
             'select', 'select-ajax', 'vis', 'mathjs', 'socket.io', 'codemirror', 'leaflet', 'showdown', 'sortable',
             'google-platform']]


class Font(object):
  size, header_size, unit = 20, 14, "px"
  family = "Calibri"


css.Font = Font


EXTENSIONS = {}


Imports.extend_imports(EXTENSIONS)


def build_interface():
  """
  This function will build a new components hierarchy which will be used in project mode.
  """
  import os
  import sys
  import inspect

  core_component_path = os.path.split(html.__file__)[0]
  sys.path.append(core_component_path)
  module_per_package = {}
  for paths in [core_component_path] + HTML_COMPONENTS_PATH :
    for f in os.listdir(paths):
      if f.endswith('.py'):
        html_mod = __import__(f[:-3])
        for name, obj in inspect.getmembers(html_mod, inspect.isclass):
          if hasattr(obj, 'requirements') and obj.requirements is not None:
            for req in obj.requirements:
              module_per_package.setdefault(req, []).append(obj.__name__)
  print(module_per_package)
