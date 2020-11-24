import random, pdb

N=15
class MiniMaxAI:
    def __init__(self,player_one):
        self.player_one = player_one
        self.distance_Matrix = [[9999999] * N for i in range(N)]
        def distance(mat, i, j, dist):

            if i<0 or i >14 or j < 0 or j > 14:
                return
            if dist >mat[i][j]:
                return
            print(i,j,dist)
            mat[i][j] = dist
            distance(mat,i+1,j,dist+1)
            distance(mat,i,j+1,dist+1)
            distance(mat,i-1,j,dist+1)
            distance(mat,i,j-1,dist+1)
            distance(mat,i+1,j+1,dist+1)
            distance(mat,i+1,j-1,dist+1)
            distance(mat,i-1,j+1,dist+1)
            distance(mat,i-1,j-1,dist+1)
        distance(self.distance_Matrix,7,7,0)
        print(self.distance_Matrix)

    def make_move(self, game):
        return random.choice(game.get_moves())
    def evaluate(self, game):
        ret = 0
        ret += self.center_metric(game)
        #ret += self.metric2(game)
        #ret += self.metric3(game)

        return ret
    def center_metric(self,game):
        alpha = 0.95
        #sum(alpha)^
