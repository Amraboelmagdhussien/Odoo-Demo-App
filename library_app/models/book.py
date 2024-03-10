from dateutil.relativedelta import relativedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
     _name = 'library.book'
     _description = 'Book' # for end user understanding
     _rec_name = "title"
     _order = "id"
     _sql_constraints = [
          ('title_unique', 'unique(title)', 'Book title is Already Exist'),
          ('code_unique', 'unique(code)', 'Code Already Exist'),

     ]

     title = fields.Char(string='Title', index=True, required=True) #field type char creating field (attribute string title => name will be shown to end user) (name => column)
     code = fields.Char(required=True)
     active = fields.Boolean(default=True)
     published_date = fields.Date()
     age = fields.Integer(compute='_compute_age')
     state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('publish', 'Publish')]) #selection for list adding limitations for end user orginal charfield
     image = fields.Binary(string='Image')
     publisher_id = fields.Many2one('library.publiisher', required=True)

     @api.constrains('published_date')
     def check_published_date(self):
          for record in self:
               if not record.published_date:
                    raise ValidationError("Published date Must be Added")


     @api.depends('published_date')
     def _compute_age(self):
          for record in self:
               if record.published_date:
                    record.age = relativedelta(fields.Date.today(), record.published_date).years
               else:
                    record.age = False