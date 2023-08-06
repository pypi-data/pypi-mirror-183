import pathlib

def load_radar_exporter_web_page():
  """
  Read colocalized html file and return it
  """
  web_page_content = ""
  current_path = pathlib.Path(__file__).parent.resolve()
  with open(f"{current_path}/radar-exporter-index.html", "r") as web_page_file:
    web_page_content = web_page_file.read()
  
  return web_page_content