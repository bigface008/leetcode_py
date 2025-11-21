import heapq
from typing import List, Tuple, Dict


# 5.	Code exercise - Simulated Exchange
#   This code exercise is to simulate exchange for matching orders.
#   - When an order is input, an unique order Id is assigned to the order.
#   - Orders are matched in the ordering of price and time priorities.
#   Please finish class Exchange to fulfil the task in main function.
class Order:
    def __init__(self, order_id: int, side: int, volume: int, price: float):
        self.order_id = order_id
        self.side = side
        self.remain_volume = volume
        self.price = price
        self.traded_volume = 0
        self.traded_money = 0


class Exchange:
    def __init__(self):
        self.orders: Dict[int, Order] = dict()
        self.sell_min_hp: List[Tuple[int, Order]] = [] # sell_price, order
        self.buy_max_hp: List[Tuple[int, Order]] = [] # -buy_price, order

    def InputOrder(self, side: int, volume: int, price: float) -> int:
        """
        InputOrder receives order, and return assigned order Id.
        :param side: 0 is buy, 1 is sell,-1 means not valid
        :param volume:order's quantity
        :param price:order's prices
        :return: order Id, an integer
        """
        if side == -1:
            return -1

        order_id = len(self.orders)
        new_order = Order(order_id, side, volume, price)
        self.orders[order_id] = new_order

        if side == 0:
            # Buy
            while self.sell_min_hp and new_order.remain_volume > 0:
                buy_price, buy_order = self.sell_min_hp[0]
                if buy_price > price:
                    break
                trade_volume = min(buy_order.remain_volume, new_order.remain_volume)

                buy_order.remain_volume -= trade_volume
                buy_order.traded_volume += trade_volume
                buy_order.traded_money += trade_volume * buy_price

                new_order.remain_volume -= trade_volume
                new_order.traded_volume += trade_volume
                new_order.traded_money += trade_volume * buy_price

                if buy_order.remain_volume == 0:
                    heapq.heappop(self.sell_min_hp)
            if new_order.remain_volume > 0:
                heapq.heappush(self.buy_max_hp, (-price, new_order))
        else:
            # Sell
            while self.buy_max_hp and new_order.remain_volume > 0:
                buy_price, buy_order = self.buy_max_hp[0]
                buy_price = -buy_price
                if buy_price < price:
                    break
                trade_volume = min(buy_order.remain_volume, new_order.remain_volume)

                buy_order.remain_volume -= trade_volume
                buy_order.traded_volume += trade_volume
                buy_order.traded_money += trade_volume * buy_price

                new_order.remain_volume -= trade_volume
                new_order.traded_volume += trade_volume
                new_order.traded_money += trade_volume * buy_price

                if buy_order.remain_volume == 0:
                    heapq.heappop(self.buy_max_hp)
            if new_order.remain_volume > 0:
                heapq.heappush(self.sell_min_hp, (price, new_order))
        return order_id

    def QueryOrderTrade(self, orderId: int) -> Tuple[int, float]:
        """
        queries order's trade volume and average price.
        :param orderId: assigned order Id
        :return: (order's trade volume, avg_price),tuple
        """
        if orderId not in self.orders:
            return (0, 0.0)
        order = self.orders[orderId]
        if order.traded_volume == 0:
            return (0, 0.0)
        return order.traded_volume, order.traded_money / order.traded_volume


if __name__ == "__main__":
    ex = Exchange()
    orders = list()

    orders.append(ex.InputOrder(0, 1, 100))
    orders.append(ex.InputOrder(0, 2, 101))
    orders.append(ex.InputOrder(0, 3, 102))
    orders.append(ex.InputOrder(1, 4, 100))
    orders.append(ex.InputOrder(1, 5, 101))
    orders.append(ex.InputOrder(1, 6, 102))

    for orderId in orders:
        tradeVolume, avgPrice = ex.QueryOrderTrade(orderId)
        print("orderId:%d,tradeVolume:%d,averagePrcies:%f" % (orderId, tradeVolume, avgPrice))


# 0, 1, 100
# 0, 2, 100

