from odoo import models, fields, api

class TaskManager(models.Model):
    _name = 'task.manager'
    _description = 'Gestor de Tareas'

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    deadline = fields.Date(string="Fecha Límite")
    assigned_to = fields.Many2one('res.users', string="Asignado a")
    priority = fields.Selection([
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta')
    ], string="Prioridad", default='medium')
    done = fields.Boolean(string="Completada", default=False)

    status = fields.Char(string="Estado", compute="_compute_status")

    @api.depends('done')
    def _compute_status(self):
        for record in self:
            record.status = 'Hecho' if record.done else 'Pendiente'
