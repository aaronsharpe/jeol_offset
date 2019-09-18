"""
Functions for calculating the offset for a JEOL write
"""


def compute_offset():
    """
    Prompts the user to input various coordinates and returns the calculated
    offset

    Arguments:
        letters_in: the letters of the alignement mark
        origin_xy: the origin of the pattern relative to the AA mark
        stage_xy: current position of the JEOL stage
    """
    print('JEOL offset calculator')

    letters_in = input('Enter letters (top then bottom): ')
    origin_xy = input('Pattern origin relative to AA (x,y): ')
    stage_xy = input('Current stage position (x,y): ')

    x_chip, y_chip = letter_to_dist(letters_in)

    x_origin, y_origin = number_list_parse(origin_xy)
    x_stage, y_stage = number_list_parse(stage_xy)

    x_offset = x_origin - x_chip + x_stage
    y_offset = y_origin - y_chip + y_stage
    print(f'Offset: {x_offset:.3f},{y_offset:.3f}')
    return x_offset, y_offset


def letter_to_dist(letters_in):
    """
    Takes the letters of a given alignment mark and returns their coordinates

    Arguments:
        letters_in
    """
    if len(letters_in) != 2:
        raise ValueError('needs to be 2 letters')

    grid_vals = range(0, 5001, 500)
    letters = 'ACEGIKMOQS'

    y_let, x_let = letters_in
    if x_let not in letters or y_let not in letters:
        raise ValueError('incorrect letter')

    x = grid_vals[letters.find(x_let)]
    y = grid_vals[letters.find(y_let)]
    return x, y


def number_list_parse(str_in):
    """
    Takes a string of two numbers separated by a comma and returns the two
    numbers

    Arguments:
        str_in: string of two numbers separated by a comma
    """
    x, y = str_in.split(',')
    return float(x), float(y)
