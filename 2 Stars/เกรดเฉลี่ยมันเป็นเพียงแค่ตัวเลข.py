# https://www.borntodev.com/devlab/task/14?languageId=71
i=input
t=0
def g():
    v=float(i())
    global t
    t+=v
    return v
  
print(f"THAI = {g()}\nMATH = {g()}\nENGLISH = {g()}\nSCIENCE = {g()}\nSPORT = {g()}\n---\nGPA = {t/5}")