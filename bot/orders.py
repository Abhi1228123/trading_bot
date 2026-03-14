import logging
from bot.client import client


def place_market_order(symbol, side, quantity):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
            recvWindow=60000
        )

        logging.info(f"Market Order Request: {symbol} {side} {quantity}")
        logging.info(f"Market Order Response: {order}")

        return order

    except Exception as e:

        logging.error(f"Market order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
            recvWindow=60000
        )

        logging.info(f"Limit Order Request: {symbol} {side} {quantity} @ {price}")
        logging.info(f"Limit Order Response: {order}")

        return order

    except Exception as e:

        logging.error(f"Limit order failed: {e}")
        raise