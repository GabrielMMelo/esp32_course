import mfrc522

RF_SCK = 12  # clock
RF_SDA = 13  # data
RF_MOSI = 14  # master-out slave-in
RF_MISO = 27  # master-in slave-out
RF_RST = 26  # reset


class Mfrc522():
    def __init__(self, allowed_id='0x64963524'):
        self.rdr = mfrc522.MFRC522(RF_SCK, RF_MOSI, RF_MISO, RF_RST, RF_SDA)
        self.allowed_id = allowed_id
        self.read()

    def read(self):
        while True:
            (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
            if stat == self.rdr.OK:
                (stat, raw_uid) = self.rdr.anticoll()
                try:
                    read = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    if read == self.allowed_id:
                        print("Usuário permitido :) -", read)
                    else:
                        print("Usuário não permitido :( -", read)
                except IndexError:
                    pass
