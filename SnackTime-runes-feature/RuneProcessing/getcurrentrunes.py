# this god awful piece of code gets the currently selected rune page using the undocumented (like the mexicans) api
# in order to query the client websocket which needs documentation or deportation

from lcu_driver import Connector


def getcurrentrunepage():

    connector = Connector()

    async def get_rune_page(connection):
        currentrune = await connection.request('get', '/lol-perks/v1/currentpage')
        if currentrune.status == 200:
            print("Obtaining current rune page from League client...")
            # print(dir(currentrune))
            # print(await currentrune.json())
            runes = await currentrune.json()
            global runeid
            runeid = runes.get("id")
            print("Acquired rune page ID: " + str(runeid))
            return runeid

            # print("these are the runes", currentrune)
        else:
            print("yeah idk wtf is going on lmao")

    @connector.ready
    async def connect(connection):
        print('Ready to connect to League Client')

        # check if the user is already logged into his account
        summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
        if summoner.status != 200:
            print('Please login into your account and restart SnackTime script')
        else:
            print("Connecting to League client")
            await get_rune_page(connection)
            return runeid

    # fired when League Client is closed (or disconnected from websocket)
    @connector.close
    async def disconnect(_):
        print('Disconnected from League client')

    # starts the connector
    connector.start()

    return runeid



getcurrentrunepage()
