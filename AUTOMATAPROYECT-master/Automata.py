from automatalib.fa.dfa import DFA
dfa1 = DFA(
    states={'q0','q1', 'q2', 'q3','q4','q5','q6','q7','q8','q9','q10','q11',
            'q12','q13','q14','q15','q16','q17','q18','q19','q20',
            'q21','q22','q23','q24','q25','q26'},
    input_symbols={'a', 'b'},
    transitions={
        'q0':  {'a':'q1',  'b':'q2'},#
        'q1':  {'a':'q2'},#
        'q2':  {'a':'q3',  'b':'q4'},#
        'q3':  {'b':'q5'},#
        'q4':  {'a':'q5',  'b':'q16'},#
        'q5':  {'a':'q6',  'b':'q7'},#
        'q6':  {'a':'q9',  'b':'q8'},#
        'q7':  {'a':'q6',  'b':'q10'},#
        'q10': {'a':'q6',  'b':'q11'},#
        'q11': {'a':'q12', 'b':'q6'},#
        'q12': {'a':'q13', 'b':'q14'},#
        'q14': {'a':'q17', 'b':'q5'},#
        'q16': {'a':'q17', 'b':'q18'},#
        'q18': {'a':'q19', 'b':'q24'},#
        'q19': {'a':'q21', 'b':'q20'},#
        'q21': {'a':'q22', 'b':'q23'},#
        'q24': {'a':'q26', 'b':'q25'},#
        'q8':{},
        'q9':{},
        'q13':{},
        'q15':{},
        'q17':{},
        'q20':{},
        'q22':{},
        'q23':{},
        'q25':{},
        'q26':{}
        
    },
    initial_state='q0',
    final_states={'q8','q9','q13','q15','q17','q20','q22','q23','q25','q26'}
)

print (list(dfa1.validate_input('aaaba',step=True)))
    








# cantidad = int(input("¿Cuantas palabras va ingresar? = "))
# if(cantidad !=0 and cantidad >=1):
#     multiafndcheker(cantidad, nfa1)
# elif(cantidad==1):
#     entrada = str(input("Ingrese Palabra Punto 4 ER: a*ba*b(a+b)* = "))
#     print(checker2afnd(entrada, nfa1))
