class ALU:  # Arithmetic Logic Unit = Rechenwerk
    def __init__(self):
        self.operand = "0"
        self.acc = "0"
        self.operation = " "
        self.result = "0"

    def compute(self):
        if self.operation == "?":  # cmp
            if int(self.acc) > int(self.operand):
                self.result = "1"
            elif int(self.acc) == int(self.operand):
                self.result = "0"
            else:
                self.result = "-1"
                
        else:
            if self.operation == "+":  # add
                self.result = str(int(int(self.acc) + int(self.operand)))

            elif self.operation == "-":  # sub
                self.result = str(int(int(self.acc) - int(self.operand)))

            elif self.operation == "*":  # mul
                self.result = str(int(int(self.acc) * int(self.operand)))

            elif self.operation == "/":  # div
                self.result = str(int(int(self.acc) / int(self.operand)))

            elif self.operation == "%":  # mod
                self.result = str(int(int(self.acc) % int(self.operand)))

            self.acc = self.result
