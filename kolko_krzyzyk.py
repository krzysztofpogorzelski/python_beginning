l=[[ " * "," * "," * "],[ " * "," * "," * "],[" * "," * "," * "]]

print(f"{l[0][0]} | {l[0][1]} | {l[0][2]}\n----|-----|-----"
      f"\n{l[1][0]} | {l[1][1]} | {l[1][2]}\n----|-----|-----"
      f"\n{l[2][0]} | {l[2][1]} | {l[2][2]}")

i=0
while True:
      try:
            if i%2==0:
                  x= input(f"\nGracz X, podaj numer pola: ")
                  x_list = list(x)
                  if (l[int(x_list[0])][int(x_list[1])]==" X " or l[int(x_list[0])][int(x_list[1])])==" O ":
                        pass
                  else:
                        l[int(x_list[0])][int(x_list[1])] = " X "
                  i+=1
            elif i%2==1:
                  x = input(f"\nGracz O, podaj numer pola: ")
                  x_list = list(x)
                  if (l[int(x_list[0])][int(x_list[1])]) == " X " or  (l[int(x_list[0])][int(x_list[1])]) == " O ":
                        pass
                  else:
                        l[int(x_list[0])][int(x_list[1])] = " O "
                  i+=1
            print(f"{l[0][0]} | {l[0][1]} | {l[0][2]}\n----|-----|-----"
                  f"\n{l[1][0]} | {l[1][1]} | {l[1][2]}\n----|-----|-----"
                  f"\n{l[2][0]} | {l[2][1]} | {l[2][2]}")

            if ((l[0][0] == " X " and l[0][1] == " X " and l[0][2] == " X ") or
                  (l[1][0] == " X " and l[1][1] == " X " and l[1][2] == " X ") or
                  (l[2][0] == " X " and l[2][1] == " X " and l[2][2] == " X ") or
                  (l[0][0] == " X " and l[1][0] == " X " and l[2][0] == " X ") or
                  (l[0][1] == " X " and l[1][1] == " X " and l[2][1] == " X ") or
                  (l[0][2] == " X " and l[1][2] == " X " and l[2][2] == " X ") or
                  (l[0][0] == " X " and l[1][1] == " X " and l[2][2] == " X ") or
                  (l[0][2] == " X " and l[1][1] == " X " and l[2][0] == " X ")):
                  print("======= WYGRAŁES X =======")
                  exit()

            elif ((l[0][0] == " O " and l[0][1] == " O " and l[0][2] == " O ") or
                  (l[1][0] == " O " and l[1][1] == " O " and l[1][2] == " O ") or
                  (l[2][0] == " O " and l[2][1] == " O " and l[2][2] == " O ") or
                  (l[0][0] == " O " and l[1][0] == " O " and l[2][0] == " O ") or
                  (l[0][1] == " O " and l[1][1] == " O " and l[2][1] == " O ") or
                  (l[0][2] == " O " and l[1][2] == " O " and l[2][2] == " O ") or
                  (l[0][0] == " O " and l[1][1] == " O " and l[2][2] == " O ") or
                  (l[0][2] == " O " and l[1][1] == " O " and l[2][0] == " O ")):
                  print("======= WYGRAŁES O =======")
                  exit()
            elif (l[0][0] != " * " and l[0][1] != " * " and l[0][2] != " * " and
                  l[1][0] != " * " and l[1][1] != " * " and l[1][2] != " * " and
                  l[2][0] != " * " and l[2][1] != " * " and l[2][2] != " * "):

                  print("======= REMIS =======")
                  exit()
      except ValueError:
            print("podaj miejsce jako dwie cyfry będące namiarymi (xy) pola gdzie chcesz wstawić swój znak  ")

