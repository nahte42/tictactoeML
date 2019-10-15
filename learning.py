import random
import pickle

class learning:
    #Initilize learning object with weights and empty board
    def __init__(self,epsilon=0.2,alpha=0.3,gamma=0.9):
        self.epsilon=epsilon
        self.alpha=alpha
        self.gamma=gamma
        self.Q = {}
        self.last_board=None
        self.q_last=0.0
        self.state_action_last = None
        
    #Initiate game for learning
    def game_begin(self):
        self.last_board = None
        self.q_last = 0.0
        self.state_action_last = None
        
    #set board as tuple of board states
    def epsilon_greedy(self, state, possible_moves):
        self.last_board = tuple(state)
        if(random.random() < self.epsilon):#if random is less than weight epsilon move randomly, update state and last action
            move = random.choice(possible_moves)
            self.state_action_last = (self.last_board, move)
            self.q_last = self.getQ(self.last_board, move)
            return move
        else:
            Q_List = []
            for action in possible_moves:
                Q_List.append(self.getQ(self.last_board, action))
            maxQ = max(Q_List)
            
            if Q_List.count(maxQ) > 1:
                best_options = [i for i in range(len(possible_moves)) if Q_List[i]  == maxQ]
                i = random.choice(best_options)
            else:
                i = Q_List.index(maxQ)
            self.state_action_last = (self.last_board, possible_moves[i])
            self.q_last = self.getQ(self.last_board, possible_moves[i])
            return possible_moves[i]
            
    def getQ(self, state, action):
        if(self.Q.get((state,action))) is None:
            self.Q[(state, action)] = 1.0
        return self.Q.get((state,action))
        
    def updateQ(self, reward, state, possible_moves):
        q_list = []
        for moves in possible_moves:
            q_list.append(self.getQ(tuple(state), moves))
        if q_list:
            max_q_next = max(q_list)
        else:
            max_q_next = 0.0
            
        self.Q[self.state_action_last] = self.q_last + self.alpha * ((reward + self.gamma*max_q_next) - self.q_last)
        
    #wrtie Qtable to files
    def saveQtable(self, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(self.Q, handle, protocol=pickle.HIGHEST_PROTOCOL)
    #load Qtable from file
    def loadQtable(self, file_name):
        with open(file_name, 'rb') as handle:
            self.Q = pickle.load(handle)