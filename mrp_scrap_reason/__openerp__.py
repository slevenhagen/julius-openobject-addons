# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    "name" : "MRP Scrap Reason",
    "version" : "0.1",
    "author" : "Julius Network Solutions , Novapoint Group INC (Ruby Chauhan)",
    "website" : "http://julius.fr",
    "category" : "Manufacturing",
    "depends" : [
        'mrp',
        'stock',
    ],
    "description": """
    This module will add a new object reason for scraping components
    """,
    "demo" : [],
    "data" : [
        "security/ir.model.access.csv",
        "wizard/scrap_view.xml",
        "mrp_view.xml",
        "stock_view.xml",
    ],
    'installable' : True,
    'active' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
