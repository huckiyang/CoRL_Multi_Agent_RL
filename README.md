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

### Workspace by Udacity 
To set up your computer to run the python code in this repository, follow the instructions below.

1. Install/Setup Python 3.6+.   See the instructions for how to do this for your operating system on the official [www.python.org](www.python.org) website.

2. [Install pip for python](https://pip.pypa.io/en/stable/installing/)

3. Install dependent python packages
    - numpy (e.g. `pip install numpy`)
    - matplotlib (see [installation instructions](https://matplotlib.org/faq/installing_faq.html))
    - pytorch: Select the correct options in the "Getting Started" section of the [pytorch main page](https://pytorch.org/), then run the command created in the "Run this command:" section of that webpage.
    - jupyter notebook: (e.g. `pip install jupyter`).  If simple pip install doesn't work see jupyter's [official documentation](http://jupyter.org/install)
    
4. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.

    - Next, install the classic control environment group by following the instructions [here](https://github.com/openai/gym#classic-control).

5. Clone this GitHub repository that contains my solution to the problem.  
    - Navigate to the folder where you want to install the repository (e.g. cd C:/bananas/)

    - `git clone https://github.com/huckiyang/Udacity_DQN_Navigation.git`

        `cd python`

        `pip install .`

6. Create an IPython kernel for the drlnd environment.

    e.g. `python -m ipykernel install --user --name drlnd --display-name "drlnd"`
