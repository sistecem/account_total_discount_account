# -*- coding: utf-8 -*-

from odoo import fields,models

class DiscountCompany(models.Model):
    _inherit = 'res.company'

    testeo = fields.Char(string='Nombre Completo de propuesta')
    discount_account_id = fields.Many2one('account.account',string='Cuenta para Descuentos')
    discount_tax_id = fields.Many2one('account.tax',string='Impuesto para Descuentos')