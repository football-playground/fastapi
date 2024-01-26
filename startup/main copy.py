list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      # 0  1  2  
list_sub = list[1:3]
print(list_sub)

lists = [list[(i*3):(i+1)*3] for i in range(5)]
print(lists)