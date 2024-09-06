class Phone:
    def __init__(self,name,family,telphon,mobile_1,mobile_2,mobile_3,address,postal_code,gender):
        self.Name = name
        self.Family = family
        self.Telphon = telphon
        self.Mobile_1 = mobile_1
        self.Mobile_2 = mobile_2
        self.Mobile_3 = mobile_3
        self.Address = address
        self.postal_code = postal_code
        self.gender = gender
    def name(self):
        corect = False
        for i in range(len(self.Name)):
            if 'a' <= (self.Name[i]) <= 'z' or 'A' <= (self.Name[i]) <= 'Z' or (self.Name[i]) == ' ':
                corect = True
            else:
                corect =  False
                break
        return corect  
    def family(self):
        corect = False
        for i in range(len(self.Family)):
            if 'a' <= (self.Family[i]) <= 'z' or 'A' <= (self.Family[i]) <= 'Z' or (self.Family[i]) == ' ':
                corect = True
            else:
                corect =  False
                break
        return corect   
       
    def telphon_just_num(self):
        corect = False
        for i in range(len(self.Telphon)):
           try : 
              if  0 <= (int(self.Telphon[i])) <= 9:
                  corect = True
              else:
                  corect =  False
                  break
           except :
               corect = False
        return corect  
    def telphon_len(self):
        mode = None
        if (len(self.Telphon)) == 8 :
            mode = 1
        elif (len(self.Telphon)) == 10 :
            mode = 2
        elif (len(self.Telphon)) == 11 :
            mode = 0
        else :
            mode = 3
        return mode
        
        
    def mobile_just_num(self):
        corect = False
        try :
            for i in range(len(self.Mobile_1)):
                if  0 <= (int(self.Mobile_1[i])) <= 9 :
                    corect = True
                else:
                    corect =  False
                    break
        except :
            corect = False 
        return corect
    
    
    def mobile_1_need(self):
        if len(self.Mobile_1) == 12 :
            return 1
        elif len(self.Mobile_1) == 11 :
            return 2
        else :
            return 3
        
    def mobile_2_just_num_or_not(self):
        corect = False
        try :
            if self.Mobile_2 =="":
                corect = True
                return corect
            for i in range(len(self.Mobile_2)):
                if 0 <= (int(self.Mobile_2[i])) <= 9  :
                    corect = True
                else:
                    corect =  False
                    break
        except :
            corect =False
        return corect 
    def mobile_3_just_num_or_not(self):
        corect = False    
        try :
            if self.Mobile_3 == "":
                corect = True
                return corect
            for i in range(len(self.Mobile_3)):
                if  0 <= (int(self.Mobile_3[i])) <= 9 :
                    corect = True
                else:
                    corect =  False
                    break
        except :
            corect = False
        return corect
    
    def mobile_2_need(self):
        mood2= None
        if len(self.Mobile_2) == 12 :
            mood2 = 1
        elif len(self.Mobile_2) == 11 :
            mood2 = 2
        elif self.Mobile_2 =="":
            mood2 = 0
        else :  
            mood2 = 3
        return mood2
    def mobile_3_need(self):
        mood3 = None
        if len(self.Mobile_3) == 12 :
            mood3 = 1
        elif len(self.Mobile_3) == 11 :
            mood3 = 2
        elif self.Mobile_3 == "":
            mood3 = 0
        else :  
            mood3 = 3    
        return mood3
    def addres_check(self):
        corect = False
        for i in range(len(self.Address)):
            try:         
                if 'a' <= (self.Address[i]) <= 'z' or 'A' <= (self.Address[i]) <= 'Z' or (self.Address[i]) == ' ' or (self.Address[i]) == '-' or (self.Address[i]) == ',' or 0<= (int(self.Address[i])) <= 9:
                    corect = True
                else:
                    corect =  False
                    break
            except : 
                corect = False    
            return corect  
    def postal_code_number_check(self):
        corect = False
        try :
            for i in range(len(self.postal_code)):
                if  0 <= (int(self.postal_code[i])) <= 9 :
                    corect = True
                else:
                    corect =  False
                    break
        except :
            corect = False 
        return corect
    def postal_code_digit(self):
        if len(self.postal_code) == 10 :
            return True
        else:
            return False
    def gender_check(self):
        mood = (self.gender).lower()  
        if mood == "male" or mood =='m' :
            return 1
        elif mood == "female" or mood =='f':
            return 2
        else :
            return 3






