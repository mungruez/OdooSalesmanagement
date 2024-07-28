from odoo import models, fields

class ShopSalesOrderLine(models.Model):
    _name = 'shop.sales.order.line'
    _description = 'Sales Order Line'

    product_quantity = fields.Integer(string="Quantity")
    product_id = fields.Many2one('shop.product', string='Product ID')
    sales_order_line = fields.Many2One('shop.sales.order', string='Sales Order')
