# Gaming Gadget Store Billing System

This is a console-based billing system for a Gadget Gaming Store. It handles customer orders, calculates totals, applies discounts, manages delivery and gift options, and tracks loyalty points. Here’s the thing: it’s designed to let a customer go from picking products to completing payment all in one flow, without unnecessary complications.

---

## Features

### User Authentication
- Customers can register with a **username**, **password**, and **4-digit PIN**.  
- Returning users can log in using their credentials.  
- The system prevents duplicate usernames and ensures secure authentication for payments.

### Product Catalog
- The store sells gaming gadgets such as:
  - Keyboards
  - Mice
  - Chairs
  - Monitors
  - Headsets
  - Other gaming accessories
- Customers can view a clear list of items with prices and select quantities for each product.

### Cart Management
- Users can add multiple items to the cart.  
- Quantities for each item can be adjusted before checkout.

### Delivery Options
- **Home Delivery** – Rs. 200  
- **Store Pickup** – Free

### Gift Wrapping
Customers can choose per-item wrapping:  
- **Basic Wrap** – Rs. 100 per item  
- **Premium Box** – Rs. 300 per item  
- **No Wrap** – Rs. 0  

### Membership Discounts
If the customer is a member:  
- **Platinum Member** – 25% discount  
- **Gold Member** – 15% discount  
- **Silver Member** – 10% discount  

New customers can also purchase membership during checkout, which applies the discount immediately.

### Taxes
VAT is applied based on location:  
- **Inside Kathmandu** – 13%  
- **Outside Kathmandu** – 15%

### Billing
The system generates a detailed bill that includes:  
- Items purchased with quantities and prices  
- Membership discounts and type  
- Tax, delivery, and gift wrap charges  
- Grand total  
- Loyalty points earned  

All bills are **saved in a record file** for future reference.

### Payment Options
Customers can pay via:  
- **ATM/Card** – Requires entering registered credentials and 4-digit PIN. Maximum 3 attempts allowed.  
- **Cash on Delivery/Pickup**  

---

## How to Use

1. Run the program in a Python environment.  
2. Choose whether to place an order.  
3. Login or register as a new user.  
4. Browse the gadget catalog and select items with quantities.  
5. Choose delivery and gift wrap options.  
6. Confirm membership status or purchase membership for discounts.  
7. Review taxes applied and the grand total.  
8. Proceed to payment via ATM or opt for cash.  
9. Bills and payment records are automatically saved.

---

## File Structure

- `shopdata.txt` – Stores registered user credentials.  
- `atmdata.txt` – Logs ATM payments.  
- `record.txt` – Maintains billing records for all transactions.

---

## Notes

- Quantity input must be **at least 1**.  
- Users have **three login attempts** before the program exits.  
- Loyalty points are calculated as **1 point per 100 Rs.** of the final bill.  
- The program is fully console-based; no GUI is required.  

---