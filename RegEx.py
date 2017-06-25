from enum import Enum
from collections import deque

"""
Changelog
    1.0 First Release!
    1.1 Improved expression readability
    1.2 Added compatibilty with non linear expressions
    2.0 Added Berry-Sethi Algorithm and automata PNG generation
    2.1 Added mapping to long expressions
    2.2 Added epsilon (ε)
To-do
    Add option (? or [])
    Add +
    Separate classes and methods into different files
"""
class RegExpType(Enum):
    KLEENE = 1
    CONCAT = 2
    UNION = 3
    TERMINAL = 4
    EPSILON = 5

class RegExpNode:
    charMap = {}
    sigma = set()

class BinaryNode(RegExpNode):
    def __init__(self, leftSon, rightSon):
        self.rightSon = rightSon
        self.leftSon = leftSon

class UnaryNode(RegExpNode):
    def __init__(self, son):
        self.son = son

class LeafNode(RegExpNode):
    def __init__(self, lex):
        self.lex = lex

class KleeneStar(UnaryNode):
    expType = RegExpType.KLEENE

    def __str__(self):
        if self.son.expType == RegExpType.TERMINAL: return str(self.son) + '*'
        return "(" + str(self.son) + ")*"

class Concatenation(BinaryNode):
    expType = RegExpType.CONCAT

    def __str__(self):
        return str(self.leftSon) + '.' + str(self.rightSon)

class Union(BinaryNode):
    expType = RegExpType.UNION

    def __str__(self):
        return "(" + str(self.leftSon) + "|" + str(self.rightSon) + ")"

class Terminal(LeafNode):
    expType = RegExpType.TERMINAL

    def __str__(self):
        return self.charMap[self.lex]

class Epsilon(LeafNode):
    expType = RegExpType.EPSILON

    def __init__(self):
        super().__init__('ε')

    def __str__(self):
        return 'ε'


class Digraph(tuple):
    """Class for representing Digraphs as tuples"""
    def __str__():
        st = ""
        for e in tuple(self):
            st += str(e)
        return st

def NullSet(e):
    if (e.expType == RegExpType.TERMINAL): return set()
    elif (e.expType == RegExpType.UNION): return NullSet(e.leftSon) | NullSet(e.rightSon)
    elif (e.expType == RegExpType.CONCAT): return NullSet(e.leftSon) & NullSet(e.rightSon)
    elif (e.expType == RegExpType.KLEENE): return set('ε')
    elif (e.expType == RegExpType.EPSILON): return set('ε')

def IniSet(e):
    if (e.expType == RegExpType.TERMINAL):
        tempSet = set()
        tempSet.add(str(e.charMap[e.lex])+str(e.lex))
        return tempSet
    elif (e.expType == RegExpType.UNION): return IniSet(e.leftSon) | IniSet(e.rightSon)
    elif (e.expType == RegExpType.CONCAT): return IniSet(e.leftSon) | SetConcatenation(NullSet(e.leftSon), IniSet(e.rightSon))
    elif (e.expType == RegExpType.KLEENE): return IniSet(e.son)
    elif (e.expType == RegExpType.EPSILON): return set()

def FinSet(e):
    if (e.expType == RegExpType.TERMINAL):
        tempSet = set()
        tempSet.add(str(e.charMap[e.lex])+str(e.lex))
        return tempSet
    elif (e.expType == RegExpType.UNION): return FinSet(e.leftSon) | FinSet(e.rightSon)
    elif (e.expType == RegExpType.CONCAT): return FinSet(e.rightSon) | SetConcatenation(NullSet(e.rightSon), FinSet(e.leftSon))
    elif (e.expType == RegExpType.KLEENE): return FinSet(e.son)
    elif (e.expType == RegExpType.EPSILON): return set()

def DigSet(e):
    if (e.expType == RegExpType.TERMINAL):
        return set()
    elif (e.expType == RegExpType.UNION): return DigSet(e.leftSon) | DigSet(e.rightSon)
    elif (e.expType == RegExpType.CONCAT):
        return DigSet(e.leftSon) | DigSet(e.rightSon) | SetTupleConcatenation(FinSet(e.leftSon), IniSet(e.rightSon))
    elif (e.expType == RegExpType.KLEENE):
        return DigSet(e.son) | SetTupleConcatenation(FinSet(e.son), IniSet(e.son))
    elif (e.expType == RegExpType.EPSILON):
        return set()

def SetConcatenation(a, b):
    res = set()
    for x in a:
        if x=='ε': x = ""
        for y in b:
            if y == 'ε': y = ""
            if x=="" and y == "": res.add('ε')
            else: res.add(x+y)
    return res

def SetTupleConcatenation(a, b):
    res = set()
    for x in a:
        if x == 'ε': continue
        for y in b:
            if y == 'ε': continue
            res.add(Digraph([x, y]))
    return res

def parse(expression):
    stack = []
    count = 1
    for t in expression:
        if t == '.':
            temp = stack.pop()
            stack.append(Concatenation(stack.pop(), temp))
        elif t == '|':
            temp = stack.pop()
            stack.append(Union(stack.pop(), temp))
        elif t == '*':
            stack.append(KleeneStar(stack.pop()))
        elif t == 'e' or t == 'ε':
            stack.append(Epsilon())
        else:
            terNode = Terminal(count)
            stack.append(terNode)
            terNode.charMap[count] = t
            count += 1
            terNode.sigma.add(t)
    return stack.pop()

