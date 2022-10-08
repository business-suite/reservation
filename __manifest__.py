# -*- coding: utf-8 -*-

{
  "name"                 :  "Odoo Booking & Reservation Management",
  "summary"              :  """Booking & reservation management in Odoo allows users to take appointment and ticket booking facility in Odoo website.""",
  "category"             :  "Website",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "Business Suite Team",
  "description"          :  """Odoo booking & reservation management
        Odoo Subscription Management
        Odoo Website Subscription Management
        Odoo appointment management
        Odoo website Appointment Management
        Schedule bookings
        Tickets
        Reservations
        Booking Facility in Odoo
        Website booking system
        Appointment management system in Odoo
        Booking & reservation management in Odoo
        Reservation management in Odoo
        Booking
        Reservation
        Booking and reservation""",
  "depends"              :  ['website_sale'],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'views/booking_config_view.xml',
                             'views/booking_sol_view.xml',
                             'wizard/bk_qty_available_wizard_view.xml',
                             'views/product_template_view.xml',
                             'views/booking_product_cart_temp.xml',
                             'views/booking_template.xml',
                             'views/ir_crons.xml',
                            ],
  "assets"               : {
          'web.assets_frontend': [
                          'website_booking_system/static/src/css/booking_n_reservation.css',
                          'website_booking_system/static/src/css/booking_n_res_mob.css',
                          'website_booking_system/static/src/js/booking_n_reservation.js',
                      ],
                            },
  "images"               :  ['static/description/Banner.gif'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}
