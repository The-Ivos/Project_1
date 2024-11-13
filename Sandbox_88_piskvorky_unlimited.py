import os

def main():
     
     diagonal = input(f"Choose the horizontal length of the board, please (min {rule} / max 26): ")
     
     while not diagonal.isdigit() or int(diagonal) < rule or int(diagonal) > 26:
               diagonal = input(f"Length has to be a number between {rule}-26.\nTry again, please: ")
     diagonal = int(diagonal)
   
     vertical = input(f"Now choose the vertical length of the board, please (min {rule} / max 26): ")

     while not vertical.isdigit() or int(vertical) < rule or int(vertical) > 26:
               vertical = input(f"Length has to be a number between {rule}-26.\nTry again, please: ")
     vertical = int(vertical)
          
     return create_board(int(diagonal),int(vertical))

def create_board(diagonal,vertical):
          
     for i in range(1,((diagonal*vertical)+vertical)+1):

          board[i]= "|_"

     for i in range(1,len(board)+1):
          if i % (diagonal+1) == 0:
               board[i] = f"|\n"

     ylines = []

     for i in range(0,len(board)):
          if board[i] == "|\n":
               ylines.append(i)

     l = 0

     for i in range(0,len(board)-diagonal):
          if board[i] == "|\n" or board[i] == "\n":
               l +=1
               board[i+1] = (f"{l:2d}|_")

     alphabet = "abcdefghijklmnopqrstuvwxyz "

     header = []

     for i in range(0,diagonal):
          header.append(alphabet[i].upper())

     header = "\u0332 ".join(header + list(" "))
     board[0] = f"   {header}\n"

      
     os.system("cls")

     return mark_x(diagonal,vertical)

def mark_x(diagonal,vertical):
 
     os.system("cls")

     print("".join(map(str,list(board.values()))))

     coordinates = input(f"Player {player_x} (X), choose your coordinates: ")
     if coordinates == "vert":
           return
     
     alphabet = "abcdefghijklmnopqrstuvwxyz "

     num = ""
     alpha = ""
     digits = ""
     alphasis = ""


     for i in coordinates:
          
          if i.isdigit():
               digits += i
               num = int(digits)
               
          if len(i) == 1 and i.isalpha():
               alphasis +=i
               alpha = i

          if digits == "":
                num = 0

     while len(alphasis) != 1 or (alphabet.index(alpha.lower())+1) > diagonal or num > vertical or num < 1 or (alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))) in occupied:
           print("NOT POSSIBLE! (Place is already occupied or out of board)\nTry again, please.")
           input("\nPress any key to continue...")
           return mark_x(diagonal,vertical)
          

     if alpha.lower() == "a":
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"{num:2d}|X"))
          occupied_x.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
     else:
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"|X"))
          occupied_x.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
    
     print("".join(map(str,list(board.values()))))

     # print(occupied_x)

     coor_x = alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))

     # print("coor_x:",coor_x)
     

     return check_mark_x(coor_x,diagonal,vertical)

def mark_o(diagonal,vertical):

     os.system("cls")

     print("".join(map(str,list(board.values()))))

     coordinates = input(f"Player {player_o} (O), choose your coordinates: ")
     if coordinates == "vert":
           return
     
     alphabet = "abcdefghijklmnopqrstuvwxyz "

     num = ""
     alpha = ""
     digits = ""
     alphasis = ""


     for i in coordinates:
          
          if i.isdigit():
               digits += i
               num = int(digits)
               
          if len(i) == 1 and i.isalpha():
               alphasis +=i
               alpha = i

          if digits == "":
                num = 0

     while len(alphasis) != 1 or (alphabet.index(alpha.lower())+1) > diagonal or num > vertical or num < 1 or (alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))) in occupied:
           print("NOT POSSIBLE! (Place is already occupied or out of board)\nTry again, please.")
           input("\nPress any key to continue...")
           return mark_o(diagonal,vertical)

     if alpha.lower() == "a":
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"{num:2d}|O"))
          occupied_o.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
     else:
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"|O"))
          occupied_o.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
    
     print("".join(map(str,list(board.values()))))

     # print(occupied_o)

     coor_o = alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))

     # print("coor_o:",coor_o)
     
     return check_mark_o(coor_o,diagonal,vertical)

