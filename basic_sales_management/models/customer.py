from odoo import api,models, fields

class ShopCustomer(models.Model):
    _name = 'shop.customer'
    _description = 'Customer Records'
    
    customer_email = fields.Char(string="Customer Email", required=True)
    sales_order = fields.One2many('shop.sales.order', 'customer_id', string='Customer ID')
   
