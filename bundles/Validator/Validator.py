class Validator:

     rules = [];

     def __init__(self, rules:list):
         rules = [ rule for rule in rules if isinstance(Rule, rule) ]