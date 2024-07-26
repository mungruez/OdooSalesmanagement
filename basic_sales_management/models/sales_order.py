from odoo import models, fields, api,  _

class ShopSalesOrder(models.Model):
    _name = 'shop.sales.order'
    _description = 'Sales Order Record'

    order_date = fields.Date(string='Name', required=True,  track_visibility="always")
    customer_id = fields.Many2one('shop.customer', string='Customer ID')
    sales_order_lines = fields.One2many('shop.sales.order.line', 'sales_order_line', string='Sales Order Lines')