# Uniik Estate - Custom Odoo Real Estate Module

Uniik Estate is a custom Odoo 18 module designed to manage real estate properties, offers, and buyers. It allows users to list properties, receive offers from clients, accept or refuse offers, and track the sale status.

## 🚀 Features

- Property listing with details (name, description, price, etc.)
- Offer management per property
- Accept/refuse offers manually
- Automatically updates selling price and buyer details
- Tracks property state (`New`, `Offer Received`, `Offer Accepted`, `Sold`, `Canceled`)
- Integrated with Odoo’s partner (customer) model
- Demo data included for quick testing

## 🛠️ Installation

1. Clone this repository or place the `uniik_estate` module into your Odoo `custom_addons` directory:

   ```bash
   git clone https://github.com/uniquetheo/odoo-docker.git

   ```

2. Ensure the module path is mounted in your docker-compose.yml:
   volumes:

   - ./custom_addons:/mnt/extra-addons

3. Start your Odoo container:
   docker-compose up

4. Log into Odoo as an admin user, activate Developer Mode, and install the Uniik Estate module from the Apps menu.

⚙️ Usage
Go to the Estate menu in Odoo.

Create new properties and view existing ones.

Create offers from the related tab on a property form.

Use the Accept or Refuse buttons to manage offer status.

The property state and selling price update automatically when an offer is accepted.

Developed with ❤️ by Theo Mercifield | https://uniiktheo.tech
