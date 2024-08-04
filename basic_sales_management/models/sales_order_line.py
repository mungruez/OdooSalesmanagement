from odoo import api, models, fields

class ShopSalesOrderLine(models.Model):
    _name = 'shop.sales.order.line'
    _description = 'Sales Order Line'

    product_quantity = fields.Integer(string="Quantity", required=True, track_visibility="always")
    product_id = fields.Many2one(comodel_name='shop.product', string='Product ID', required=True)
    sales_order_line = fields.Many2one(comodel_name='shop.sales.order', string='Sales Order', required=True)

