# dj_affiliate

A simple Django affiliate module.

## Features
- Track affiliate IDs via URL parameters.
- Automatically store affiliate IDs in user sessions.
- Admin interface for managing affiliates and their rewards.

## Installation

Install the module via pip:

```bash
pip install git+https://github.com/EyobAbdella/dj_affiliate.git
```

### Configuration

1. Add `dj_affiliate` to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       "dj_affiliate",
   ]
   ```

2. Add the middleware to your `MIDDLEWARE` list:
   ```python
   MIDDLEWARE = [
       ...,
       "dj_affiliate.middleware.AffiliateMiddleware",
   ]
   ```
3. migrate:
   ```bash
   python3 manage.py makemigrations
   ```

   ```bash
   python3 manage.py migrate
   ```

### Usage

#### Implementing Affiliate Tracking

You can implement affiliate tracking in your views like this:

```python
from decimal import Decimal
from dj_affiliate.models import Affiliate

affiliate_id = request.affiliate
if affiliate_id:
    product_price = order.product.price
    affiliate = Affiliate.objects.get(affiliate_id=affiliate_id)
    reward_increment = product_price * Decimal('0.05')  # 5% reward
    affiliate.reward_amount += reward_increment
    affiliate.save()
```

#### Setting Up Affiliates

1. Go to the Django admin page.
2. Add an affiliate by selecting a registered user and assigning them an `affiliate_id`.

#### Sharing Affiliate Links

Affiliates can share their unique links with customers. The link should include their affiliate ID as a query parameter:

```
http://127.0.0.1:8000/store/products/?affiliate_id=<affiliate_id>
```

When a customer visits this link:
- The affiliate ID is stored in the user's session.
- Any purchases they make can be tracked and rewards calculated for the affiliate.

---

### Example Workflow
1. Affiliate shares their link with a customer.
2. Customer visits the link, and the affiliate ID is stored in their session.
3. Customer places an order.
4. The affiliate's reward is calculated and updated based on the order total.

