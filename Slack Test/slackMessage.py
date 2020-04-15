import requests as rq
import json

def sendMessage():
    done = False
    print("Enter message to send, press Enter for next steps.") 
    print("Respond to prompts to send multi-line message.")
    message = input()
    while (not done):       
        print("Your current message is: \n" + message)
        print("Would you like to send it? If more to add, enter 'y', else 'n'.")
        prompt = input()
        if (prompt == "y"):
            print("Enter the next part of your message.")
            newLine = input()
            message += "\n" + newLine
        elif (prompt == "n"):
            done = True
    return message

# https://api.slack.com/reference/surfaces/formatting#linking_to_channels_and_users
def auto():
    message = "@channel Just a reminder that the main channels " \
        "for raiding and helpful information are #random and #pogoinfo! " \
        "Also, the current moderators are <@UA0JFTHGA>, @JG, and TODO. " \
        "Please send us a message if there are issues with anything!\n" \
        "THIS MESSAGE WAS SENT AUTOMATICALLY BY A BOT. DO NOT RESPOND TO THIS MESSAGE."
    return message

which = input("Enter A for auto message, M for manual message: \n")

if (which == "A"):
    message = auto()
    print(message)
elif (which == "M"):
    message = sendMessage()
else:
    message = "ERROR. PLEASE CONTACT THE ADMINSTRATOR OF THE BOT!"

channelID = "CA0BLLNUC"
url = "http://slack.com/api/chat.postMessage?"

headers = {
    "User-Agent": "BotRepeat/0.1",
    "connection": "keep-alive"
}

with open ("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

send = {
    "token": token,
    "channel": channelID,
    "text": message,
    "link_names": "true",
    "username": "BOT",
    "pretty": 1
}

S = rq.Session()

req = rq.Request('POST', url=url, headers=headers, params=send)
prepared = req.prepare()

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

pretty_print_POST(prepared)

E = S.get(url=url, headers=headers, params=send).json()
print(E)


# https://slack.com/api/chat.postMessage?
# token=xoxb-339928689920-1075450810401-NpVPXyUjcogkhrWeciKekKiU
# &channel=CA0BLLNUC
# &text=TEST%20%40JG%2C%20%23random
# &link_names=true
# &username=BOT
# &pretty=1