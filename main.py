import websocket
import json
import time


n = 0
up = 0
down = 0
price = 0.0

def on_open(ws):
    json_data = json.dumps({'ticks':'frxEURUSD'})
    ws.send(json_data)

def on_message(ws, message):

    global n
    global up
    global down
    global price

    m = json.loads(message)

    #print('ticks update: %s' % message)
    #bid = float(m['tick']['bid'])
    #ask = float(m['tick']['ask'])
    quote = float(m['tick']['quote'])

    if n == 0:
        price = quote

    n = n + 1

    print ('# %d | Entrey %f Exit %f' % (n, price, quote))

    if n % 5 == 0:

        n = 0

        if quote > price:
            print ("\tUP")
            up = up + 1
        else:
            print ("\tDOWN")
            down = down + 1

        price = quote

        print ("\nREPORT: UP %d DOWN %d" % (up,down))

        if up + down >= 50:

            up = 0
            down = 0

            if up - down > 6:
                print ("binary-bot-up.xml")

            elif down - up > 6:
                print ("binary-bot-down.xml")

            else:
                print ("binary-bot.xml")

            time.sleep(20)






    #print('BID:' + m['tick']['bid'])
    #print('ASK:' + m['tick']['ask'])
    #print('QUOTE:' + m['tick']['quote'])







if __name__ == "__main__":
    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()