def check_mark_x(coor_x,diagonal,vertical):
      os.system("cls")

      diag_1 = []
      diag_2 = []

      diag_r1 = []
      diag_r2 = []

      diag_u1 = []
      diag_u2 = []

      diag_s1 = []
      diag_s2 = []

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):1])
      diag_s1 = list(board.items())[coor_x:0:-1] 
      diag_s2 = list(board.items())[coor_x:(list(board.keys())[-1]):1]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal+1])
      diag_u1 = list(board.items())[coor_x::((diagonal+1)*(-1))] 
      diag_u2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal+1)]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal])
      diag_r1 = list(board.items())[coor_x::((diagonal)*(-1))] 
      diag_r2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal)]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal+2])
      diag_1 = list(board.items())[coor_x::((diagonal+2)*(-1))] 
      diag_2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal+2)]

      # diag_1_rev = diag_1[::-1]

      # print(type(diag_r1))
      # print(type(diag_r2))

      # print(type(diag_1))
      # print(type(diag_2))
      # print(type(diag_1_rev))

      # print(diag_r1)
      # print(diag_r2)

      # print(diag_u1)
      # print(diag_u2)

      # print(diag_s1)
      # print(diag_s2)

      # print(diag_1)
      # # print(diag_1_rev)
      # print(diag_2)

      diag = list(set(diag_1).union(set(diag_2)))
      diag.sort()

      diagr = list(set(diag_r1).union(set(diag_r2)))
      diagr.sort()

      diagu = list(set(diag_u1).union(set(diag_u2)))
      diagu.sort()

      diags = list(set(diag_s1).union(set(diag_s2)))
      diags.sort()

      # print("diags:",diags)
      # print("coor_x:",coor_x)


      xline = []
      xliner = []
      xlineu = []
      xlines = []

      for i in diag:
            if "X" in i[1]:
                  xline.append("X")
            else:
                  xline.append("nope")

      for i in diagr:
            if "X" in i[1]:
                  xliner.append("X")
            else:
                  xliner.append("nope")

      for i in diagu:
            if "X" in i[1]:
                  xlineu.append("X")
            else:
                  xlineu.append("nope")

      for i in diags:
            if "X" in i[1]:
                  xlines.append("X")
            else:
                  xlines.append("nope")

      # print(xline)
      # print(xliner)
      # print(xlineu)
      # print(xlines)

      xline_check = "".join(xline)
      xliner_check = "".join(xliner)
      xlineu_check = "".join(xlineu)
      xlines_check = "".join(xlines)

      # print(xline_check)
      # print(xliner_check)
      # print(xlineu_check)
      # print(xlines_check)

      if "X"*rule in xline_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xliner_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xlineu_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xlines_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif len(occupied) == (diagonal*vertical):
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print("It's a draw!")
      else:
            
            return mark_o(diagonal,vertical)


      # input("Press...")

      # if (coor_x+1) in occupied_x and (coor_x+2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-1) in occupied_x and (coor_x-2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-1) in occupied_x and (coor_x+1) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x+(diagonal+1)) in occupied_x and (coor_x+((diagonal+1))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x+(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x+(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-(diagonal+2)) in occupied_x and (coor_x-((diagonal+2))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x+(diagonal)) in occupied_x and (coor_x+((diagonal))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-(diagonal)) in occupied_x and (coor_x-((diagonal))*2) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # elif (coor_x-(diagonal)) in occupied_x and (coor_x+((diagonal))) in occupied_x:
      #       print("".join(map(str,list(board.values()))))
      #       return print(f"Player {player_x} (X) have won!")
      # else:
            
      #       return mark_o(diagonal,vertical)

def check_mark_o(coor_o,diagonal,vertical):
      os.system("cls")

      diag_1 = []
      diag_2 = []

      diag_r1 = []
      diag_r2 = []

      diag_u1 = []
      diag_u2 = []

      diag_s1 = []
      diag_s2 = []

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):1])
      diag_s1 = list(board.items())[coor_o:0:-1] 
      diag_s2 = list(board.items())[coor_o:(list(board.keys())[-1]):1]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal+1])
      diag_u1 = list(board.items())[coor_o::((diagonal+1)*(-1))] 
      diag_u2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal+1)]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal])
      diag_r1 = list(board.items())[coor_o::((diagonal)*(-1))] 
      diag_r2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal)]

      # print(list(board.keys())[-1])
      # print(list(board)[coor_x:(list(board.keys())[-1]):diagonal+2])
      diag_1 = list(board.items())[coor_o::((diagonal+2)*(-1))] 
      diag_2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal+2)]

      # diag_1_rev = diag_1[::-1]

      # print(type(diag_r1))
      # print(type(diag_r2))

      # print(type(diag_1))
      # print(type(diag_2))
      # print(type(diag_1_rev))

      # print(diag_r1)
      # print(diag_r2)

      # print(diag_u1)
      # print(diag_u2)

      # print(diag_s1)
      # print(diag_s2)

      # print(diag_1)
      # # print(diag_1_rev)
      # print(diag_2)

      diag = list(set(diag_1).union(set(diag_2)))
      diag.sort()

      diagr = list(set(diag_r1).union(set(diag_r2)))
      diagr.sort()

      diagu = list(set(diag_u1).union(set(diag_u2)))
      diagu.sort()

      diags = list(set(diag_s1).union(set(diag_s2)))
      diags.sort()

      # print("diags:",diags)
      # print("coor_x:",coor_x)


      oline = []
      oliner = []
      olineu = []
      olines = []

      for i in diag:
            if "O" in i[1]:
                  oline.append("O")
            else:
                  oline.append("nope")

      for i in diagr:
            if "O" in i[1]:
                  oliner.append("O")
            else:
                  oliner.append("nope")

      for i in diagu:
            if "O" in i[1]:
                  olineu.append("O")
            else:
                  olineu.append("nope")

      for i in diags:
            if "O" in i[1]:
                  olines.append("O")
            else:
                  olines.append("nope")

      # print(xline)
      # print(xliner)
      # print(xlineu)
      # print(xlines)

      oline_check = "".join(oline)
      oliner_check = "".join(oliner)
      olineu_check = "".join(olineu)
      olines_check = "".join(olines)

      # print(xline_check)
      # print(xliner_check)
      # print(xlineu_check)
      # print(xlines_check)

     
      if "O"*rule in oline_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in oliner_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in olineu_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in olines_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif len(occupied) == (diagonal*vertical):
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print("It's a draw!")
      else:
            
            return mark_x(diagonal,vertical)
           
os.system("cls")

board = {0:f"\n"}
occupied = []
occupied_x = []
occupied_o = []



print("Welcome to the game of PISKVORKY UNLIMITED!\n")

player_x = input("Choose name for player X: ")
player_o = input("Choose name for player O: ")

rule = ""

while not rule.isdigit():
      rule = input("Please set the number of symbols which has to be in line to win the game: (min 3, max 9): ")

rule = int(rule)

while rule < 3 or rule > 9:
      rule = input("The number has to be between 3 and 9: ")
      while not rule.isdigit():
            rule = input("The number has to be between 3 and 9: ")
      rule = int(rule)

main()









