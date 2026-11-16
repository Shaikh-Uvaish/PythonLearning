#Practical 2:- To implement Model-based Intelligent Agent.

# ),1 Indications:
# 0 --> Free Space to move, 1 --> Obstacle in a way.
grid = [#0 1 2
        [0,0,0],  #0
        [1,1,0],  #1
        [1,0,0]   #2
    ]

agent = [0,0]
goal = [2,2]

#To Create and Maintain the Internal State
internal_state = []

print("\nAgent Starts at: ",agent)

#Program will run only if goal is have to be achieved thus, agent is not equal to goal is given
while agent != goal:
    internal_state.append(agent.copy()) #Storing the copies of position wherever agent had moved through program to achieve goal state

    #Next step for a agent
    row = agent[0]
    col = agent[1]

    #To move Right Side:
    if col + 1 < 3 and grid[row][col + 1] == 0:
        agent[1] = agent[1] + 1

    #To move the downward position:
    elif row +1 < 3 and grid[row +1][col] == 0:
        agent[0] = agent[0] + 1

    #When Agent gets Stucked:
    else:
        print("Agent is blocked !!!!")
        break

    #Agents moving position
    print("Agent moved to:", agent)

#Finally when Goal is reached:
if agent == goal:
    print("====Goal is reached!====")

#To output the internal state of program
print("Internal State is: ", internal_state)
