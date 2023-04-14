def validParanthesis(s):
      stack = []
      pair = {'(' : ')' , '[' : ']' , '{' : '}'}
      for i in s :
           if (i =='(' or i == '[' or i == '{'):
               stack.append(i)
           if (i == ')' or i == ']' or i == '}'):
               if not stack :
                   return False
               elif  i != pair[stack.pop()] :
                   return False
               else :
                   continue
      if not stack :
           return True
      else :
           return False

        
sequence = '([})]'
if(validParanthesis(sequence)):
    print("paranthesis are valid")
else:
    print("paranthesis are not valid")
