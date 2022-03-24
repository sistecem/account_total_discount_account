# -*- coding: utf-8 -*-

from odoo import api,fields,models,_


class AccountMove(models.Model):
    _inherit = 'account.move'

    discount_total = fields.Monetary(compute='_total_discount', string='Descuento Total', default=0, readonly=False, store=True)

    @api.depends('state','invoice_line_ids.quantity','invoice_line_ids.price_unit','invoice_line_ids.discount')
    def _total_discount(self):
        # in_draft_mode = self != self._origin

        for invoice in self:
            total_price = 0
            final_discount_amount = 0
            line_ids = []
            account_line_of_discount = None
            if invoice:
                # for line in invoice.line_ids:
                #     # if (line.product_id == 57):
                #     if(line.name=='Descuento Total'):
                #     # if (line.account_id == self.company_id.discount_account_id):
                #         print(line.product_id)
                #         account_line_of_discount = line.id
                #         print(account_line_of_discount)
                #         print('Discount Account Line found - '+str(line.tax_ids)+'-'+str(line.name))
                #         break

                for line in invoice.invoice_line_ids:
                    discount_amount = 0
                    if line.discount:
                        total_price = line.quantity * line.price_unit
                        if total_price:
                            discount_amount = round((total_price * (line.discount/100)),2)
                            if discount_amount:
                                final_discount_amount = final_discount_amount + discount_amount
                                # = line.credit + discount_amount*.87
                                # line.tax_base_amount = line.tax_base_amount + discount_amount*.87
                                # print(line.tax_base_amount)

                #Hacer distincion para ventas y compras
                # if self.type == 'out_refund':
                #     debit = move_line[2].get('debit', 0.0)
                #     debit += line.discount_amt
                #     move_line[2].update({'debit': debit})
                # elif self.type == 'out_invoice':
                #     credit = move_line[2].get('credit', 0.0)
                #     credit += line.discount_amt
                #     move_line[2].update({'credit': credit})

                # if (final_discount_amount > 0):
                #         balance = -final_discount_amount
                #         to_write_on_line = {
                #             # 'amount_currency': final_discount_amount,
                #             # 'currency_id': taxes_map_entry['grouping_dict']['currency_id'],
                #             'name': 'Descuento Actualizado',
                #             'price_unit': round(-balance * .87, 2),
                #             'amount_currency': balance * .87,
                #             'credit': -balance * .87,
                #
                #         }
                #         # invoice.invoice_line_ids.create({line_ids})
                #
                #         # line_discount = self.env['account.tax.repartition.line'].browse(
                #         # line_discount = self.env['account.move.line'].browse(
                #         #     values['move_id'])
                #         print(account_line_of_discount)
                #
                #         #removing the discount line
                #         grouping_key = 'Discount'
                #         discount_map = {}
                #         # grouping_key = _serialize_discount_grouping_key(grouping_dict)
                #         # to_remove = self.env['account.move.line']
                #         # for line in self.line_ids:
                #         #     # if grouping_key in discount_map:
                #         #     if ('Descuento Total' in str(line.name)):
                #         #         # A line with the same key does already exist, we only need one
                #         #         # to modify it; we have to drop this one.
                #         #         to_remove += line
                #         # self.line_ids -= to_remove
                #
                #
                #         discount_map_entry = discount_map.setdefault(grouping_key,{
                #             'discount_line': account_line_of_discount,
                #             # 'amount': final_discount_amount*.87,
                #             # 'tax_base_amount': 0.0,
                #             'grouping_dict': False,
                #         })
                #
                #         print('Map entry '+str(discount_map_entry['discount_line']))
                #         if account_line_of_discount:
                #             # if discount_map_entry['discount_line'] :
                #             # Update an existing discount line.
                #             print('do nothing')
                #             # self.line_ids = account_line_of_discount
                #             # discount_map_entry['discount_line'].update(to_write_on_line)
                #         else:
                #             create_method = in_draft_mode and self.env['account.move.line'].new or self.env['account.move.line'].create
                #             discount_map_entry['discount_line'] = create_method(
                #                 {'name': 'Descuento Total',
                #                  'move_id': self.id,
                #                  'move_name': self.name,
                #                  'partner_id': self.partner_id.id,
                #                  'company_id': self.company_id.id,
                #                  'exclude_from_invoice_tab': True,
                #                  # 'product_id': 57,
                #                  'quantity': 1,
                #
                #                  # 'tax_base_amount': -balance,
                #                  # 'tax_base_amount': tax_base_amount,
                #                  # 'tax_exigible': tax.tax_exigibility == 'on_invoice',
                #                  'journal_id': self.journal_id.id,
                #                  'amount_residual': 0,
                #                  'amount_residual_currency': 0,
                #                  'company_currency_id': self.company_id.currency_id,
                #                  # 'blocked': False,
                #                  # 'reconciled': False,
                #                  'date': self.date or fields.Date.context_today(self),
                #                  'currency_id': self.currency_id,
                #                  'price_unit': round(-balance * .87, 2),
                #                  'amount_currency': round(balance * .87,2),
                #                  'credit': round(-balance * .87,2),
                #                  'debit': 0,
                #                  # 'debit': balance > 0.0 and balance or 0.0,
                #                  # 'credit': balance < 0.0 and -balance or 0.0,
                #                  'account_id': self.company_id.discount_account_id,
                #                  'a': self.a,
                #                  'parent_state': self.state,
                #                  'is_rounding_line': False,
                #                  'tax_ids': self.company_id.discount_tax_id,
                #                  })
                #             # print(discount_map_entry['discount_line'].tax_ids.id)
                #             self._recompute_tax_lines()
                #             self._onchange_recompute_dynamic_lines()
                #
                #             # discount_map_entry['discount_line'].update(to_write_on_line)
                #             # discount_map_entry['discount_line'].update(discount_map_entry['discount_line']._get_fields_onchange_balance(force_computation=True))
                #
                #
                #         # if in_draft_mode:
                #         #     discount_map_entry['discount_line'].update(
                #         #         discount_map_entry['discount_line']._get_fields_onchange_balance(force_computation=True))
                #
                # invoice.update({'amount_total': self.amount_total+final_discount_amount*.87})
                invoice.update({'discount_total': final_discount_amount})
            invoice.discount_total = final_discount_amount



