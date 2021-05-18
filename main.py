class Inkop:
    def __init__(self, insaltad, namn, sedel_datum, sedel_vikt,
                 brutto, avdrag, anv_kod):
        self.insaltad = insaltad
        self.namn = namn
        self.sedel_datum = sedel_datum
        self.sedel_vikt = sedel_vikt
        self.brutto = brutto
        self.avdrag = avdrag
        self.netto = self.brutto - self.avdrag
        self.anv_kod = anv_kod


class ERapport(Inkop):
    def __init__(self):
        super().__init__(
            self.insaltad,
            self.namn,
            self.sedel_datum,
            self.sedel_vikt,
            self.brutto,
            self.avdrag,
            self.anv_kod
        )


class VagJournal(ERapport):
    def __init__(self):
        super().__init__()

test = VagJournal()
test.namn = 'Fredrik Karlsson'
print(test.namn)