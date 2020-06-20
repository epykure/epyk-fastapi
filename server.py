
import os
import uvicorn

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import templates

app = FastAPI(debug=True)

origins = [
    "*",
    "http://127.0.0.1",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', response_class=HTMLResponse)
def home():
  """
  Description:
  ------------
  Report creation on the fly in Flask
  """
  from epyk.core.Page import Report

  rptObj = Report()
  list = rptObj.ui.list()
  for pyfile in os.listdir("reports"):
    if pyfile.endswith(".py"):
      list.add_item(rptObj.ui.link(pyfile, url="/views/%s" % pyfile[:-3]).css({"padding": '2px 0', 'display': 'block'}))
  return rptObj.outs.html()


@app.get("/views/{file_name}", response_class=HTMLResponse)
def read_item(file_name, refresh: bool = False):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param file_name:
  """
  html_page = os.path.join('views', '%s.html' % file_name)
  if not os.path.exists(html_page):
    refresh = True
  if refresh:
    templates.refresh(file_name)

  html_content = open(html_page).read()
  return html_content


@app.post("/file")
async def file(request: Request):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param request:
  """
  import json

  data = await request.form()
  content = []
  for pyFile in data.values():
    print(pyFile.filename)
    content = json.loads(await pyFile.read())
    print(content)
    print(list(content[0].keys()))
    return {"cols": content}


@app.post("/data_table")
async def data_table(request: Request):
  """
  Description:
  ------------

  :param request:
  """
  return {'row': {"name": 'test'}, 'columns': [], 'visible': [], 'content': []}


@app.post("/data_chartjs")
async def data_chartjs(request: Request):
  """
  Description:
  ------------

  :param request:
  """
  from epyk.core import data as chart_data

  values = [
    {1: 45, 2: 41, 3: 4, 5: 48, 'x': 1, 'g': "A"},
    {1: 45, 2: 41, 3: 4, 5: 48, 'x': 1, 'g': "B"},
  ]
  result = chart_data.chartJs.xyz(values, [1, 2], 'x')
  result_bar = chart_data.chartJs.y(values, [3, 4, 5], 'g')
  result_pie = chart_data.chartJs.y(values, [1, 4, 5], 'g')
  return {'scatter': result, 'pie': result_pie, 'bar': result_bar}


@app.post("/data")
async def data(request: Request):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param request:
  """

  from epyk.core import data as chart_data

  data = await request.json()
  result = chart_data.chartJs.xyz([
    {"x": 1, 1: 1, 2: 2},
    {"x": 2, 1: 1, 2: 2},
  ], [1, 2], 'x')
  pie_data = chart_data.chartJs.y([
    {"x": 1, 1: 1, 2: 2},
    {"x": 2, 1: 2, 2: 2},
  ], [1], 'x')

  return {"chart": result, 'pie': pie_data}


if __name__ == '__main__':
  uvicorn.run("server:app", host='127.0.0.1', port=8080, reload=True)
