import random
import string
import os

from flask import Flask, redirect, url_for, abort, render_template
from flask_dance.contrib.google import make_google_blueprint, google
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from dotenv import load_dotenv

load_dotenv()

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import last_event_id

sentry_dsn = os.environ["SENTRY_DSN"]

sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]
app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ["GOOGLE_CLIENT_ID"]
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ["GOOGLE_CLIENT_SECRET"]
google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")

TOKENS = {}


@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    try:
        resp = google.get("/oauth2/v1/userinfo")
        email = resp.json()["email"]
        if not email.endswith("@mun.ca"):
            return render_template("not_mun.html")
        else:
            prefix = email.split("@")[0]
            if prefix not in TOKENS:
                TOKENS[prefix] = "".join([random.choice(string.ascii_letters) for _ in range(20)])
            return render_template("verified.html", token=TOKENS[prefix])
    except TokenExpiredError:
        return redirect(url_for("google.login"))


@app.route("/identity/<token>")
def identity(token):
    for ident, t in TOKENS.items():
        if t == token:
            return ident
    abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", sentry_event_id=last_event_id(), sentry_dsn=sentry_dsn), 500
