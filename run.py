#!/usr/bin/env python3
from src.app import app

app.run(debug=app.config['DEBUG'], port=4990)
