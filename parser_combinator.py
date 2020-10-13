parse_decimal = lambda s: (s[0],s[1:]) if len(s)>0 and s[0].isnumeric() else (None,s) 

parse_char = lambda s,char: (s[0],s[1:]) if len(s)>0 and s[0]==char else (None,s) 

def parse_int(s):
    out=""
    while True:
        curr,s = parse_decimal(s)
        if curr==None: break
        out+=curr
    return (out if out else None,s)
    
def parse_paranthesis(s):
    unmodified_s=s
    
    begp,s=parse_char(s,"(")
    if begp==None: return parse_int(unmodified_s)
    first,s=parse_addition(s)
    endp,s=parse_char(s,")")   
    
    if None in [endp,begp,first]: return parse_addition(unmodified_s)
    else: return (first,s)
    
def parser_template(upper_func_name,func_op,func_symbol,s):
    unmodified_s=s
    
    first,s=upper_func_name(s)
    pls_sign,s=parse_char(s,func_symbol)
    if pls_sign==None: return upper_func_name(unmodified_s)
    second,s=upper_func_name(s)
    
    if None in [first,pls_sign,second]:return upper_func_name(unmodified_s)
    else: return (func_op(int(first),int(second)),s)
    
apply_template = lambda upper_func_name,func_op,func_symbol: lambda s: parser_template(upper_func_name,func_op,func_symbol,s)
    
parse_multiplication=apply_template(parse_paranthesis,lambda x,y:x*y,"*")
parse_division=apply_template(parse_multiplication,lambda x,y:x//y,"/")
parse_subtraction=apply_template(parse_division,lambda x,y:x-y,"-")
parse_addition=apply_template(parse_subtraction,lambda x,y:x+y,"+")
    
def parse_expr(s):
    s=s.replace(" ","")
    while True:
        curr,s = parse_addition(s)
        if curr==None or len(s) == 0: break
        s=str(curr)+s
    return (curr,s)    

while True: print(parse_expr(input("enter input expression: ")))