import vonage

client = vonage.Client(key="1e9486a3", secret="w67XX2DuRpsxINR4")
sms = vonage.Sms(client)

def send_sms(tonumber):
    responseData = sms.send_message(
        {
            "from": "18665173046",
            "to": f"{tonumber}",
            "text": "Hello a friend would like to send you a surprise gift, using FlexiGift. \
                \nIf you would like to accept your gift, please click the link below. \
                    We will gather your information for your special delivery! \
                        Don't worry, your address will remain anonymous. \
                https://www.myflexigift.com/address-2.html#/",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
        return "Message sent successfully."
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        return f"Message failed with error: {responseData['messages'][0]['error-text']}"

if __name__ == '__main__':
    send_sms(17066149026)
    # send_sms(+923117039097)
