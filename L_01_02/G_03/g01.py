class Constant:
    def __init__(self, val):
        self.value = val
        
    def __string__(self):
        return str(self.value)

    def eval(self):
        return self.value

    def simple(self):
        return self

class Variable:
    def __init__(self, idnt, exp):
        self.id = idnt
        self.exp = exp

    def __string__(self):
        return self.id

    def eval(self):
        return self.exp.eval()

    def simple(self):
        return self.exp.simple() if isinstance(Constant) else self.exp

class Sum:
    def __init__(self, exp_1, exp_2):
        self.exp_1 = exp_1
        self.exp_2 = exp_2

    def __string__(self):
        return str(self.exp_1) + '+' + str(self.exp_2)

    def eval(self):
        return self.exp_1.eval() + self.exp_2.eval()

    def simple(self):
        eval_1 = self.exp_1.simple()
        eval_2 = self.exp_2.simple()
        if isinstance(eval_1, Constant) and eval_1 == 0:
            return eval_2
        if isinstance(eval_2, Constant) and eval_2 == 0:
            return eval_1
        return self

class Product:
    def __init__(self, exp_1, exp_2):
        self.exp_1 = exp_1
        self.exp_2 = exp_2

    def __string__(self):
        return str(self.exp_1) + '*' + str(self.exp_2)
        
    def eval(self):
        return self.exp_1.eval() * self.exp_2.eval()

    def simple(self):
        eval_1 = self.exp_1.simple()
        eval_2 = self.exp_2.simple()
        if isinstance(eval_1, Constant) and eval_1 == 1:
            return eval_2
        if isinstance(eval_2, Constant) and eval_2 == 1:
            return eval_1
        return self

