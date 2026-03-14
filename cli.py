import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging


def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)

    print("\nOrder Summary")
    print("----------------------")
    print("Symbol:", args.symbol)
    print("Side:", side)
    print("Type:", order_type)
    print("Quantity:", args.quantity)

    try:

        if order_type == "MARKET":

            order = place_market_order(
                args.symbol,
                side,
                args.quantity
            )

        elif order_type == "LIMIT":

            if args.price is None:
                print("Error: LIMIT order requires price")
                return

            print("Price:", args.price)

            order = place_limit_order(
                args.symbol,
                side,
                args.quantity,
                args.price
            )

        print("\nOrder Response")
        print("----------------------")

        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Quantity:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice"))

        print("\n✅ Order placed successfully")

    except Exception as e:

        print("\n❌ Order failed:", str(e))


if __name__ == "__main__":
    main()