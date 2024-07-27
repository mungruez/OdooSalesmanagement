from odoo import models, fields, api,  _

class ShopProduct(models.Model):
    _name = 'shop.product'
    _description = 'Product Record'
    
    product_name = fields.Char(string='Name', required=True,  track_visibility="always")
    product_price = fields.Float(string="Price")
    sales_order_line = fields.One2many('shop.sales.order.line', 'product_id', string='Sales Order')
