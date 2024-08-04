from odoo import api, models, fields

class ShopProduct(models.Model):
    _name = 'shop.product'
    _description = 'Product Record'
    
    product_name = fields.Char(string='Name', required=True, track_visibility="always")
    product_price = fields.Float(string="Price", required=True, track_visibility="always")
    sales_order_line = fields.One2many('shop.sales.order.line', 'product_id', string='Sales Order')
