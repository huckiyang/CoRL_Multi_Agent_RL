### Definition of Problem 
Please see the `Readme.md` session

![](https://github.com/huckiyang/Udacity_DDGD_Control/blob/master/image/actor-critic.png)

### Method 
In this project, I used Deep Determinstic Policy Gradient (DDPG) for a off-policy and model-free actor-critic algorithms. DDPG expand the Deep-Q-Network(DQN)'s accessibility on learning determinstic policy on contious place.     

### Results Discussion 

The actor-network directly outputs action which agent will take and use without any additional clipping, normalizing or preprocessing. The neural network gives an output related to its action space(=4). The hidden size parameters were chosen after careful tuning. I did experiments with 256, 512, and 1024 nodes. This tuning part of the experiment was really trickly. 

## [Solved] 512 - the environment solved at 3214 episode
![](/image/512_done.png)


The experiment got a final success at the epsidoes = 3214 with 512 nodes. It took around two hours on the working space. 
`Environment solved in 3214 episodes!	Average Score: 0.501`


## [Failed] 1024 layers - need to stop the training around 1900 episdoes, where was a crash after 2100 episodes... 
![](/image/1024_layers.png)

A classical Failure case with 1024 hidden nodes
`Episode 200	Average Score: 0.009
Episode 400	Average Score: 0.026
Episode 600	Average Score: 0.033
Episode 800	Average Score: 0.079
Episode 1000	Average Score: 0.115
Episode 1200	Average Score: 0.135
Episode 1400	Average Score: 0.137
Episode 1600	Average Score: 0.156
Episode 1800	Average Score: 0.158
Episode 2000	Average Score: 0.390
Episode 2120	Average Score: 0.085`

#### Denosie during the exploration 
![](https://github.com/huckiyang/Udacity_DDGD_Control/blob/master/image/ou_process.png)

I used ornstein uhlenbeck process during the learning processing in the continuous space. 

### Future Works
Since the tuning process of Multiple DDPG was really trciky - I spent around 8 hours on just modifying the hyper-parameters - a series of new framwork would be a good references. 

- **Multi-Agent Reinforcement Learning** -  
* [Mean Field Multi-Agent Reinforcement Learning](https://arxiv.org/pdf/1802.05438.pdf) by Yaodong Yang, Rui Luo, Minne Li, Ming Zhou, Weinan Zhang, and Jun Wang. arXiv, 2017.
* [Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/pdf/1706.02275.pdf) by Lowe R, Wu Y, Tamar A, et al. arXiv, 2017.
* [Deep Decentralized Multi-task Multi-Agent RL under Partial Observability](https://arxiv.org/pdf/1703.06182.pdf) by Omidshafiei S, Pazis J, Amato C, et al. arXiv, 2017.

- **Hyperparameter** - I focused on tuning hidden size and gradient clip which gave major improvements. A larger size could be discussed and further to be implements. 
