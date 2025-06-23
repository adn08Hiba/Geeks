class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)

    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To: {msg['to']} | Message: {msg['content']}")

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From: {msg['from']} | Message: {msg['content']}")

    def show_messages_from(self, number):
        print(f"Messages from {number}:")
        for msg in self.messages:
            if msg["from"] == number and msg["to"] == self.phone_number:
                print(f"Message: {msg['content']}")

phone1 = Phone("0600000001")
phone2 = Phone("0600000002")


phone1.call(phone2)
phone2.call(phone1)

phone1.show_call_history()
phone2.show_call_history()

phone1.send_message(phone2, "Salut !")
phone2.send_message(phone1, "Salut, ça va ?")
phone1.send_message(phone2, "Oui, très bien !")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()

phone2.show_outgoing_messages()
phone2.show_incoming_messages()

phone2.show_messages_from("0600000001")
