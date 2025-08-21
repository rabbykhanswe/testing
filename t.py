import ast
import textwrap

class PathAnalyzer(ast.NodeVisitor):
    def _init(self):  # fixed __init_
        self.nodes = 1
        self.edges = 0
        self.decisions = 0
    
    def visit_If(self, node):
        self.decisions += 1
        self.generic_visit(node)
    
    def visit_For(self, node):
        self.decisions += 1
        self.generic_visit(node)
        
    def visit_While(self, node):
        self.decisions += 1
        self.generic_visit(node)
        
    def visit_Try(self, node):
        self.decisions += len(node.handlers)
        if node.finalbody:
            self.decisions += 1
        self.generic_visit(node)

def cyclomatic_complexity(code):
    tree = ast.parse(code)
    analyzer = PathAnalyzer()
    analyzer.visit(tree)
    complexity = analyzer.decisions + 1  # McCabe’s formula: decisions + 1
    return complexity
        
if _name_ == "_main":  # fixed __name_
    target_code = textwrap.dedent('''
        def example(x):
            if x > 0:
                print("Positive!")
            else:
                print("Not Positive!")
            
            for i in range(3):
                if i % 2 == 0:
                    print(i)
            
            return x
    ''')
    
    print("Number of Independent Paths: ", cyclomatic_complexity(target_code))