def setToText(s):
    text = ""
    for a in sorted(s):
        text += a
    return text

class Automaton():
    def __init__(self, states, sigma, rules, initialState, finalStates):
        self.states = states
        self.sigma = sigma
        self.rules = rules
        self.initialState = initialState
        self.finalStates = finalStates

    def __str__(self):
        states = str(self.states)
        sigma = str(self.sigma)
        rules = str(self.rules)
        initialState = str(self.initialState)
        finalStates = str(self.finalStates)
        return "Q: " + states +"\nΣ: " + sigma + "\nP: " + rules + "\nI: " + initialState + "\nF: " +finalStates

    def graphvizExport(self):
        text = ""
        text += "digraph automaton {\n"
        text += "node [shape = doublecircle]; "
        for f in self.finalStates: text += setToText(f)+' '
        text += ";\n"
        text += "node [shape = circle];\n"
        for fromRule in self.rules.keys():
            tempSet1 = set(fromRule)
            for toRule in self.rules[fromRule]:
                tempSet2 = set(toRule[0])
                text += '"' + setToText(tempSet1) + '"' + " -> " + '"' + setToText(tempSet2) + '"'
                transitionLabel =  str(toRule[1]) if str(toRule[1]) not in transDict else transDict[str(toRule[1])]
                text += " [ label = " + '"' + transitionLabel + '"' + " ];\n"
        text += "}"
        return text

def berry_sethi(null, ini, fin, dig, sigma):
    #Fol Set
    fol = {}
    for connection in dig:
        f = connection[0]
        t = connection[1]
        if f not in fol:
            fol[f] = set()
        fol[f].add(t)
    for final in fin:
        if final not in fol:
            fol[final] = set()
        fol[final].add('˧')
    print("Fol: ", fol)

    #Berry-Sethi Algorithm
    q = deque()
    if null: ini.add('˧')
    q.append(ini)
    states = []
    states.append(ini)
    rules = {}
    visited = []
    while q:
        curState = frozenset(q.popleft())
        visited.append(curState)
        for b in sigma:
            nextState = set()
            for bi in curState:
                if bi[:-1] == b:
                    try:
                        nextState = nextState | fol[bi]
                    except:
                        pass
            if nextState and nextState not in visited:
                q.append(nextState)
                states.append(nextState)
            if nextState:
                if curState not in rules:
                    rules[curState] = set()
                rules[curState].add((frozenset(nextState), b))
    finals = [x for x in states if '˧' in x]
    return Automaton(states, sigma, rules, ini, finals)

#expression = parse(input("Enter input: "))
#import sys
transDict = {}
"""for line in sys.stdin.readlines():
    lhs, rhs = tuple([x.strip() for x in line.split(':')])
    print(lhs, rhs)
    transDict[lhs] = rhs"""




import sys
from antlr4 import *
from RegExpGrammarLexer import RegExpGrammarLexer
from RegExpGrammarParser import RegExpGrammarParser
from RegExpGrammarVisitor import RegExpGrammarVisitor

class RegExpGrammarPrintVisitor(RegExpGrammarVisitor):
    def __init__(self):
        super().__init__()
        self.count = 1

    def visitR0(self, ctx:RegExpGrammarParser.R0Context):
        print('In R0')
        if len(ctx.children) == 1:
            return self.visitR3(ctx.r3())
        else:
            return KleeneStar(self.visitR3(ctx.r3()))


    def visitR1(self, ctx:RegExpGrammarParser.R1Context):
        print('In R1')
        if len(ctx.children) == 1:
            return self.visitR2(ctx.r2())
        else:
            return Union(self.visitR1(ctx.r1()), self.visitR2(ctx.r2()))


    def visitR2(self, ctx:RegExpGrammarParser.R2Context):
        print('In R2')
        if len(ctx.children) == 1:
            return self.visitR0(ctx.r0())
        else:
            return Concatenation(self.visitR2(ctx.r2()), self.visitR0(ctx.r0()))


    def visitR3(self, ctx:RegExpGrammarParser.R3Context):
        print('In R3')
        if len(ctx.children) == 1:
            terNode = Terminal(self.count)
            terNode.charMap[self.count] = str(ctx.ID())
            self.count += 1
            terNode.sigma.add(str(ctx.ID()))
            return terNode
        else:
            return self.visitR1(ctx.r1())



expression = input('Type:')
istream = InputStream(expression)
lexer = RegExpGrammarLexer(istream)
stream = CommonTokenStream(lexer)
parser = RegExpGrammarParser(stream)
tree = parser.r1()
print(tree.toStringTree(recog=parser))
walker = RegExpGrammarPrintVisitor()
expression = walker.visit(tree)



print("RegExp:", expression)
null = NullSet(expression)
print('Sets:')
print("Null:", null)
ini = IniSet(expression)
print("Ini:", ini)
fin = FinSet(expression)
print("Fin:", fin)
dig = DigSet(expression)
print("Dig:", dig)
sigma = expression.sigma
print("Sigma:", sigma)
automaton = berry_sethi(null, ini, fin, dig, sigma)
print()
print('Automaton:')
print(automaton)

with open("automata.dot", encoding='utf-8', mode='w') as file:
    file.write(automaton.graphvizExport())

from subprocess import call
call(["dot", "automata.dot", "-Tpng", "-o", "image.png"])