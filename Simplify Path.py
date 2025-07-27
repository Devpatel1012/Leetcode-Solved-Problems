# class Solution(object):
#     def simplifyPath(self, path):
#         """
#         :type path: str
#         :rtype: str
#         """
#         stack = []
#         current = ""

#         for i in path+"/" :
#             if i == "/":
#                 if current == "..":
#                    if stack: stack.pop()
#                 elif current != "" and current != ".":
#                     stack.append(current)
#                 current = ""
#             else:
#                 current +=i
#         return "/"+"/".join(stack)
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
       