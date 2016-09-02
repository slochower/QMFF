from parmed.tools import changeLJSingleType

def manipulate_lj(reference, atom, radius, epsilon):
    '''
    Write out a new parameter file with `parameter` set to `value`.
    The `parameter` must be in the form `parmed` can understand.
    The `reference` set must be a `parmed` object.
    '''
    # action = changeLJSingleType(reference, atom, '{}.{}'.format(reference, prop), new_value)
    # Get the class attribute of the AmberParm object given by the string `prop`.
    # This will return a list, so index the list by the atom index of interest.
    # action = changeLJSingleType(reference, atom, getattr(reference, prop)[atom_index], new_value)
    
    action = changeLJSingleType(reference, atom, radius, epsilon)
    action.execute()
    # print(str(action))
    try:
        # Chop until the period, then cut off the [0].
        # Unclear whether [0] will be added to each property, but it is
        # currently added to LJ_radius and LJ_depth. N.B. This will depend on atom order.
        # prop_name = prop.rsplit('.', 1)[1][:-3]
        atom_name = atom[-2:]
        reference.save('parameters-{}-{}-{}.prmtop'.format(atom_name, radius, epsilon))
    except IOError:
        # The parameter file with these properties already exists, most likely.
        pass
    except:
        print('HALP')
    return 'parameters-{}-{}-{}.prmtop'.format(atom_name, radius, epsilon)


    