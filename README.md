# Udacity_Multi_Agent_RL
Tennis Environment in Unity 
# Project : Collaboration and Competition 

## Description 
For this project, we train a pair of agents to play tennis.

<p align="center">
	<img src="image/unity.gif" width=60% height=60%>
</p>

## Problem Statement 
A reward of +0.1 is provided for each step that one of the two agent hits the ball over the net.
A reward of -0.01 is provided an agent lets a nall hit the ground or hits the ball out of bounds.
Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 24 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

The task is episodic. In order to solve
the environment, one of the agent must get an average score of +0.5 over 100 consecutive
episodes.

### Instructions

See the main file `Tennis.ipynb` to get an introduction to the environment and follow the steps to solving the environment. The main classes are defined in the file `MADDPG_agent.py`.

### Approach and solution

The reinforcement learning approach we use in this project is called Multi Agent Deep Deterministic Policy Gradients (MADDPG). see this [paper](https://papers.nips.cc/paper/7217-multi-agent-actor-critic-for-mixed-cooperative-competitive-environments.pdf). In this model every agent itself is modeled as a Deep Deterministic Policy Gradient (DDPG) agent (see this [paper](https://arxiv.org/pdf/1509.02971.pdf)) where, however, some information is shared between the agents.



