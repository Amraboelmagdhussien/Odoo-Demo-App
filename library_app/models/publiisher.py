import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Publiisher(models.Model):
    _name = 'library.publiisher'
    _description = 'Publisher'
    _rec_name = 'fname'

    fname = fields.Char()
    lname = fields.Char()
    date_join = fields.Date()
    active = fields.Boolean(default=True)
    national_id = fields.Char()
    image = fields.Binary()
    mobile = fields.Char(required=True)
    book_ids = fields.One2many('library.book', 'publisher_id')

    @api.constrains('mobile')
    def check_mobile_number(self):
        for record in self:
            if not re.match(r"^01[0-25]\d{8}$", record.mobile):
                raise ValidationError("Phone Number must Follow the Egyptian Rules: Starts with 01 Followed by a digit that can be 0, 1, 2, or 5. Followed by exactly 8 more digits.")