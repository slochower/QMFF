from parmed.tools import changeLJSingleType

def manipulate_lj(reference, atom, prop, new_value):
    '''
    Write out a new parameter file with `parameter` set to `value`.
    The `parameter` must be in the form `parmed` can understand.
    The `reference` set must be a `parmed` object.
    '''
    # action = changeLJSingleType(reference, atom, '{}.{}'.format(reference, prop), new_value)
    action = changeLJSingleType(reference, atom, reference.LJ_radius[0], new_value)
    action.execute()
    try:
        # Chop until the period, then cut off the [0].
        # Unclear whether [0] will be added to each property, but it is
        # currently added to LJ_radius and LJ_depth. N.B. This will depend on atom order.
        # prop_name = prop.rsplit('.', 1)[1][:-3]
        prop_name = 'LJ_radius'
        atom_name = atom[-2:]
        reference.save('parameters-{}-{}-{}.prmtop'.format(atom_name, prop_name, new_value))
    except IOError:
        # The parameter file with these properties already exists, most likely.
        pass
    except:
        print('HALP')
    return 'parameters-{}-{}-{}.prmtop'.format(atom_name, prop_name, new_value)


    