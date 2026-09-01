class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                b,a=stack.pop(),stack.pop()
                stack.append(a-b)
            elif c=="*":
                stack.append(stack.pop() * stack.pop())
            elif c=="/":
                b,a=stack.pop(),stack.pop()
                if b==0:
                    return -1
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[0]