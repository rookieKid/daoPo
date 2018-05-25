def cp(str):
    return str[0].upper()+str[1:];
def gen(name,attr):
    str = name+"PO.java";
    content="";
    with open(str,'wt') as f:
        content=content+"package PO;\n"+"public class "+ name+"PO implements java.io.Serializable {\n"+"private static final long serialVersionUID = 1L;\n";
        for key in attr:
            content = content+"private "+key+" ";
            content = content+",".join(attr[key])+";\n";
        for key in attr:
            for par in attr[key]:
                content = content+"public "+key+" get"+cp(par)+"(){\n";
                content = content+"return this."+par+";\n";
                content = content+"}\n";
                content = content+"public void set"+cp(par)+"("+key+" "+cp(par)+"){\n";
                content = content+"this."+par+" = "+cp(par)+";\n";
                content = content+"}\n";
        content = content+"}";
        f.write(content);

        

                
                
            

            
            
