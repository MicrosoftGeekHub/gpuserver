import json

import bottle
from bottle import request, route

from sgfsummary import sgflib

#
# Where Yimeng you could work on
#
"""
input: a initialized sgf_parser with data received
output: please return a 2-tuple
"""
def handle_sgf(sgf_parser):
    print sgf_parser
    return (0, 0)
# END

@route('/try_sgf')
def try_sgf():
    return '''
<form action="/get_sgf" method="post" enctype="multipart/form-data">
    SGF File: <input type="file" name="sgffile" />
    <input type="submit" value="upload" />
</form>
'''

"""
please use form data to send file, field name: sgffile
"""
@route('/get_sgf', method='POST')
def get_sgf():
    uploaded_file = request.files.get('sgffile')
    sgfparser = sgflib.SGFParser(uploaded_file.file.read())

    rtn_data = {
        'data': list(handle_sgf(sgfparser))
    }
    return json.dumps(rtn_data)

if __name__ == "__main__":
    # TODO: initialize your model here
    bottle.run()
