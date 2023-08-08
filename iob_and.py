from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of signals'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Operand 0'},
        'i1': {'direction':'input', 'description':'Operand 1'},
        'o0': {'direction':'output', 'description':'Result'}
    }

def unit_test():
    """Unit test for iob_and"""

    # Create 3 wires
    w0 = iob_wire(name='w0', width=10, value=0)
    w1 = iob_wire(name='w1', width=10, value=0)
    w2 = iob_wire(name='w2', width=10, value=0)

    width = 10
    
    # Create module variation and an instance
    and0 = iob_and(
        #module
        module_suffix='_'+str(width),
        description=f'2-input bit-wise AND gate with {width} bit operands and result',
        #instance 
        instance_name = 'and0',
        param_dict = {'W': width},
        port_list = [
            {'name': 'i0', 'direction': 'input', 'connect_to': w0},
            {'name': 'i1', 'direction': 'input', 'connect_to': w1},
            {'name': 'o0', 'direction': 'output', 'connect_to': w2}
        ]
    )
                            
    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
