from goody import irange, type_as_str
import math

class Rational:
    @staticmethod
    # Call as Rational._gcd(...); static, so no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    def _gcd(x : int, y : int) -> int:
        assert type(x) is int and type(y) is int and x >= 0 and y >= 0,\
          'Rational._gcd: x('+str(x)+') and y('+str(y)+') must be integers >= 0'
        while y != 0:
            x, y = y, x % y
        return x
    
    @staticmethod
    # Call as Rational._validate_arithmetic(..); static, so no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Rational or int is...
    # Rational._validate_arithmetic(right, {Rational,int},'+','Rational',type_as_str(right))
    def _validate_arithmetic(v : object, t : {type}, op : str, left_type : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+left_type+'\' and \''+right_type+'\'')        

    @staticmethod
    # Call as Rational._validate_relational(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v : object, t : {type}, op : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Rational() '+op+' '+right_type+'()') 
                   

    def __init__(self,num=0,denom=1):
        assert type(num)   is int, 'Rational.__init__ numerator is not int: '+str(num)
        assert type(denom) is int, 'Rational.__init__ denominator is not int: '+str(denom)
        assert denom != 0,'Rational.__init__ denominator is 0'
        if denom < 0:
            num, denom = -num, -denom
        if num == 0:
            denom = 1
        gcd = Rational._gcd(abs(num), denom)
        self.num = num // gcd
        self.denom = denom // gcd
        

    def __str__(self):
        return str(self.num)+'/'+str(self.denom)
   

    def __repr__(self):
        return 'Rational({},{})'.format(self.num,self.denom)
    
    def __bool__(self):
        return self.num != 0
    

    def __getitem__(self,i):
        if i == 0 or i == 1:
            return self.num if i == 0 else self.denom
         if i == '':
            raise TypeError('Fraction.__getitem: index('+str(i)+') not, 0, 1 or (non-empty) prefix')
       if 'numerator'.find(str(i).lower()) == 0:
            return self.num
        elif 'denominator'.find(str(i).lower()) == 0:
            return self.denom
        else:
            raise TypeError('Fraction.__getitem: index('+str(i)+') not, 0, 1 or (non-empty) prefix')
    
 
    def __pos__(self):
        return self
    
    
    def __neg__(self):
        return Rational(-self.num,self.denom)
    
    
    def __abs__(self):
        return Rational(abs(self.num),self.denom)
    

    def __add__(self,right):
        Rational._validate_arithmetic(right, [Rational,int],'+','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational(self.num*right.denom+right.num*self.denom,self.denom*right.denom)
    
    def __radd__(self,left):
        Rational._validate_arithmetic(left, [Rational,int],'+',type_as_str(left),'Rational')
        return self + left


    def __sub__(self,right):
        Rational._validate_arithmetic(right, [Rational,int],'-','Rational',type_as_str(right))
        return self + -right
     
    def __rsub__(self,left):
        Rational._validate_arithmetic(left, [Rational,int],'-',type_as_str(left),'Rational')
        return left + -self 
     

    def __mul__(self,right):
        Rational._validate_arithmetic(right, [Rational,int],'*','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational(self.num*right.num,self.denom*right.denom)

    def __rmul__(self,left):
        Rational._validate_arithmetic(left, [Rational,int],'*',type_as_str(left),'Rational')
        return self * left
    

    def __truediv__(self,right):
        Rational._validate_arithmetic(right, [Rational,int],'/','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational(self.num*right.denom,self.denom*right.num)
 

    def __rtruediv__(self,left):
        Rational._validate_arithmetic(left, [Rational,int],'/',type_as_str(left),'Rational')
        if type(left) is int:
            left = Rational(left)
        return left / self


    def __pow__(self,right):
        Rational._validate_arithmetic(right, [int],'**','Rational',type_as_str(right))
        if right >= 0:
            return Rational(self.num**right,self.denom**right)
        else:
            return Rational(self.denom**-right,self.num**-right)

    def __eq__(self,right):
        Rational._validate_relational(right,[Rational,int],'==',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return self.num==right.num and self.denom==right.denom
    
    def __neq__(self,right):
        Rational._validate_relational(right,[Rational,int],'!=',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return not (self == right)
    
    def __lt__(self,right):
        Rational._validate_relational(right,[Rational,int],'<',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return self.num*right.denom < right.num*self.denom
    
    def __gt__(self,right):
        Rational._validate_relational(right,[Rational,int],'>',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return right.__lt__(self)
     

    def __le__(self,right):
        Rational._validate_relational(right,[Rational,int],'<=',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return not right.__lt__(self)
     
    def __ge__(self,right):
        Rational._validate_relational(right,[Rational,int],'>=',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return not self.__lt__(right)

    
    def __call__(self, decimal_places):
        answer = ''
        num   = self.num
        denom = self.denom
    
        # handle negative values
        if num < 0:
            num, answer = -num, '-'
    
        # handle integer part
        if num >= denom:
            answer += str(num//denom)
            num     = num - num//denom*denom
            
        # handle decimal part
        return answer + '.' + '{:0>{}}'.format(num*10**decimal_places//denom,decimal_places)
    
    
    def __setattr__(self,name,value):
        if (name == 'num' or name == 'denom') and name not in self.__dict__:
            self.__dict__[name] = value
        else:
            raise NameError('Rational is immutable; attempted to change instance variable: '+name)
 
        
# e ~ 1/0! + 1/1! + 1/2! + 1/3! + ... + 1/n!
def compute_e(n):
    answer = Rational(1)
    for i in irange(1,n):
        answer += Rational(1,math.factorial(i))
    return answer

# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Rational(1,2)
    x      = Rational(1,2)
    for i in irange(1,n):
        big = 2*i+1
        answer += Rational(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer


    #Run simple tests before running driver

    x = Rational(8,29) 
    print(x+x)
    print(2*x)
    print(x(30))
    
    print()
    import driver    
    driver.default_file_name = 'bscp22S19.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
