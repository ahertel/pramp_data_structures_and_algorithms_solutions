def isToeplitz(arr):
  # we don't have to evaluate the bottom left and top right corners
  # compare [0][0], [1,1]
  i = x = 0
  is_toeplitz = True
  #start one up from bottom left row because bottom left corner doesn't need to be evaluated
  #we'll check em all for simplicity sake
  # not to check out of index because non empty

  cols = len(arr[0])
  rows = len(arr)
  
  for c in range(cols-1, -1, -1): # from 2 to 0
    r 
    c = 0
    last_val = arr[i][x]
    r += 1
    c += 1

    while r < rows and c < cols: # 3 and 4
      print('comparing ' + str(last_val) + ' to ' + str(arr[r][c]))
      is_toeplitz = False if last_val != arr[i][x] else True
      last_val = arr[r][c]
      # move one down and across 
      r += 1
      c += 1
      print('eol: i = ' + str(r) + ", x = " + str(c))
    if c == 0:
      c += 1
  '''
  if len(arr) > 0:
    for i in range(len(arr)): # 0 to 2
      for x in range(len(arr[0])): # 0 to 3
        if arr[i][x]
    return
  '''
  return is_toeplitz

print (isToeplitz([[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]))

print( isToeplitz([[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]))