
import numpy as np

import csv
import pandas as pd
class Service():
    def __init__(self,name,rate,time,price):
        self.name = name
        self.rate = rate
        self.time = time
        self.price = price
        pass

class Invoice():
    def __init__(self):
        style = 'classic' # Determines the outpus style
        
        self.latexfile = "example.tex"
        self.title = "Invoice"
        self.num = 42
        
        self.name_rec = self.get_info()[0]
        self.adress_rec = self.get_info()[1]
        self.postcode_rec = self.get_info()[2]
        self.mail_rec = self.get_info()[3]
        
        self.name_sen = self.get_info()[4]
        self.adress_sen= self.get_info()[5]
        self.postcode_sen = self.get_info()[6]
        self.mail_sen = self.get_info()[7]
        
        self.date ="April 1, 2017"
        self.due =21

        self.items = self.get_items()
        pass
    
    
    def get_info(self):
        info = ['']*8

        df = pd.read_csv(r'Info.csv', sep=',')
        
        for i in range(0,df.values.shape[0]):
            
            if df[df.columns[0]][i] == "To":
                info[0]= df[df.columns[1]][i]
                info[1]= df[df.columns[2]][i]
                info[2]= df[df.columns[3]][i]
                info[3]= df[df.columns[4]][i]
    
            elif df[df.columns[0]][i] == "From":
                info[4]= df[df.columns[1]][i]
                info[5]= df[df.columns[2]][i]
                info[6]= df[df.columns[3]][i]
                info[7]= df[df.columns[4]][i]
            
        return info  
     
    def get_items(self):
        items = []
        df = pd.read_csv(r'Examplecsv.csv', sep=',')
        
        for i in range(0,df.values.shape[0] -1):
            # print(i)
            # print(df[df.columns[0]][i])
            items.append(Service(df[df.columns[0]][i],df[df.columns[1]][i],df[df.columns[2]][i],df[df.columns[3]][i]))
        return items
    

    
    def writeln(self,String,f):
        
        if type(String) is list:
            for st in String:
                f.writelines(st)
                f.write('\n')
        else:
            f.writelines(String)
            f.write('\n')
        
        return 
    
    
    def Start(self):
        stri = [r"\documentclass[english]{article}",r"\usepackage{invoice}",r"\begin{document}"]
        return stri

    def set_invoice_reciver(self):
        stri = [r"\setinvoicetitle{"+self.title+"}",r"\setinvoicenumber{"+f"{self.num}"+"}",r"\setreceivername{"+self.name_rec+"}",r"\setreceiveraddress{"+self.adress_rec+"}"]
        return stri

    def set_invoice_sender(self):
        stri = [r"\setname{"+self.name_sen+"}", r"\setaddress{"+f"{self.adress_sen}"+"}{"+f"{self.adress_sen}"+"}"
                ,r"\setphonenumber{"+f"{self.num}" + "}",r"\setemail{"+self.mail_sen+"}"]
        return stri

    def ref(self):
        stri = [r"\setyourref{"+self.name_rec+"}", r"\setourref{"+f"{self.adress_sen}"+"}"]
        return stri

    def dates(self,date,deadline):
        stri = [r"\setinvoicedate{"+self.date+"}", r"\setdeadline{"+f"{self.due}"+"}"]
        return stri

    def addthings(self):
        stri = []
        for i in self.items:
            stri.append(r"\additem{"+f"{i.time} hours doing {i.name}"+"}{"+f"{i.rate}"+" USD}{0}{"+f"{i.price}"+" USD}")
        return stri

    def End(self):
        stri =["\setsubtotal{650 USD}", "\setvat{0 USD}","\settotal{650 USD}","\setaccountnumber{1234 56 78910}","\makeinvoice",r"\end{document}"]
        return stri

    def makeDocument(self):
        self.writeln(self.Start(),f)
        f.write('\n')

        self.writeln(self.set_invoice_reciver(),f)
        f.write('\n')

        self.writeln(self.set_invoice_sender(),f)
        f.write('\n')

        self.writeln(self.ref(),f)
        f.write('\n')

        self.writeln(self.dates("April 1, 2017",21),f)
        f.write('\n')

        self.writeln(self.addthings(),f)
        f.write('\n')

        self.writeln(self.End(),f)
        f.write('\n')
        return
    
    
f = open("test.tex","w")

i = Invoice()

i.makeDocument()
    

# df = pd.read_csv(r'D:\Code\Latex\Invoices\simpleinvoice\Examplecsv.csv', sep=',')
# print(df.values)






