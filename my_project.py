
import pandas as pd

class data_create():
    def __init__(self,Input):

        self.dataset = pd.read_csv(Input)
        self.Status_name = 'Status'
        self.Gender_column = 'GENDER'
        self.Age_column  = 'AGE'
        self.Income_column = 'INCOME'
        self.Region_column = 'REGION'
        self.Ethnic_column = 'ETHNICITY'
        self.Hispanic_column = 'CORE_ACCULTURATION_0001'


        #print(self.dataset)

        self.x_status = None
        self.x_gender = None
        self.x_age = None
        self.x_income = None
        self.x_region = None
        self.x_ethnic = None
        self.x_hisp= None


    def data_columns(self):
        if self.Status_name in self.dataset.columns:
            self.x_status = self.dataset[self.Status_name]
        if self.Gender_column in self.dataset.columns:
            self.x_gender = self.dataset[self.Gender_column]
        if self.Age_column in self.dataset.columns:
            self.x_age = self.dataset[self.Age_column].apply(pd.to_numeric,errors = 'coerce').fillna(-1).astype(int)
        if self.Income_column in self.dataset.columns:
            self.x_income = self.dataset[self.Income_column].astype(str)

        if self.Region_column in self.dataset.columns:
            self.x_region = self.dataset[self.Region_column]
        if self.Ethnic_column in self.dataset.columns:
            self.x_ethnic = self.dataset[self.Ethnic_column]
        if self.Hispanic_column in self.dataset.columns:
            self.x_hisp = self.dataset[self.Hispanic_column]

        # age bracket counts


        # if x_status is None or x_gender is None:
        #  print("Required columns 'Status' and 'GENDER' not found in the dataset.")
        #  return

class gender(data_create):
    def gender_data(self):

        self.data_columns()
        gender_counter_male = 0
        gender_counter_female = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]

            gender = self.x_gender.iloc[i]

            if status == 'Completed' and gender == 'Male':
                gender_counter_male += 1
            elif status == 'Completed' and gender == 'Female':
                gender_counter_female += 1

        print('Male : ', gender_counter_male)
        print('Female : ', gender_counter_female)
        print('total count is ', gender_counter_male+gender_counter_female)
        print()




class age_data(data_create):

    def age_data(self):
        self.data_columns()
        age_18_24 = 0
        age_25_34 = 0
        age_35_44 = 0
        age_45_54 = 0
        age_55_64= 0
        age_65_ = 0


        for i in range(len(self.dataset)):
            age = self.x_age.iloc[i]

            status = self.x_status.iloc[i]



            if status =='Completed':

                if age == -1:
                    continue

                if  18<= age <= 24:
                    age_18_24 +=1
                if 25 <= age <= 34:
                    age_25_34 += 1
                if 35 <= age <= 44:
                    age_35_44 += 1
                if 45 <= age <= 54:
                    age_45_54 += 1
                if 55 <= age <= 64:
                    age_55_64 += 1
                if age >= 65:
                    age_65_ += 1


        print('18-24 : ', age_18_24)
        print('25-34 :', age_25_34)
        print('35-44 : ', age_35_44)
        print('45-54 : ', age_45_54)
        print('55-64 : ', age_55_64)
        print('65+ : ', age_65_)

        print('Total age count is ',age_65_+ age_55_64+age_45_54+age_35_44+age_25_34+age_18_24)
        print()




