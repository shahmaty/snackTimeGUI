from connector import Connector
import runepagecreator, getcurrentrunes

# Hi I'm here to hijack ur code
print("ENTER CHAMPION: ")
champion = input()
createdpage = runepagecreator.createrunepage(champion)

primaryStyleId = createdpage[0]
subStyleId = createdpage[10]
selectedPerkIds = createdpage
selectedPerkIds.pop(10)
selectedPerkIds.pop(0)
runePageName = "SnackTime: " + champion
runePageID = getcurrentrunes.getcurrentrunepage()

connector = Connector()


async def set_rune_page(connection):
    print("Setting created page to page ID: " + str(runePageID) + "...")
    setRunePage = await connection.request('put', "/lol-perks/v1/pages/" + str(runePageID),
                                           data={'autoModifiedSelections': [], 'current': True, 'id': runePageID,
                                                 'isActive': False, 'isDeletable': True, 'isEditable': True,
                                                 'isValid': True, 'lastModified': 1589016704794, 'name': runePageName,
                                                 'order': 1, 'primaryStyleId': primaryStyleId,
                                                 'selectedPerkIds': selectedPerkIds, 'subStyleId': subStyleId})

    if setRunePage.status == 201:
        print("Created page successfully set!")
    else:
        print("An error has occured while setting created page")

# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):
    print('Ready to connect to League Client')

    # check if the user is already logged into his account
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status != 200:
        print('Please login into your account and restart SnackTime script')
    else:
        print("Connecting to League client")
        await set_rune_page(connection)


# fired when League Client is closed (or disconnected from websocket)
@connector.close
async def disconnect(_):
    print('Disconnected from League Client')

# starts the connector
connector.start()
