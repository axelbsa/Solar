from solar import create_app

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--port", dest="port", type="int", default=3000)
parser.add_option("--host", dest="host", type="string",
                  default="0.0.0.0")
(options, args) = parser.parse_args()

import httplib
httplib.HTTPConnection.debuglevel = 1

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

app = create_app()
# app.debug = True
app.run(host=options.host, port=options.port)
