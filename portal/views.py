import gc
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
    Response, jsonify
from portal.application.sequence import sequence_type, generat_arithmetic_sequence, generat_geometric_sequence
from portal.application.matrix_operations import matrix_arithmetic, matrix_arithmetic_operations, get_matrix, \
    get_ones_zeros_eye,get_transpose_inv_det,get_Diagonal_Trace_Size
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

bp = Blueprint('view', __name__, url_prefix='/uncg_math', template_folder="./templates", static_folder="./static")


@bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")


@bp.route('/sequences', methods=["GET", "POST"])
def sequences():
    if request.method == "GET":
        return render_template("sequences.html")
    if request.method == "POST":
        data = request.json
        type = data["type"]
        if type == 'a_or_g_output':
            arith_or_geo = data["arith_or_geo_input"]
            a_n_term = data["a_n_term"]
            finl_out = sequence_type(arith_or_geo, a_n_term, a_n_term)
            print(finl_out)
            return finl_out
        elif type == 'Arithmetic Sequence':
            print('Geometric', data)
            final_output_ = generat_arithmetic_sequence(data)
            return final_output_
        elif type == 'Geometric Sequence':
            final_output_ = generat_geometric_sequence(data)
            return final_output_
        Status = {"status": 'as,mna,sn,s'}
        return jsonify(Status)


@bp.route('/matrix_operation', methods=["GET", "POST"])
def matrix_operation():
    if request.method == "GET":
        return render_template("matrix_operation.html")
    if request.method == "POST":
        data = request.json
        temp_matrix_a = str(data['matrix_expression_1_input']).replace('{', '').replace('}', '').split(';')
        temp_matrix_b = data['matrix_expression_2_input'].replace('{', '').replace('}', '').split(';')
        operation_ = data['Matrix_Action']
        matrix_a = get_matrix(temp_matrix_a)
        matrix_b = get_matrix(temp_matrix_b)
        check_list_ = matrix_arithmetic(matrix_a, matrix_b)
        if check_list_['OutPut'] == 'Successful':
            result_ = matrix_arithmetic_operations(matrix_a, matrix_b, operation_)
            str_final_=get_final_out(result_, "matrix_operation")
            str_final_ = str_final_ + '}'
            return {'result_': str(str_final_), 'status': str(check_list_['OutPut'])}
        else:
            return {'result_': 'None', 'status': str(check_list_['OutPut'])}


def get_final_out(result_, action):
    print('result_',result_)
    len_ = 0
    str_final_ = ''
    if action == 'matrix_matlab_operation':
        result_ = result_.astype(int)
    for i in result_.tolist():
        temp_ = str(i).replace('[', '').replace(']', "")
        if len_ == 0:
            str_final_ = '{' + str(temp_)
        else:
            str_final_ = str(str_final_) + ';' + str(temp_)
        len_ += 1
    return str_final_


@bp.route('/matrix_matlab_operation', methods=["GET", "POST"])
def matrix_matlab_operation():
    if request.method == "POST":
        data = request.json
        result_ = ''
        if data['type'] == "Zeros" or data['type'] == "Ones":
            if str(data['matrix_matlab_Expression']).__contains__(','):
                temp_matrix_a = str(data['matrix_matlab_Expression']).replace('(', '').replace(')', '').split(',')
                final_ = []
                for num in temp_matrix_a:
                    if num.isdigit() and int(num) == 0:
                        return {'result_': "Size cannot be zero.", 'status': "Failed"}
                    elif num.isdigit():
                        final_.append(int(num))
                    else:
                        return {'result_': "Size cannot be string.", 'status': "Failed"}
                result_ = get_ones_zeros_eye(tuple(final_), data['type'])
            else:
                return {'result_': "Please check entered expression", 'status': "Failed"}
        elif data['type'] == "Eyes":
            temp_matrix_a = str(data['matrix_matlab_Expression'])
            if temp_matrix_a.isdigit() and int(temp_matrix_a) == 0:
                return {'result_': "Size cannot be zero.", 'status': "Failed"}
            elif temp_matrix_a.isdigit():
                temp_matrix_a = int(temp_matrix_a)
            else:
                return {'result_': "Size cannot be string.", 'status': "Failed"}
            result_ = get_ones_zeros_eye(temp_matrix_a, data['type'])
        elif data['type'] == "Det" or data['type'] == "Inverse" or data['type'] == "Transpose":
            if str(data['matrix_matlab_Expression']).__contains__(';'):
                temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
                matrix_a = get_matrix(temp_matrix_a)
                result_=get_transpose_inv_det(matrix_a,data['type'])

                if data['type'] == "Det":
                    return {'result_': float(result_), 'status': "Successful"}
            else:
                return {'result_': "Please check entered expression", 'status': "Failed"}
        elif data['type'] == "Diagonal" or data['type'] == "Size" or data['type'] == "Trace":
            if str(data['matrix_matlab_Expression']).__contains__(';'):
                temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
                matrix_a = get_matrix(temp_matrix_a)
                result_=get_Diagonal_Trace_Size(matrix_a,data['type'])
                if data['type'] == "Size":
                    return {'result_': tuple(result_), 'status': "Successful"}
                elif data['type'] == "Trace":
                    return {'result_': float(result_), 'status': "Successful"}

        if result_ == 'The matrix is singular':
            return {'result_': "The matrix is singular", 'status': "Failed"}
        elif result_ == 'The matrix is not square':
            return {'result_': "The matrix is not square", 'status': "Failed"}
        elif result_ == 'Please check matrix expression':
            return {'result_': "Please check matrix expression", 'status': "Failed"}
        if data['type'] == "Zeros" or data['type'] == "Ones" or data['type'] == "Eyes":
            str_final_ = get_final_out(result_, "matrix_matlab_operation")
        else:
            str_final_ = get_final_out(result_, "matrix_matlab_operation1")
        if str_final_:
            str_final_ = str_final_ + '}'
            return {'result_': str_final_, 'status': "Successful"}
        else:
            return {'result_': "Please check entered expression", 'status': "Failed"}
