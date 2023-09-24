'''
Focus on win abbey. The only difference is we find the optimal number of past patterns to remember for learning. I found it is 5. The play style is similar to Abbey but different in story. I also do the clean up of the code.
'''

#add play order totrack the patterns of moves and their counts
def player(prev_play, opponent_history=[], play_order=[{}]):
  #we know that the first move of abbey first move is S
  if not prev_play:
    prev_play = "S"

  #keep track the opponent history
  opponent_history.append(prev_play)
  
  #save the last five moves of opponent
  last_five = "".join(opponent_history[-5:])
 

  #observing the last 5 moves
  if len(last_five) == 5:
    # increase the count in the play_order dictionary for that specific pattern
    # get method is used to retrieve the current count for last_five, if the dict is empty then get return 0.
    play_order[0][last_five] = play_order[0].get(last_five, 0) + 1
    
    last_four = "".join(opponent_history[-4:])
    #list all potential steps
    potential_plays = [last_four + move for move in "RPS"]
    #dictionary comprehension that extracts the counts of the potential next moves from the play_order dictionary, using the get method with a default value of 0 for moves that haven't occurred yet.
    sub_order = {k: play_order[0].get(k, 0) for k in potential_plays}

  #make prediction
  #If there isn't enough history for a prediction (last_five < 5), the default prediction is set to "P" (paper).
  #Make prediction by selecting the move with the highest count from sub_order. The max function with key=sub_order.get is used to find the move with the highest count. The [-1] indexing extracts the last character of the predicted move
  prediction = "P" if len(last_five) != 5 else max(sub_order, key=sub_order.get)[-1]

  return {"P": "S", "R": "P", "S": "R"}[prediction]
