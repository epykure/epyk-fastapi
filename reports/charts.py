


def get_page(rptObj):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param rptObj:

  :rtype: epyk.core.Page.Report
  """

  # Defined the charts containers
  scatter = rptObj.ui.charts.chartJs.bubble()
  bar = rptObj.ui.charts.chartJs.bar()
  pie = rptObj.ui.charts.chartJs.polar()

  button = rptObj.ui.button("Update Charts")
  button.click([
    rptObj.js.post("/data_chartjs").onSuccess([
      # Update the charts with data coming from the server
      scatter.build(rptObj.js.objects.data['scatter']),
      pie.build(rptObj.js.objects.data['pie']),
      bar.build(rptObj.js.objects.data['bar'])
    ]),
  ])
