import math


def sum_arithmetic_sequence(a_1, d, n):
    S_n = (n / 2) * ((2 * a_1) + (n - 1) * d)
    return S_n


def sum_geometric_sequence(a_1, r, n):
    if r == 1:
        S_n = a_1 * n
    else:
        S_n = (a_1 * (1 - r ** n)) / (1 - r)
    return S_n


def generate_first_order_arithmetic_sequence(a_1, d, n):
    sequence = [a_1]
    current_term = a_1
    for i in range(1, n):
        current_term = current_term + d
        sequence.append(current_term)
    return sequence


def generate_geometric_sequence(a_1, r, n):
    sequence = [a_1]
    current_term = a_1
    for i in range(1, n):
        current_term = current_term * r
        sequence.append(round(current_term, 3))
    return sequence


def sequence_type(sequence_input, a_n_term, s_n_term):
    from fractions import Fraction
    final_output_ = {}

    sequence_list = []
    for x in sequence_input:
        try:
            if '/' in x:
                L = Fraction(str(x).strip())
                sequence_list.append(float(L))
            else:
                sequence_list.append(int(str(x).strip()))
        except ValueError:
            break
    sequence = sequence_list
    differences_ = ''
    status_ = ''
    diff1 = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    if len(set(diff1)) == 1:
        differences_ = 1
        status_ = "First-order arithmetic sequence"

    diff2 = [diff1[i + 1] - diff1[i] for i in range(len(diff1) - 1)]
    if len(set(diff2)) == 1:
        differences_ = 1
        status_ = "Second-order arithmetic sequence"

    geometric = all(sequence[i + 1] / sequence[i] == sequence[1] / sequence[0] for i in range(len(sequence) - 1))
    if geometric:
        status_ = "First-order geometric sequence"

    if status_:
        n_terms = a_n_term
        if status_ == 'Second-order arithmetic sequence':
            print(status_)
            d = sequence[1] - sequence[0]
            a1 = sequence[0]
            c = sequence[2] - 2 * sequence[1] + sequence[0]
            b1 = (n_terms - 1) * d
            c1_ = (n_terms - 2) * (n_terms - 1)
            c2_ = c1_ // 2
            c_ = c2_ * c
            a_n = a1 + b1 + c_
            s_n = sum_arithmetic_sequence(a1, d, s_n_term)
            sequence_10 = generate_first_order_arithmetic_sequence(a1, d, 10)
            final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                             'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}
        elif status_ == 'First-order arithmetic sequence':
            print(status_)
            # an = a1 + (n - 1)d
            a1 = sequence[0]
            d = sequence[1] - sequence[0]
            print(d)
            d_ = (n_terms - 1) * d
            a_n = a1 + d_
            s_n = sum_arithmetic_sequence(a1, d, s_n_term)
            sequence_10 = generate_first_order_arithmetic_sequence(a1, d, 10)
            final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                             'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}
        elif status_ == 'First-order geometric sequence':
            # a_n = a_1 * r^(n-1)
            a1 = sequence[0]
            r_ = sequence[1] / sequence[0]
            n_f = r_ ** (n_terms - 1)
            a_n = a1 * n_f
            s_n = sum_geometric_sequence(a1, r_, s_n_term)
            sequence_10 = generate_geometric_sequence(a1, r_, 10)
            final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': round(r_, 4),
                             'nth_number': round(a_n, 3), 'sum_of_nth_number': round(s_n, 3),
                             "type": 'Geometric sequence'}
        else:
            final_output_ = {'sequence': "None", 'first_term': "None", 'common_difference': "None",
                             'nth_number': "None", 'sum_of_nth_number': "None",
                             "type": 'Not an arithmetic or geometric sequence'}
        return final_output_

    else:
        final_output_ = {'sequence': "None", 'first_term': "None", 'common_difference': "None", 'nth_number': "None",
                         'sum_of_nth_number': "None", "type": 'Not an arithmetic or geometric sequence'}
        return final_output_


