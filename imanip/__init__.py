import os, json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)

app.config.from_object('imanip.settings')

app.url_map.strict_slashes = False

import imanip.core
import imanip.helpers
import imanip.controllers