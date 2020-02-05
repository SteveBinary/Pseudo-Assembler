class CACHE:  # Speicherwerk
    def __init__(self):
        self.cells = dict()

    def read(self, adr):
        try:
            return self.cells[adr]
        except KeyError:  # Falls noch kein Wert an dieser Adresse gespeichert ist, wird die Speicherzelle mit 0 belegt.
            self.write(adr, "0")
            return self.cells[adr]

    def write(self, adr, val):
        self.cells[adr] = val
