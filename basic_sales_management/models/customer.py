from odoo import models, fields, api,  _


class ShopCustomer(models.Model):
    _name = 'shop.customer'
    _description = 'Customer Records'
    
    customer_name = fields.Char(string='Name', required=True,  track_visibility="always")
    sales_order = fields.One2many('shop.sales.order', 'customer_id', string='Customer ID')
    email_id = fields.Char(string="Email")
   