# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time

from openerp.osv import osv, fields

class account_analytic_balance_plan(osv.osv_memory):
    _name = 'account.analytic.balance.plan'
    _description = 'Account Analytic Planning Balance'

    _columns = {
        'date1': fields.date('Start of period', required=True),
        'date2': fields.date('End of period', required=True),
        'empty_acc': fields.boolean('Empty Accounts ? ', help='Check if you want to display Accounts with 0 balance too.'),
        'crossovered_budget_id': fields.many2one('crossovered.budget', 'Budget', required=False),
    }

    _defaults = {
        'date1': lambda *a: time.strftime('%Y-01-01'),
        'date2': lambda *a: time.strftime('%Y-%m-%d')
    }

    def check_report(self, cr, uid, ids, context=None):
        datas = {}
        if context is None:
            context = {}
        data = self.read(cr, uid, ids)[0]
        datas = {
             'ids': context.get('active_ids',[]),
             'model': 'account.analytic.account',
             'form': data
                 }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'account.analytic.account.balance.plan',
            'datas': datas,
            }

account_analytic_balance_plan()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

