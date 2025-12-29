from webob.response import Response
from demo_app import app


@app.route('/static')
def static_view(request) -> Response:
    return Response(body="<h1>This is a static view</h1>")


@app.route('/dashboard')
def dashboard(request) -> Response:
    name = "Dipanjal"
    title = "Dashboard View"
    html_content = app.template("dashboard.html", context={"name": name, "title": title})
    return Response(body=html_content)
