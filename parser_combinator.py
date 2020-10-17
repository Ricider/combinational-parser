parse_decimal = lambda s: (s[-1],s[:-1]) if len(s)>0 and s[-1].isnumeric() else (None,s) 

parse_char = lambda s,char: (s[-1],s[:-1]) if len(s)>0 and s[-1]==char else (None,s) 

def parse_int(s):
    out = ""
    sign=None
    while True:
        curr,s = parse_decimal(s)
        if curr==None: break
        out=curr+out
    if len(s) >= 2 and not (s[-2].isnumeric() or s[-2]==")"): sign,s=parse_char(s,"-")    
    return (("-"+out if sign else out) if out else None,s)
    
def parse_paranthesis(s):
    begp,s=parse_char(s,")")
    if begp==None: return parse_int(s)
    first,s=parse_addition(s)
    endp,s=parse_char(s,"(")   
    return (first,s)
    
def parser_template(upper_func_name,func_op,func_symbol,s):
    first,s=upper_func_name(s)
    pls_sign,s=parse_char(s,func_symbol)
    if pls_sign==None: return (first,s)
    second,s=parser_template(upper_func_name,func_op,func_symbol,s)
    
    if not second: return (first,s)
    else: return (func_op(int(second),int(first)),s)
    
apply_template = lambda upper_func_name,func_op,func_symbol: lambda s: parser_template(upper_func_name,func_op,func_symbol,s)
    
parse_multiplication=apply_template(parse_paranthesis,lambda x,y:x*y,"*")
parse_division=apply_template(parse_multiplication,lambda x,y:x//y,"/")
parse_subtraction=apply_template(parse_division,lambda x,y:x-y,"-")
parse_addition=apply_template(parse_subtraction,lambda x,y:x+y,"+")

while True: print(parse_addition(input("enter input expression: ")))
