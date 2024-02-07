'''我的主页'''
import streamlit as st
from PIL import Image, ImageFilter, ImageOps


page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理工具', '智慧词典', '留言区', '解方程'])


def page_1():
    '''兴趣推荐'''
    st.title(':sunny:兴趣推荐:soccer:')
    st.header(':red[游戏推荐]：Rolling Sky')
    st.video('qianyi_RS.mp4')
    st.subheader(':red[音乐推荐]：周杰伦《本草纲目》')
    with open('qianyi_本草纲目.MP3', 'rb') as f:
        sound = f.read()
        st.audio(sound)
    st.header(':red[影片推荐]：《流浪地球2》')
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image('qianyi_WE2.jpg')
    with col2:
        pass


def page_2():
    '''图片处理工具'''
    st.title(':sunglasses:图片处理:sunglasses:')
    uploaded_file = st.file_uploader('由此上传图片(可拖拽上传)↓↓↓', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        _img = None
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['原图', '调色1', '调色2', '灰度', '模糊', '浮雕', '反色', '素描'])
        with tab1:
            st.image(img)
        with tab2:
            _img = img.copy()
            st.image(img_change(_img, 1, 2, 0))
        with tab3:
            _img = img.copy()
            st.image(img_change(_img, 2, 0, 1))
        with tab4:
            st.image(img.convert('L'))
        with tab5:
            st.image(img.filter(ImageFilter.BLUR))
        with tab6:
            st.image(img.filter(ImageFilter.EMBOSS))
        with tab7:
            st.image(ImageOps.invert(img))
        with tab8:
            st.image(img_sketch(img, 5))

    
