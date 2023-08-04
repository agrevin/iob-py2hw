from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    # Default ports and parameters
    ports = {'i': 'input',
            'o0': 'output'}
    params = [{'name': 'W', 'min_value': 1, 'max_value': 32},
            {'name': 'N', 'min_value': 2, 'max_value': 32}]

def unit_test():
    """Unit test for iob_and"""

    # Create 3 wires
    w0 = iob_wire('w0', 10, 0)
    w1 = iob_wire('w1', 10, 0)
    w2 = iob_wire('w2', 10, 0)
    
    # Create module
    and0 = iob_and('and0', [{'name': 'i0', 'wire': w0, 'direction': 'input'},
                            {'name': 'i1', 'wire': w1, 'direction': 'input'},
                            {'name': 'o0', 'wire': w2, 'direction': 'output'}],
                            {'W': 10, 'N': 2}, '_0')
                            
    
    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