def generat_arithmetic_sequence(data):
    a1 = data['a1']
    n = data['n']
    d_or_r = data['d_or_r']
    a_n_ = data['a_n_']
    s_n_ = data['s_n_']
    if (a1 is not None) and (n is not None) and (d_or_r is not None) and (a_n_ is None):
        a1 = a1
        d = d_or_r
        d_ = (n - 1) * d
        a_n = a1 + d_
        s_n = sum_arithmetic_sequence(a1, d, s_n_)
        sequence_10 = generate_first_order_arithmetic_sequence(a1, d, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                         'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}
    elif (a1 is None) and (n is not None) and (d_or_r is not None) and (a_n_ is not None):
        # an = a1 + (n - 1)d
        # a1=an-(n - 1)d
        d = d_or_r
        d_ = (n - 1) * d
        a_n = a_n_
        a1 = a_n - d_
        s_n = sum_arithmetic_sequence(a1, d, s_n_)
        sequence_10 = generate_first_order_arithmetic_sequence(a1, d, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                         'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}
    elif (a1 is not None) and (n is None) and (d_or_r is not None) and (a_n_ is not None):
        # an = a1 + (n - 1)d
        # (n - 1)d=an-a1 , (n - 1)=(an-a1)/d ,n=(an-a1)/d +1
        a1 = a1
        a_n = a_n_
        d = d_or_r
        sub_a=a_n-a1
        d_=sub_a // d
        n=d_+1
        print(n)

        s_n = sum_arithmetic_sequence(a1, d, s_n_)
        sequence_10 = generate_first_order_arithmetic_sequence(a1, d, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                         'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}
    elif (a1 is not None) and (n is not None) and (d_or_r is None) and (a_n_ is not None):
        # an = a1 + (n - 1)d
        # (n - 1)d=an-a1 , d=(an-a1)/(n - 1)
        a1 = a1
        a_n = a_n_
        n=n
        sub_a = a_n - a1
        sub_n=n - 1
        d=sub_a//sub_n
        s_n = sum_arithmetic_sequence(a1, d, s_n_)
        sequence_10 = generate_first_order_arithmetic_sequence(a1, d, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': d, 'nth_number': a_n,
                         'sum_of_nth_number': s_n, "type": 'Arithmetic sequence'}

    print('final_output_', final_output_)

    return final_output_


def generat_geometric_sequence(data):
    a1 = data['a1']
    n = data['n']
    d_or_r = data['d_or_r']
    a_n_ = data['a_n_']
    s_n_ = data['s_n_']
    if (a1 is not None) and (n is not None) and (d_or_r is not None) and (a_n_ is None):
        # a_n = a_1 * r^(n-1)
        a1 = a1
        r_ = d_or_r
        n_f = r_ ** (n - 1)
        a_n = a1 * n_f
        s_n = sum_geometric_sequence(a1, r_, s_n_)
        sequence_10 = generate_geometric_sequence(a1, r_, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': round(r_, 4),
                         'nth_number': round(a_n, 3), 'sum_of_nth_number': round(s_n, 3),
                         "type": 'Geometric sequence'}
    elif (a1 is None) and (n is not None) and (d_or_r is not None) and (a_n_ is not None):

         # a_n = a_1 * r^(n-1)
        r_ = d_or_r
        n=n
        a_n=a_n_
        n_f = r_ ** (n - 1)
        a1=a_n /n_f
        s_n = sum_geometric_sequence(a1, r_, s_n_)
        sequence_10 = generate_geometric_sequence(a1, r_, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': round(r_, 4),
                         'nth_number': round(a_n, 3), 'sum_of_nth_number': round(s_n, 3),
                         "type": 'Geometric sequence'}
    elif (a1 is not None) and (n is None) and (d_or_r is not None) and (a_n_ is not None):
        # a_n = a_1 * r^(n-1)
        a_n = a_n_
        a1=a1
        r_ = d_or_r
        n = math.log(a_n // a1, r_) + 1
        if str(n).__contains__('.9'):
            n=math.ceil(n)
        else:
            n=int(n)
        s_n = sum_geometric_sequence(a1, r_, s_n_)
        sequence_10 = generate_geometric_sequence(a1, r_, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': round(r_, 4),
                         'nth_number': round(a_n, 3), 'sum_of_nth_number': round(s_n, 3),
                         "type": 'Geometric sequence'}
    elif (a1 is not None) and (n is not None) and (d_or_r is None) and (a_n_ is not None):
        a_n = a_n_
        a1 = a1
        n=n
        r_ = (a_n / a1) ** (1 / (n - 1))
        s_n = sum_geometric_sequence(a1, r_, s_n_)
        sequence_10 = generate_geometric_sequence(a1, r_, n)
        final_output_ = {'sequence': sequence_10, 'first_term': a1, 'common_difference': round(r_, 4),
                         'nth_number': round(a_n, 3), 'sum_of_nth_number': round(s_n, 3),
                         "type": 'Geometric sequence'}
    return final_output_
