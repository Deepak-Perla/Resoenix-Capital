from fyers_api import fyersModel
client_id = 'client_id'
token='token_id'
fyers=fyersModel.FyersModel(client_id=client_id,token=token,)
order_id={
    'symbol':'ticker_symbol_id',
    'qty':enter_qty,
    'type':2,
    'side':1,
    'productType':'MARGIN',
    'limitPrice':enter_price,
    'stopPrice':enter_price,
    'validity':'DAY',
    'disclosedQty':enter_qty,
    'offlineOrder':'False',
    'stopLoss':enter_price,
    'takeProfit':enter_price,
}

order_id=fyers.place_order(order_id)['id']
orders={'id':order_id}
print(fyers.orderbook(orders))