class ethnic_data(data_create):
    '''        if self.Ethnic_column in self.dataset.columns:
                self.x_ethnic = self.dataset[self.Ethnic_column]
            if self.Hispanic_column in self.dataset.columns:
                self.x_hisp = self.dataset[self.Hispanic_column]'''

    def ethnic_data(self):
        self.data_columns()

        #ethnicVariable

        White = 0
        AA = 0
        Hispanic = 0
        Asian = 0
        Other = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            ethnic = self.x_ethnic[i]
            hispanic = self.x_hisp[i]


            if status == 'Completed':
                if hispanic == 'No' or hispanic == 'Prefer not to answer':

                    if (ethnic == 'American Indian or Alaska Native' or ethnic == 'Pacific Islander - Gaumanian'
                            or ethnic == 'Pacific Islander - Native Hawaiian' or ethnic == 'Pacific Islander - Other Pacific Islander'
                            or ethnic == 'Some other race'):

                        Other += 1

                    if (ethnic == 'Asian - Asian Indian' or ethnic == 'Asian - Chinese' or ethnic == 'Asian - Filipino'
                        or ethnic == 'Asian - Japanese' or ethnic == 'Asian - Korean'  or ethnic == 'Asian - Vietnamese'
                            or ethnic == 'Asian - Other'):

                        Asian +=1

                    if (ethnic == 'Black or African American'):
                        AA +=  1

                    if ethnic == 'White':
                        White += 1

                else:
                    Hispanic +=1


        print('White : ', White)
        print('AA : ', AA)
        print('Hispanic :', Hispanic)
        print('Asian : ', Asian)
        print('Other : ', Other)

        print('Total Ethnic count is ' ,White + AA + Asian + Hispanic + Other)
        print()


class Income(data_create):

    def income_data(self):
        self.data_columns()

        inc_25000_less = 0
        inc_25000_49000 = 0
        inc_50000_74999 = 0
        inc_75000_99999 = 0
        inc_100000_199999 = 0
        inc__200000 = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            income = self.x_income.iloc[i]

            if status == 'Completed':
                if (income == 'Less than $14,999' or income == 'Less than $5,000' or income == '$15,000 to $19,999'
                        or income == '$20,000 to $24,999'):
                    inc_25000_less += 1

                if (income == '$25,000 to $29,999' or income == '$30,000 to $34,999' or income == '$35,000 to $39,999'
                        or income == '$35,000 to $39,999' or income == '$40,000 to $44,999' or income == '$45,000 to $49,999'):
                    inc_25000_49000 += 1

                if (income == '$50,000 to $54,999' or income == '$55,000 to $59,999' or income == '$60,000 to $64,999'
                        or income == '$65,000 to $69,999' or income == '$70,000 to $74,999'):
                    inc_50000_74999 += 1

                if (income == '$75,000 to $79,999' or income == '$80,000 to $84,999' or income == '$85,000 to $89,999'
                        or income == '$90,000 to $94,999' or income == '$95,000 to $99,999'):
                    inc_75000_99999 += 1

                if (
                        income == '$100,000 to $124,999' or income == '$125,000 to $149,999' or income == '$150,000 to $174,999'
                        or income == '$175,000 to $199,999'):
                    inc_100000_199999 += 1

                if (income == '$200,000 to $249,999' or income == '$250,000 and above'):
                    inc__200000 += 1

        print('inc_25000_less : ',  inc_25000_less)
        print('inc_25000_49000 : ',inc_25000_49000)
        print('inc_50000_74999 : ', inc_50000_74999 )
        print('inc_75000_99999 : ', inc_75000_99999 )
        print('inc_100000_199999 : ', inc_100000_199999  )
        print('inc__200000 : ', inc__200000)
        total = (inc_25000_less + inc_25000_49000 + inc_50000_74999+ inc_75000_99999+ inc_100000_199999 + inc__200000)
        print('Total income count is ',total )
        print()



class region(data_create):

    def region_data(self):
        self.data_columns()

        West = 0
        Midwest = 0
        South = 0
        Northeast = 0

        for i in range(len(self.dataset)):
            status = self.x_status.iloc[i]
            region = self.x_region.iloc[i]

            if status == 'Completed':
                if region == 'South':
                    South +=1
                if region == 'Midwest':
                    Midwest +=1
                if region == 'West':
                    West +=1
                if region == 'Northeast':
                    Northeast +=1

        print('Northeast : ', Northeast)
        print('Midwest : ', Midwest)
        print('South : ', South)
        print('West : ', West)
        print('Total region counts ', Northeast+Midwest+South+West)




Input = r"C:\Users\prabi\Downloads\Main__Question_Report_Job_1717766797636.csv"




gender = gender(Input)
gender.gender_data()

age = age_data(Input)
age.age_data()

ethnic = ethnic_data(Input)
ethnic.ethnic_data()


Income = Income(Input)
Income.income_data()


Region = region(Input)
Region.region_data()











