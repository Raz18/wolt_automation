import uuid


class CheckoutPage:
    """
    A mock checkout page with a payment simulation method.
    """

    def pay(self, price, restaurant_name):
        """
        Simulate a payment and return a success message if the price of the order is larger than 0.
        """
        if price > 0:
            transaction_id = uuid.uuid4()  # Generate a unique transaction ID
            return {
                "status": "SUCCESS",
                "transaction_id": str(transaction_id),
                "amount": round(price, 2),
                "restaurant_name": restaurant_name,
                "message": "Payment processed successfully."

            }
        else:
            return {
                "status": "FAILED",
                "transaction_id": None,
                "amount": round(price, 2),
                "restaurant_name": restaurant_name,
                "message":"Payment failed. Order price is not sufficient.",
            }
