
import requests
import argparse

"""
This class is using the requests api to ping the server.

default usage : [python -m] client.py --get --file=index.html --port=8088

Note, it can be python -m or python3 based on the OS and the python version

"""
class SimpleHttpClient:
  def __init__(self, host):
    self.host = host
    self.server_address = 'http://{}'.format(self.host)

  """
  Based on the input args, we get the file to fetch
  given the host
  """
  def get(self, file_name):
    file_path = self.server_address + "/" + file_name
    response = requests.get(file_path)
    print (response.text)
    return response.text

    """
  Based on the input args, we read the file and call the server to 
  put the file
  """
  def put(self, file_name):
    data = "Hello this is in text"
    response = requests.put(self.server_address +"/"+file_name, data)
    print (response.content)
    return response.text

if __name__ == '__main__':

  parser = argparse.ArgumentParser()

  parser.add_argument("--get", action='store_true', default=False)
  parser.add_argument("--file", type=str,
                      help='A required field filename')
  parser.add_argument("--put", action='store_true', default=False)
  parser.add_argument('--host', action='store',
                      default="127.0.0.1", type=str,
                      nargs='?',
                      help='Specify alternate port [default:127.0.0.1]')
  parser.add_argument('--port', action='store',
                      default="8080", type=str,
                      nargs='?',
                      help='Specify alternate port [default: 8080]')
  args = parser.parse_args()

  hostname = args.host +":"+ args.port
  client = SimpleHttpClient(hostname)
  if args.put:
    client.put(args.file)
  else:
    client.get(args.file)


