#2

def func_cv(**kwargs):
    return f"Name: {kwargs['name']}, Surname: {kwargs['surname']}, E-mail: {kwargs['email']}," \
           f" birth year: {kwargs['birthyear']}, City: {kwargs['city']}"
print(func_cv(name= 'Evgenij', surname= 'Bukharkov', email= 'evgenijbukharkov@gmail.com',  birthyear= '1979',
              city= 'Dolgoprudniy'))