from odoo import api, models, fields

class ShopSalesOrder(models.Model):
    _name = 'shop.sales.order'
    _description = 'Sales Order Record'

    order_date = fields.Datetime(string="Order Date", required=True, default=fields.Datetime.now, track_visibility="always")
    customer_id = fields.Many2one(comodel_name='shop.customer', string='Customer ID', required=True)
    sales_order_lines = fields.One2many('shop.sales.order.line', 'sales_order_line', string='Sales Order Lines')
