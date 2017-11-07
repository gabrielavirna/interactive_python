"""
Inheritance: Logic Gates and Circuits
======================================
- Important aspect of OOP: Inheritance is the ability for one class to be related to another class in much the same way
that people can be related to one another. Children inherit characteristics from their parents. Similarly, Python child
classes can inherit characteristic data and behavior from a parent class. These classes are: subclasses & superclasses.

E.g. The built-in Python collections and the relationship structure (inheritance hierarchy)
IS-A Relationship: The list(child, subclass) IS-A sequential collection(parent, superclass).
Lists inherit characteristics: the ordering of the underlying data and operations:concatenation, repetition, indexing.

                                                    -> list
                    ->  Sequential collections      -> string
                                                    -> tuple
Python Collections
                    -> Non-sequential collections   -> dictionary


E.g. Construct an application to simulate digital circuits.
-----------------------------------------------------------
The basic building block for this simulation: the logic gate.
These electronic switches represent boolean algebra relationships between their input and their output.
Generally, gates have a single output line. The value of the output is dependent on the values given on the input lines.

Logic Gates:
-> Binary gates: AND and OR:  two input lines: 0, 1(False, True), a single output line.
-> Unary gate: NOT: a single input line: 0 or 1 (False or True), a single output line.


Circuit: built by combining the gates in various patterns & then applying a set of input values; have logical functions.

AND

  0  1
  -----
0 |0 0
1 |0 1

OR

  0  1
  -----
0 |0 1
1 |1 1

NOT

0 |1
1 |0


"""


class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    # allow a user of a gate to ask the gate for its label (for identification)
    def get_label(self):
        return self.label

    #  to produce output, the gate needs to know specifically what that logic is
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, label):
        # The constructors starts with an explicit call to the constructor of the parent class
        # LogicGate.__init__(self, label)
        super(BinaryGate, self).__init__(label)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input("Enter Pin A input for gate " + self.get_label() + '-->'))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b:
            return int(input("Enter Pin B input for gate " + self.get_label() + '-->'))
        else:
            return self.pin_b.get_from().get_output()

    # the connector must be connected to only of the input line (the available one).
    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                # raise RuntimeError("Error: NO EMPTY PINS")
                print("Cannot Connect: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):
    def __init__(self, label):
        # LogicGate.__init__(self, label)
        super(UnaryGate, self).__init__(label)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_label() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, label):
        # BinaryGate.__init__(self, label)
        super(AndGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        # BinaryGate.__init__(self, label)
        super(OrGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, label):
        # UnaryGate.__init__(self, label)
        super(NotGate, self).__init__(label)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NandGate(AndGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1


# Connector HAS-A LogicGate: connectors will have instances of the
# LogicGate class within them but are not part of the hierarchy.
class Connector:
    # data values will “flow” from the output of one gate into an input line of the next
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        # for making connections
        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

main()

