from flask import Blueprint, render_template
from flask_login import login_required

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def dashboard_page():
    # User is returning, show normal dashboard
    return render_template(
        "dashboard.html"
    )