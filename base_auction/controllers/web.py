# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request

from odoo.addons.portal.controllers import web
from odoo.addons.web.controllers.main import ensure_db


class Home(web.Home):
    @http.route()
    def index(self, *args, **kw):
        if request.session.uid and request.env["res.users"].sudo().browse(
            request.session.uid
        ).has_group("base_auction.group_auction_user"):
            return request.redirect_query("/web", query=request.params)
        return super(Home, self).index(*args, **kw)

    def _login_redirect(self, uid, redirect=None):
        if not redirect and request.env["res.users"].sudo().browse(uid).has_group(
            "base_auction.group_auction_user"
        ):
            redirect = "/web"
        return super(Home, self)._login_redirect(uid, redirect=redirect)

    @http.route("/web", type="http", auth="none")
    def web_client(self, s_action=None, **kw):
        if request.session.uid and request.env["res.users"].sudo().browse(
            request.session.uid
        ).has_group("base_auction.group_auction_user"):
            ensure_db()
            if kw.get("redirect"):
                return request.redirect(kw.get("redirect"), 303)
            request.uid = request.session.uid
            try:
                context = request.env["ir.http"].webclient_rendering_context()
                response = request.render("web.webclient_bootstrap", qcontext=context)
                response.headers["X-Frame-Options"] = "DENY"
                return response
            except AccessError:
                return request.redirect("/web/login?error=access")
        return super(Home, self).web_client(s_action, **kw)
