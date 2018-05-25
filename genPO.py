import gen1
name = input("请输入PO名字:");
print("接下来输入属性，先输入属性类型，再输入个数");
attr={};
while True:
    par = input("请输入属性类型（输入0结束）:");
    if par =="0":
        break;
    else:
        attr[par]=[];
        num = int(input("请输入该类型的变量个数："));
        for i in range(num):
            attrname = input("请输入第"+str(i+1)+"个变量名:");
            attr[par].append(attrname);
gen1.gen(name,attr);


            
