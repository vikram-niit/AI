import random
import time

class AutonomousAgent:
    def __init__(self, start_position, goal_position):
        self.position = start_position
        self.goal_position = goal_position
        self.steps_taken = 0

    def move(self):
        """The agent decides to move left, right, or stay put based on its position."""
        if self.position < self.goal_position:
            self.position += 1  # Move right towards goal
            action = "Moved right"
        elif self.position > self.goal_position:
            self.position -= 1  # Move left towards goal
            action = "Moved left"
        else:
            action = "Stayed put"  # Already at goal
        
        self.steps_taken += 1
        return action

    def act(self):
        """Agent's decision loop until it reaches the goal."""
        while self.position != self.goal_position:
            action = self.move()
            print(f"Step {self.steps_taken}: {action} | Current position: {self.position}")
            time.sleep(1)  # Slow down the output for demonstration
        
        print(f"Goal reached in {self.steps_taken} steps!")

# Initialize the agent with a starting position of 0 and a goal at position 5
agent = AutonomousAgent(start_position=0, goal_position=5)

# Run the agent's decision-making process
agent.act()
