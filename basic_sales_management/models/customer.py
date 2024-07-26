from odoo import models, fields, api,  _


class ShopCustomer(models.Model):
    _name = 'shop.customer'
    _description = 'Customer Records'

    sales_order = fields.One2many('shop.sales.order', 'customer_id', string='Customer ID')
    customer_email = fields.Char(string="Email")
   
