# -*- coding: utf-8 -*-

from flask import Flask, abort
import services.data as services

app = Flask(__name__)


@app.route('/api/services/<service_id>')
def hello_world(service_id):
    if services.is_not_present(service_id):
        abort(404)
    msg = services.run(service_id)
    return msg
