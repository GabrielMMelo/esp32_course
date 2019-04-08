import picoweb
from machine import Pin

def host_server(event=None, callback=None):
    app = picoweb.WebApp(__name__)
    content = []

    @app.route("/confirmacao")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        if req.method == "POST":
            yield from req.read_form_data()
            name = req.form["name"]
            email = req.form["email"]
            yield from app.render_template(resp, "confirmation.tpl", args=(req,))
            nonlocal content
            content = [name, email]
            event.clear() # limpa o evento _server
        else:
            yield from app.render_template(resp, "404.tpl")

    @app.route("/info")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        if req.method == "POST":
            yield from app.render_template(resp, "info.tpl", (req,))
            callback.set([content]) # seta o evento _rfid
        else:
            yield from app.render_template(resp, "404.tpl")

    @app.route("/liga")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        if req.method == "POST":
            Pin(18, Pin.OUT).off()
            Pin(19, Pin.OUT).off()
        yield from app.render_template(resp, "index.tpl", (req,))

    @app.route("/desliga")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        if req.method == "POST":
            Pin(18, Pin.OUT).on()
            Pin(19, Pin.OUT).on()
        yield from app.render_template(resp, "index.tpl", (req,))

    @app.route("/")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        yield from app.render_template(resp, "index.tpl", (req,))

    import logging as logging
    logging.basicConfig(level=logging.INFO)

    app.run(debug=True, host='0.0.0.0', event=event)