def page_3():
    '''智慧词典'''
    st.title(':blue_book:智慧词典:blue_book:')
    with open('qianyi_words_space.txt', encoding='utf-8') as f:
        words_list = f.read().split('\n')
        
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('qianyi_check_out_times.txt', encoding='utf-8') as f:
        times_list = f.read().split('\n')

    if times_list == ['']:
        times_list = []
    
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    col1, col2 = st.columns([5, 1])
    with col1:
        word = st.text_input('请输入要查询的单词↓↓↓')
        with open('qianyi_searching.txt', encoding='utf-8') as f:
            if word != f.read():
                with open('qianyi_find.txt', 'w', encoding='utf-8'):
                    pass
    with col2:
        click_find = False
        st.write('\n')
        st.write('\n')
        if st.button('查询'):
            click_find = True
            with open('qianyi_find.txt', 'a', encoding='utf-8') as f:
                f.write('0')
    if click_find:
        if word in words_dict:
            with open('qianyi_find.txt', 'a', encoding='utf-8') as f:
                f.write('0')
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            
        else:
            if word:
                st.write('抱歉！查不到该单词。')
            with open('qianyi_find.txt', 'w', encoding='utf-8'):
                pass

    with open('qianyi_find.txt', encoding='utf-8') as f:
        find = f.read()
    if len(find) >= 2:
        with open('qianyi_searching.txt', 'w', encoding='utf-8') as f:
            f.write(word)
        n = words_dict[word][0]
        st.subheader(words_dict[word][1])
        cb = st.checkbox('显示查询次数')
        if cb:
            col3, col4 = st.columns([3, 2])
            delete = False
            with col3:
                st.write(':red[查询次数]：', times_dict[n] if n in times_dict else 0)
            with col4:
                if st.button('清空单词查询次数'):
                    if n in times_dict:
                        del times_dict[n]
                    delete = True
            if st.button('清空所有查询次数'):
                times_dict = {}
                delete = True
            if delete:
                with open('qianyi_find.txt', 'w', encoding='utf-8'):
                    pass
                st.write('删除成功')
                st.snow()
        with open('qianyi_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
            


def page_4():
    '''留言区'''
    st.title(':writing_hand:我的留言区:writing_hand:')
    
    with open('qianyi_leave_messages.txt', encoding='utf-8') as f:
        messages_list = f.read().split('\n')

    if messages_list == ['']:
        messages_list = []
    
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    messages_dict = {}
    for i in messages_list:
        messages_dict[i[0]] = i[1]

    if messages_dict:
        messages_range = []
        for i in range(int(len(messages_dict) / 10)):
            messages_range.append('第' + str(i * 10 + 1) + '~' + str((i + 1) * 10) + '条')
        if len(messages_dict) % 10 > 1:
            messages_range.append('第' + str(len(messages_dict) - len(messages_dict) % 10 + 1) + '~' + str(len(messages_dict)) + '条')
        elif len(messages_dict) % 10:
            messages_range.append('第' + str(len(messages_dict)) + '条')
            
        col1, col2 = st.columns([1, 6])
        with col1:
            st.subheader('\n')
            st.subheader('显示')
        with col2:
            show_messages = st.selectbox('', messages_range)
        show_messages = show_messages[1:-1].split('~')
        for i in range(len(show_messages)):
            show_messages[i] = int(show_messages[i])
    
        if len(show_messages) == 2:
            for i in range(show_messages[0], show_messages[1] + 1):
                with st.chat_message('💯'):
                    st.write(i, ':', messages_dict[str(i)])
        else:
            with st.chat_message('💯'):
                st.write(show_messages[0], ':', messages_dict[str(show_messages[0])])

    event = st.selectbox('', ['留言', '删除'])
    if event == '留言':    
        new_message = st.text_input('想要说的话……')
        if st.button('留言'):
            messages_dict[str(len(messages_dict) + 1)] = new_message
            with open('qianyi_leave_messages.txt', 'w', encoding='utf-8') as f:
                message = ''
                for k, v in messages_dict.items():
                    message += k + '#' + v + '\n'
                message = message[:-1]
                f.write(message)
            st.subheader('留言成功！')
            st.balloons()
            
    elif event == '删除':
        index = st.text_input('想删除的话的序号……')
        if st.button('删除'):
            if index in messages_dict:
                for i in range(int(index), len(messages_dict)):
                    messages_dict[str(i)] = messages_dict[str(i + 1)]
                del messages_dict[str(len(messages_dict))]
                with open('qianyi_leave_messages.txt', 'w', encoding='utf-8') as f:
                    message = ''
                    for k, v in messages_dict.items():
                        message += k + '#' + v + '\n'
                    message = message[:-1]
                    f.write(message)
                st.subheader('删除成功！')
                st.snow()
            else:
                st.write('抱歉！找不到该序号。')
     

def page_5():
    '''解方程'''
    translate = st.checkbox('翻译成中文/Translate into Chinese')
    st.write('翻译后将清空方程组。' if translate else 'It will clear the system of linear equations after translation.')
    st.write('It will clear the system of linear equations after translation.' if translate else '翻译后将清空方程组。')
    st.write('----')
        
    numbers = list('0123456789')    
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ''abcdefghijklmnopqrstuvwxyz')
    division = ['/']
    primary = ['+', '-']
    equal = ['=']
    space = [' ']
    terms = numbers + alphabet + division
    operators = primary + equal
    chars = terms + operators + space
    errors = {
        'E0000': '\n错误的等号数量。' if translate else '\nWrong number of equal signs.',
        'E0001': '\n未知数不在项的最后。' if translate else '\nNot followed by a space after an unknown number.',
        'E0002': '\n非法字符。' if translate else '\nIllegal characters.',
        'E0003': '\n没有未知数。' if translate else '\nNo unknowns.',
        'E0004': '\n运算符在方程最后。' if translate else '\nAn operator after the equation.',
        'E0005': '\n不为一的一项中分数线数量。' if translate else '\nWrong number of division sign in the term.',
        'E0006': '\n项中有运算符。' if translate else '\nThe term has any operators.',
        'E0007': '\n除数为0或分数线旁边不是数字。' if translate else '\nWrong character beside division sign.',
        'E0008': '\n运算符错误。' if translate else '\nOperator error.',
        'E0101': '方程的数量与未知数的数量不一致。' if translate else 'The number of equations does not equal to the number of unknowns.',
        'E0102': '系数错误。' if translate else 'Coefficient error.'
    }


    def put_spaces(equation: str, sep=None):
        if sep is None:
            sep = operators
        equation = equation.split(' ')
        text = ''
        for string in equation:
            text += string
        equation = text
        is_operator = True
        i = 0
        while i < len(equation):
            if not equation[i] in sep:
                is_operator = False
            elif not is_operator:
                is_operator = True
                equation = f'{equation[:i]} {equation[i]} {equation[i + 1:]}'
                i += 2
            i += 1
        return equation
    
    
    def prepare(translate):
        st.write('请输入一元一次方程组。' if translate else 'Please write a system of linear equations.')
        st.write('不要输入无理数。请在未知数前面输入分数。' if translate else 'Do not put irrationals. Put fractions before the unknowns.')
        st.write('不要输入小数。' if translate else 'Do not use decimals.')
        st.write('不要输入乘号和括号。' if translate else 'Do not use the multiple sign and the pair of parentheses.')
        return [], [], [], put_spaces(st.text_input('方程1：' if translate else 'Equation1:'))
    
    
    def error(code: str, empty: bool=False, errors_dict=None):
        if errors_dict is None:
            errors_dict = errors
        if code != 'E0000' or not empty:
            st.write(f'{errors_dict[code]}({code})')
        exit(1)
    
    
    def check_string(equation: str):
        if equation.count('=') != 1:
            error('E0000', equation == '')
        unknown_list = []
        is_unk = False
        for char in equation:
            if char not in chars:
                error('E0002')
            if (char != ' ') and is_unk:
                error('E0001')
            if char not in alphabet:
                is_unk = False
            else:
                unknown_list.append(char)
                is_unk = True
        if not unknown_list:
            error('E0003')
        return unknown_list
    
    
    def check_strings_between_spaces(equation: str):
        equation_list = equation.split(' ')
        if not equation_list[-1]:
            error('E0004')
        for terms_or_operators in equation_list:
            if terms_or_operators.count('/') > 1:
                error('E0005')
        return equation_list
    
    
    def check_char_beside_division(char: str, string: str):
        if char == '/' and (string.index('/') + 1 == len(string) or string[string.index('/') + 1] not in numbers[1:]
                            or not string.index('/') or string[string.index('/') - 1] not in numbers):
            error('E0007')
    
    
    def check_terms(string_term: str):
        for char in string_term:
            if char == '=':
                error('E0006')  
            else:
                check_char_beside_division(char, string_term)
    
    
    def check_first_terms(string_term: str):
        for char in string_term:
            if char not in primary:
                break
        else:
            error('E0006')
        check_terms(string_term)
    
    
    def check_signs(string_sign: str):
        if string_sign not in operators:
            error('E0008')
    
    
    def check_equation(equation_list: list):
        is_first_term = True
        is_sign = False
        for terms_or_operators in equation_list:
            if is_sign:
                check_signs(terms_or_operators)
                if terms_or_operators == '=':
                    is_first_term = True
                is_sign = False
            else:
                if is_first_term:
                    check_first_terms(terms_or_operators)
                    is_first_term = False
                else:
                    check_terms(terms_or_operators)
                is_sign = True
    
    
    def append_new(new_equation: str, new_unknowns: list, new_equ_list: list,
                   equations_list: list, unknowns_list: list, sys_equ_list: list):
        equations_list.append(new_equation)
        for unk in new_unknowns:
            unknowns_list.append(unk)
        sys_equ_list.append(new_equ_list)
    
    
    def input_equation(equation: str, equations_list: list, unknowns_list: list, sys_equ_list: list, index: int):
        unknown = check_string(equation)
        equation_list = check_strings_between_spaces(equation)
        check_equation(equation_list)
        append_new(equation, unknown, equation_list, equations_list, unknowns_list, sys_equ_list)
        return put_spaces(st.text_input(f'Equation{str(index)}:')) if index else None
    
    
    def check_number_equations_unknowns(equations_list: list, unknowns_list: list):
        unknowns_list = sorted(list(set(unknowns_list)), key=lambda letter: alphabet.index(letter))
        if len(equations_list) != len(unknowns_list):
            error('E0101')
        return unknowns_list
    
    
    def unite_terms_operators(sys_equ_list: list):
        equation_list = []
        for equation in sys_equ_list:
            terms_or_operators_list = []
            string_term = ''
            for string in equation:
                if string in operators:
                    if string == '-':
                        string_term = string
                    if string == '=':
                        terms_or_operators_list.append(string)
                else:
                    for i in range(len(string)):
                        if string[i] not in primary:
                            string_term += string[i:]
                            break
                        elif string[i] == '-':
                            string_term = '' if string_term else '-'
                    terms_or_operators_list.append(string_term)
                    string_term = ''
            equation_list.append(terms_or_operators_list)
        return equation_list.copy()
    
    
    def move_terms(sys_equ_list: list):
        equation_list = []
        for equation in sys_equ_list:
            will_move_term = [[], []]
            after_equ = False
            for string in equation:
                if string == '=':
                    after_equ = True
                else:
                    t_i_a = string[-1] in alphabet
                    if t_i_a if after_equ else (not t_i_a):
                        will_move_term[0 if after_equ else 1].append(string)
            after_equ = False
            for side in will_move_term:
                for string in side:
                    for i in range(len(equation)):
                        if equation[i] == string and int(i > equation.index('=')) + int(after_equ) == 1:
                            equation.pop(i)
                            break
                    equation.insert(int(after_equ) * len(equation), string[1:] if string[0] == '-' else '-' + string)
                after_equ = True
            equation_list.append(equation)
        return equation_list.copy()
    
    
    def factorization(num: int):
        if num == 1:
            return []
        primes = []
        for i in range(2, num + 1):
            for j in range(2, int(i ** 0.5) + 1):
                if i / j % 1 == 0:
                    break
            else:
                primes.append(i)
        factors = []
        while num not in primes:
            for prime in primes:
                if num / prime % 1 == 0:
                    num = int(num / prime)
                    factors.append(prime)
                    break
        factors.append(num)
        return factors
    
    
    def reduction(fraction: list):
        if fraction[0] == 0:
            return '0'
        plus_or_minus = int(abs(fraction[0]) * abs(fraction[1]) / fraction[0] / fraction[1])
        fraction[0] = abs(fraction[0])
        fraction[1] = abs(fraction[1])
        numerator = factorization(fraction[0])
        denominator = factorization(fraction[1])
        will_move_factor = []
        for factor_numerator in numerator:
            for factor_denominator in denominator:
                if factor_numerator == factor_denominator:
                    will_move_factor.append(factor_numerator)
                    denominator.remove(factor_denominator)
                    break
        for factor in will_move_factor:
            numerator.remove(factor)
        if len(numerator):
            while len(numerator) > 1:
                numerator.insert(0, numerator.pop(0) * numerator.pop(0))
            numerator = numerator[0]
        else:
            numerator = 1
        if len(denominator):
            while len(denominator) > 1:
                denominator.insert(0, denominator.pop(0) * denominator.pop(0))
            denominator = denominator[0]
        else:
            denominator = 1
        if denominator == 1:
            return str(numerator * plus_or_minus)
        return str(numerator * plus_or_minus) + '/' + str(denominator)
    
    
    def plus_string(num1: str, num2: str):
        num1 = num1.split('/') if ('/' in num1) else [num1, '1']
        num2 = num2.split('/') if ('/' in num2) else [num2, '1']
        return str(int(num1[0]) * int(num2[1]) + int(num1[1]) * int(num2[0])) + '/' + str(int(num1[1]) * int(num2[1]))
    
    
    def num_list(nums: list):
        plus_list = nums
        while len(plus_list) > 1:
            plus_list.insert(0, plus_string(plus_list.pop(0), plus_list.pop(0)))
        return reduction([int(plus_list[0].split('/')[0]),
                         int(plus_list[0].split('/')[1] if ('/' in plus_list[0]) else '1')])
    
    
    def unite_terms(sys_equ_list: list, unknowns_list: list):
        equation_list = []
        for equation in sys_equ_list:
            ind = equation.index('=')
            equation_left = equation[:ind]
            equation_right = equation[ind + 1:]
            will_unite_coefficient = []
            will_unite_unknown = []
            for string in equation_left:
                if string[-1] not in will_unite_unknown:
                    will_unite_unknown.append(string[-1])
                    will_unite_coefficient.append([string[:-1] + ('' if string[:-1] and string[:-1] != '-' else '1')])
                else:
                    will_unite_coefficient[will_unite_unknown.index(string[-1])].append(
                        string[:-1] + ('' if string[:-1] and string[:-1] != '-' else '1'))
            for i in range(len(will_unite_coefficient)):
                will_unite_coefficient[i] = num_list(will_unite_coefficient[i])
            equation_left = list(zip(will_unite_coefficient, will_unite_unknown))
            for unk in unknowns_list:
                if unk not in will_unite_unknown:
                    equation_left.append(('0', unk))
            equation_left = sorted(equation_left, key=lambda item: unknowns_list.index(item[1]))
            for i in range(len(equation_left)):
                equation_left[i] = equation_left[i][0]
            equation_right = num_list(equation_right) if equation_right else '0'
            equation_list.append([equation_left, equation_right])
        return equation_list.copy()
    
    
    def multiple(num1: str, num2: str):
        num1 = num1.split('/') if ('/' in num1) else [num1, '1']
        num2 = num2.split('/') if ('/' in num2) else [num2, '1']
        num = reduction([int(num1[0]) * int(num2[0]), int(num1[1]) * int(num2[1])])
        return num
    
    
    def coefficient_elimination(num1: str, num2: str):
        num1 = num1.split('/') if ('/' in num1) else [num1, '1']
        num1.reverse()
        num2 = num2.split('/') if ('/' in num2) else [num2, '1']
        num = reduction([int(num1[0]) * int(num2[0]) * -1, int(num1[1]) * int(num2[1])])
        return num
    
    
    def equality_property(equation: list, multiplier: str):
        equation_list = [[]]
        for i in range(len(equation[0])):
            equation_list[0].append(multiple(equation[0][i], multiplier))
        equation_list.append(multiple(equation[1], multiplier))
        return equation_list
    
    
    def plus_equation(equation1: list, equation2: list):
        equation = [[]]
        for i in range(len(equation1[0])):
            equation[0].append(num_list([equation1[0][i], equation2[0][i]]))
        equation.append(num_list([equation1[1], equation2[1]]))
        return equation
    
    
    def gaussian_elimination(sys_equ_list: list, unknowns_list: list):
        for i in range(len(unknowns_list) - 1):
            for j in range(i, len(unknowns_list)):
                for k in range(i, len(unknowns_list)):
                    if sys_equ_list[k][0][j] != '0':
                        break
                else:
                    error('E0102')
            for j in range(i, len(unknowns_list)):
                if sys_equ_list[j][0][i] != '0':
                    sys_equ_list.insert(i, sys_equ_list.pop(j))
                    break
            for j in range(i + 1, len(unknowns_list)):
                sys_equ_list[j] = plus_equation(sys_equ_list[j], equality_property(
                    sys_equ_list[i], coefficient_elimination(sys_equ_list[i][0][i], sys_equ_list[j][0][i])))
        return sys_equ_list
    
    
    def divided(num1: str, num2: str):
        num1 = num1.split('/') if ('/' in num1) else [num1, '1']
        num1.reverse()
        num2 = num2.split('/') if ('/' in num2) else [num2, '1']
        num = reduction([int(num1[0]) * int(num2[0]), int(num1[1]) * int(num2[1])])
        return num
    
    
    def minus_two_string(num1: str, num2: str):
        num1 = num1.split('/') if ('/' in num1) else [num1, '1']
        num2 = num2.split('/') if ('/' in num2) else [num2, '1']
        num = reduction([int(num1[0]) * int(num2[1]) - int(num1[1]) * int(num2[0]), int(num1[1]) * int(num2[1])])
        return num
    
    
    def solve_equations(sys_equ_list: list, unknowns_list: list):
        equation_list = []
        for i in range(len(unknowns_list)):
            for j in range(i):
                sys_equ_list[-i - 1][1] = minus_two_string(sys_equ_list[-i - 1][1],
                                                           multiple(sys_equ_list[-i - 1][0].pop(), equation_list[-j - 1]))
            if sys_equ_list[-i - 1][0][-1] == '0':
                error('E0102')
            else:
                equation_list.insert(0, divided(sys_equ_list[-i - 1][0][-1], sys_equ_list[-i - 1][1]))
        for i in range(len(equation_list)):
            equation_list[i] = unknowns_list[i] + ' = ' + equation_list[i]
        return equation_list.copy()
    
    
    def print_it(things: list):
        for thing in things:
            st.write(thing)
        
    
    st.title('解方程（组）' if translate else 'solve equation/ a system of equations')
    try:
        number_of_unknowns = st.slider('选择未知数的数量' if translate else 'Choose the number of unknowns.', 1, 10, 2)
        equations, unknowns, sys_equ, equ = prepare(translate)
    
        for i in range(number_of_unknowns - 1):
            equ = input_equation(equ, equations, unknowns, sys_equ, i + 2)

        input_equation(equ, equations, unknowns, sys_equ, 0)
    
        unknowns = check_number_equations_unknowns(equations, unknowns)
        
        sys_equ = unite_terms_operators(sys_equ)
    
        sys_equ = move_terms(sys_equ)
    
        sys_equ = unite_terms(sys_equ, unknowns)
    
        sys_equ = gaussian_elimination(sys_equ, unknowns)
    
        sys_equ = solve_equations(sys_equ, unknowns)
    
        print_it(sys_equ)
    except SystemExit:
        pass


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()

    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


def img_sketch(img, blur_arg):
    width, height = img.size
    img_l = img.convert('L')
    img_GB = ImageOps.invert(img_l).filter(ImageFilter.GaussianBlur(blur_arg))
    img_l_array = img_l.load()
    img_GB_array = img_GB.load()

    for x in range(width):
        for y in range(height):
            img_l_array[x, y] = min(int(img_l_array[x, y] + img_l_array[x, y] * img_GB_array[x, y] / max((255 - img_GB_array[x, y]), 1)), 255)
    return img_l


if page == '兴趣推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '智慧词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '解方程':
    page_5()
