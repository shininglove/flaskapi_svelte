from flask import jsonify, render_template, send_from_directory
from app.db.models import Finance, session
from sqlalchemy import select
from app import app


@app.errorhandler(404)
def no_page_exists(_):
    return render_template("404.html"), 404


@app.errorhandler(500)
def no_page_there(_):
    return render_template("500.html"), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path:path>")
def assets(path):
    return send_from_directory("static", path)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data")
def data():
    stmt = select(Finance).order_by(Finance.date.desc())
    # partitions to the amount of columns
    data = session.scalars(stmt).all()
    if data is None:
        return {}
    output = [
        [
            {
                "category": row.category,
                "amount": row.amount,
                "description": row.description,
                "date": row.date,
            }
        ]
        for row in data
    ]
    return jsonify(output)


@app.route("/info")
def info():
    stmt = select(Finance).distinct()
    info = session.scalars(stmt).all()
    if info is None:
        return {}
    sections = list(set([item.category for item in info]))
    categories = {"categories": sections, "length": len(info)}
    return jsonify(categories)


app.secret_key = ""

if __name__ == "__main__":
    app.run(debug=True)
