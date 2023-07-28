from iob_datum import iob_datum
from iob_wire import iob_wire

class iob_port(iob_datum):
    """Class to represent a port in an iob module"""

    def __init__(self, name, width,  value, direction = "input"):
        super().__init__(name, width, value)
        self.direction = direction
        # test if direction is 'input', 'output', 'inout'; exit with error otherwise
        if direction not in ["input", "output", "inout"]:
            print(f"Error: Direction must be 'input', 'output', or 'inout'.")
            exit(1)

        # If value is a iob_wire instance, check if the width matches
        if isinstance(value, iob_wire):
            if value.width != width:
                print(f"Error: Port {self.name} width ({self.width}) does not match wire {value.name} width ({value.width}).")
                exit(1)
        
    def print_port(self, comma=True):
        if comma:
            print(f"      {self.direction} [{self.width}-1:0] {self.name},")
        else:
            print(f"      {self.direction} [{self.width}-1:0] {self.name}")

        
    def print_port_assign(self, comma=True):
        if self.value == None:
            print(f"Error: Port {self.name} is not connected to a wire.")
            exit(1)
        if comma:
            print(f"      .{self.name}({self.value.name}),")
        else:
            print(f"      .{self.name}({self.value.name})")

def unit_test():
    """Unit test for iob_port"""
    
    # Create 3 wires
    wire0 = iob_wire("wire0", 8, 1)
    wire1 = iob_wire("wire1", 8, 2)
    wire2 = iob_wire("wire2", 8, 3)

    # Create 3 ports
    port0 = iob_port("port0", 8, wire0, "input")
    port1 = iob_port("port1", 8, wire1, "output")
    port2 = iob_port("port2", 8, wire2, "inout")

    # Check if the ports are correct

    print(f"port0: {port0.name}, {port0.width}, {port0.value}, {port0.direction}")
    assert port0.name == "port0"
    assert port0.width == 8
    assert port0.value == wire0
    assert port0.direction == "input"

    print(f"port1: {port1.name}, {port1.width}, {port1.value}, {port1.direction}")
    assert port1.name == "port1"
    assert port1.width == 8
    assert port1.value == wire1
    assert port1.direction == "output"

    print(f"port2: {port2.name}, {port2.width}, {port2.value}, {port2.direction}")
    assert port2.name == "port2"
    assert port2.width == 8
    assert port2.value == wire2
    assert port2.direction == "inout"

    port0.print_port()
    port1.print_port()
    port2.print_port()

    port0.print_port_assign()
    port1.print_port_assign()
    port2.print_port_assign()
    

    print("End of unit test for iob_port.")

# Test code
if __name__ == "__main__":
    unit_test()
