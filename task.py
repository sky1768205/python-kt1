# python-kt1
conection=True
while conection:
     answer=input()
     if answer =="да":

      mail=str(input("Введите адрес эл. почты"+ " "))
      simbol="."
      simbol1="@"
      if simbol and simbol1 in mail:
            print("Привильный адрес эл. почты")
      elif simbol or simbol1 in mail:
            print("Нехватает символа ")
      else:
            print("Неправильно введен адрес почты")


else:
      print("Поробуйте снова")
        

