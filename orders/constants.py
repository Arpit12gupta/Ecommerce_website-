

#--------order_sources
IOS= "iOS"
ANDROID= "Android"
WEB= "Web"
ORDER_SOURCE = [IOS, ANDROID, WEB]
ORDER_SOURCE_CHOICES = [(a,a) for a in ORDER_SOURCE]

#------------Order_status
INCOMPLETE= "Incomplete"
PLACED= "Placed"
ON_HOLD= "On Hold"
SHIPPED="Shipped"
OUT_FOR_DELIVERY="Out for Delivery"
DELIVERED="Order Delivered"
CANCELED="Order Cancelled"
ORDER_STATUS = [INCOMPLETE, ON_HOLD, SHIPPED, OUT_FOR_DELIVERY, DELIVERED, CANCELED]
ORDER_STATUS_CHOICES = [(a,a) for a in ORDER_STATUS]


#------------TRANSACTION_STATUS
FAILED="Transaction Failed"
SUCCESS="Transaction Success"
CANCELLED= "Transaction Cancelled"
REFUNDED="Money Refunded"
TRANSACTION_STATUS = [FAILED, SUCCESS, CANCELED, REFUNDED]
TRANSACTION_STATUS_CHOICES = [(a,a) for a in TRANSACTION_STATUS]

    