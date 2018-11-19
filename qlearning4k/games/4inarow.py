__author__ = "Thiago Marafon"

import numpy as np
import re
from .game import Game


class four_in_a_row(Game):

	def __init__(self, grid_size=7):
		self.grid_size = grid_size
		self.won = False
		self.reset()

	def reset(self):
		#n = np.random.randint(0, self.grid_size-1, size=1)
		#m = np.random.randint(1, self.grid_size-2, size=1)
		#self.state = np.asarray([0, n, m])[np.newaxis]
		self.state = np.zeros((self.grid_size,self.grid_size)

	@property
	def name(self):
		return "4 in a row"

	@property
	def nb_actions(self):
		return self.grid_size

	def play(self, action):
		state = self.state
		#f0, f1, basket = state[0]
		#new_basket = min(max(1, basket + action), self.grid_size-1)
		#f0 += 1
		#out = np.asarray([f0, f1, new_basket])
		#out = out[np.newaxis]
		#assert len(out.shape) == 2
		row = self.grid_size
		while state[row][action] != 0:
		    row -= 1
		state[row][action] = 1
		self.state = state

	def get_state(self):
		#im_size = (self.grid_size,) * 2
		#state = self.state[0]
		#canvas = np.zeros(im_size)
		#canvas[state[0], state[1]] = 1
		#canvas[-1, state[2]-1:state[2] + 2] = 1
		#return canvas
		return state_to_string(self)

    def state_to_string(self):
        result = ''
        for row in self.state:
            row_to_str = np.char.mod('%d', row)
            result += ' '.join(row_to_str) + '-'
        return result

	def get_score(self):
		#fruit_row, fruit_col, basket = self.state[0]
		#if fruit_row == self.grid_size-1:
		#	if abs(fruit_col - basket) <= 1:
		#		self.won = True
		#		return 1
		#	else:
		#		return -1
		#else:
		#	return 0
		string = state_to_string(self)
        return len([m.start() for m in re.finditer('(?=11)', string)])

	def is_over(self):
	    string = state_to_string(self)
		return len([m.start() for m in re.finditer('(?=1111)', string)]) == 1

	def is_won(self):
		string = state_to_string(self)
        return len([m.start() for m in re.finditer('(?=1111)', string)]) == 1
