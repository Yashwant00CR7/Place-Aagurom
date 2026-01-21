for i in range(len(solution)):
          for j in range(len(solution[0])):
            print(solution[i][j],end=' ')
          print("\t",end=' ')
          for k in range(len(solution[0])):
            print(Backtrack.Maze.maze[i][k],end=' ')
          print()
        print('\n')