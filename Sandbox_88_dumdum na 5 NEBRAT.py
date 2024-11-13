import os

def main():
     
     diagonal = input("Choose the horizontal length of the board, please: ")
     
     while not diagonal.isdigit() or int(diagonal) < 3 or int(diagonal) > 26:
               diagonal = input("Length has to be a number between 3-26.\nTry again, please: ")
     diagonal = int(diagonal)
   
     vertical = input("Now choose the vertical length of the board, please: ")

     while not vertical.isdigit() or int(vertical) < 3 or int(vertical) > 26:
               vertical = input("Length has to be a number between 3-26.\nTry again, please: ")
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
      if ((coor_x+1) and (coor_x+2) and (coor_x+3) and (coor_x+4)) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif ((coor_x-1) and (coor_x-2) and (coor_x-3) and (coor_x-4)) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif ((coor_x-1) and (coor_x+1) and (coor_x+2) and (coor_x+3)) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif ((coor_x-2) and (coor_x-1) and (coor_x+1) and (coor_x+2)) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif ((coor_x-3) and (coor_x-2) and (coor_x-1) and (coor_x+1)) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      
      
      elif (coor_x+(diagonal+1)) in occupied_x and (coor_x+((diagonal+1))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x+(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x-(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x+(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x-(diagonal+2)) in occupied_x and (coor_x-((diagonal+2))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x-(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x+(diagonal)) in occupied_x and (coor_x+((diagonal))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x-(diagonal)) in occupied_x and (coor_x-((diagonal))*2) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif (coor_x-(diagonal)) in occupied_x and (coor_x+((diagonal))) in occupied_x:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      else:
            
            return mark_o(diagonal,vertical)
      
# def check_mark_x(coor_x,diagonal,vertical):
#       os.system("cls")
#       if (coor_x+1) in occupied_x and (coor_x+2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-1) in occupied_x and (coor_x-2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-1) in occupied_x and (coor_x+1) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x+(diagonal+1)) in occupied_x and (coor_x+((diagonal+1))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x+(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-(diagonal+1)) in occupied_x and (coor_x-((diagonal+1))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x+(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-(diagonal+2)) in occupied_x and (coor_x-((diagonal+2))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-(diagonal+2)) in occupied_x and (coor_x+((diagonal+2))) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x+(diagonal)) in occupied_x and (coor_x+((diagonal))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-(diagonal)) in occupied_x and (coor_x-((diagonal))*2) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       elif (coor_x-(diagonal)) in occupied_x and (coor_x+((diagonal))) in occupied_x:
#             print("".join(map(str,list(board.values()))))
#             return print(f"Player {player_x} (X) have won!")
#       else:
            
#             return mark_o(diagonal,vertical)
      
def check_mark_o(coor_o,diagonal,vertical):
      os.system("cls")
      if (coor_o+1) in occupied_o and (coor_o+2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-1) in occupied_o and (coor_o-2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-1) in occupied_o and (coor_o+1) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o+(diagonal+1)) in occupied_o and (coor_o+((diagonal+1))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o+(diagonal+1)) in occupied_o and (coor_o-((diagonal+1))) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-(diagonal+1)) in occupied_o and (coor_o-((diagonal+1))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o+(diagonal+2)) in occupied_o and (coor_o+((diagonal+2))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-(diagonal+2)) in occupied_o and (coor_o-((diagonal+2))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-(diagonal+2)) in occupied_o and (coor_o+((diagonal+2))) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o+(diagonal)) in occupied_o and (coor_o+((diagonal))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-(diagonal)) in occupied_o and (coor_o-((diagonal))*2) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif (coor_o-(diagonal)) in occupied_o and (coor_o+((diagonal))) in occupied_o:
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      else:
            
            return mark_x(diagonal,vertical)
            
os.system("cls")

board = {0:f"\n"}
occupied = []
occupied_x = []
occupied_o = []

print("Welcome to the game of PISKVORKY!\n")

player_x = input("Choose name for player X: ")
player_o = input("Choose name for player O: ")


main()

# print(occupied)







