# Otherworlds
Otherworlds E-commerce App - Code Institute Project 5

This is a real-world e-commerce site, built for an artist who designs and makes creatures made from copper and silver wire that are sold all over the world.

Users/customers are able to browse the website, register as a customer, login and view products fully or via their respective categories. They can add items to cart, remove and once happy can checkout using the Stripe payment system.

This website was built for my sister and her business.

# Demo
A live demo of this project can be found at https://otherworlds.herokuapp.com/. This application is hosted on Heroku using a Postgres (MySQL Database)

# UX
This site is intended for use by established and new Customers of Otherworlds to allow them to view new products and purchase them with ease. They can do this via the Products page, and from the individual product information, or via their respective categories.

By paying online, it makes it easier for the the owner of Otherworlds to keep track of who paid and what they ordered, rather than having to keep track of checks or multiple spreadsheets.

No template was used to build this site. There were some specific UX and UI designs that were taken into consideration when styling this site.

The Navigation Bar and Footer are featured on every page, with the exception of the Checkout page, so that the website was easily navigable for customers. This gives a more unified and structured approach to the design.

The Home Page also has links to the shop in full, and links to the products based off their categories, this again is for customers' ease of use.

The products featured are large in size and are fully responsive when viewed on smaller screens. This is because the customer base for the business is mainly the middle aged and elderly who have trouble viewing small images, this was also the reason for larger font sizes used throughout.

The colour scheme flows throughout, with only 3 to four colours used (including black). This is to ensure consistency and a pleasant easy on the eye website, which keeps it minimalist and clear.

A user will have to sign-up and login to view the Checkout, and will be prompted to do this once they click 'Checkout' on the Cart page.

The individual products page has smaller thumbnail images that, when clicked, appear in the box where the original product image was. This allows the customer to view multiple angles of the product. This was built using jQuery and took a long time to perfect.

The admin is only accessible by myself, and the owner of Otherworlds.

# Technologies
1. Django (1.0)
2. Heroku
3. Postgres Database (MySQL)
4. Stripe Payment
5. Javascript/jQuery
6. HTML
7. CSS
8. Bootstrap (3.3.7)
9. SendGrid

# Development Process
## Automated Testing
All automated testing was done using Travis-CI. There is automated testing done for all apps with views, models, and forms (where applicable).

[![Build Status](https://travis-ci.org/NathenJohns/otherworlds.svg?branch=master)](https://travis-ci.org/NathenJohns/otherworlds).

## Manual Testing

Manual testing was done for all adding/amending/delete/appearance functions in both the Shop, Product and Cart pages/apps. This was to ensure that what was supposed to be deleting was deleting, what was being added was being added and so on.

It was also tested that only designated users i.e. the user signed in to the website was able to delete/edit/add their products to the cart. All links and forms are verified to be working correctly via manual testing.

The Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard.

# Features
Only myself and the owner of Otherworlds have access to the admin page. Since it is her business' site, it makes it easier for her to monitor all account activity, orders and product information. She will be the only one who will be allowed to make master changes to the site. As this site is an ecommerce one with full functionality, payments are processed through Stripe, and since it is a (soon to be) live site, it only processes all types of payments.

The Shop section allows customers to view all products, add them to the cart, view different pages, or go to the individual product details. They are able to search by term i.e. "monkey", "brooch" or other detailed information about the item. They are also able to view and filter products by category using the drop-down menu.

There are different apps throughout because the aim was to keep most functionality as separate as possible, this is because if they were included in the same app, there would have been too much content in one app causing confusion when changing code.

This is why there is a separate 'search' app rather than integrating that code into the 'products' app (whereas filter by category is in the 'products' app). It is also for that reason that 'information' is separate to 'home' as this content is similar to each other whereas 'home' is only for features on the home page.

The 'cart' section allows a customer to view the items when they add them to the cart, amend the cart and delete items. When deleting an item a modal will appear for confirmation, and the customer will not be able to amend the item to a non iteger item (this was previously allowed and created errors but has since been rectified). A customer will not be able to be viewed (on the navigation bar) until they have added an item and will not be able to progress further until they are logged in.

## Features Left to Implement
I would like to add more styles and designs for the Checkout Page i.e. images of Mastercard, PayPal and Debit, like other ecommerce based websites do. This is more of a personal preference rather than functionality wish but something to consider.

Another feature that would make the user experience more appealing would be the use of a "zoomable" effect on the Single Product page, so that when a user hovers over the image, a larger view of it can be seen. After intensive research into this, it was deemed too time consuming to implement correctly but something that can be done at a later date.

Having signed up with SendGrid (this needs to be the owners account and not mine), a customer who forgets their password can request a new one and SendGrid sends them an email once they enter their email address on the "Forgot Password" page. It would be
useful to have this same feature but for when a customer pays for their items and on submission a confirmation email stating that their order has been successful and details the products they purchased is sent.

# Credits
## Content
All content was provided by Saffron (the owner of Otherworlds) and from her Etsy page. It is correct at the time of completion.

## Media
All photos and product images were taken and provided by Saffron Johns.

# Installation
If you're interested in cloning this repository, to set up and install everything in the requirements.txt run the following command in the terminal:

> $ sudo pip3 -r install requirements.txt

Please note that this project was built using Cloud9, so if another editor is used, the terminal commands may differ. You should consult the documentation of the editor you're using for further information on commands. All secret keys for AWS, Stripe, Production, and Django Settings in Heroku will need to be obtained individually, as they are hidden.

To run the app in Cloud9, open the bash terminal and enter "run" and click enter. This will open a link that can be viewed on Chrome.