import random
import numpy as np 
import copy

import logging
import torch 
from collections import namedtuple, deque
from utils import pick_device

class OUNoise_Proc():
	""" Ornstein-Uhlenbeck process """

	def __init__(self, size, mu=0.0, theta=0.15, sigma=0.2):
		""" Initialize parameters and noise process """
		self.mu = mu * np.ones(size)
		self.theta = theta 
		self.sigma = sigma 
		self.reset()

	def reset(self):
		""" Reset the internal state (= noise) to mean (mu). """
		self.state = copy.copy(self.mu)

	def sample(self):
		""" Update internal state and return it as a noise sample """
		x = self.state 
		dx = self.theta * (self.mu - x) + self.sigma * np.random.standard_normal(self.size)
		self.state = x + dx 

		return self.state

class ReplayBuffer():
	""" Fixed-size buffer to store experience tuples """

	def __init__(self, config, action_size, buffer_size, batch_size):
		""" Initialize a ReplayBuffer object """

		self.config = config 
		self.action_size = action_size
		self.memory = deque(maxlen=buffer_size)
		self.batch_size = batch_size
		self.experience = namedtuple("Experience", 
			field_names=["state", "action", "reward", "next_state", "done"])

		# logging for this class 
		self.logger = logging.getLogger(self.__class__.__name__)

		# gpu support 
		self.device = pick_device(config, self.logger)


	def add(self, state, action, reward, next_state, done):
		""" Add a new experience to memory """
		e = self.experience(state, action, reward, next_state, done)
		self.memory.append(e)


	def sample(self):
		""" Randomly sample a batch of experiences from memory """
		experiences = random.sample(self.memory, k=self.batch_size)

		states = torch.from_numpy(
			np.vstack([e.state for e in experiences if e is not None])
			).float().to(self.device)
		actions = torch.from_numpy(
			np.vstack([e.action for e in experiences if e is not None])
			).float().to(self.device)
		rewards = torch.from_numpy(
			np.vstack([e.reward for e in experiences if e is not None])
			).float().to(self.device)
		next_states = torch.from_numpy(
			np.vstack([e.next_state for e in experiences if e is not None])
			).float().to(self.device)
		dones = torch.from_numpy(
			np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)
			).float().to(self.device)

		return (states, actions, rewards, next_states, dones)


	def __len__(self):
		""" Return the current size of internal memory """
		return len(self.memory)