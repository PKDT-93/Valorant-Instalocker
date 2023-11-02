import tkinter as tk
import os
from cv_functions import Thread_instalock
from functools import partial

__MAX_COLUMNS__ = 7
__MAX_ROWS___ = 7
__AGENT_FILE_PATH__ = "./agents"

class InstalockGui:
    def __init__(self):
        """Gui Constructor"""
        # init Tk obj
        self.window = tk.Tk()
        # Set window size to 800x600
        self.window.geometry='800x600'
        # Change Window Name
        self.window.title("Select Agent to Instalock")
        self.__create_rows_columns()
        self.__create_agent_buttons()
        readme_label = tk.Label(self.window, text="Item")
        readme_label.grid(row=0, column=0, sticky='n')
        self.window.mainloop()


    def __get_agent_count(self) -> int:
        """This function returns the number of files in the agents folder as an int"""
        file_count = 0
        for agents in os.listdir(__AGENT_FILE_PATH__):
            if os.path.isfile(os.path.join(__AGENT_FILE_PATH__, agents)):
                file_count += 1
        return file_count
    

    def __create_rows_columns(self) -> None:
        """This function creates all the rows and columns the tkinter grid layout"""
        # Create Columns
        for column in range(__MAX_COLUMNS__):
            self.window.columnconfigure(column, weight=1)
        # Create Rows
        for row in range(__MAX_ROWS___):
            self.window.rowconfigure(row, weight=1)


    def __get_agent_file_names(self) -> list[str]:
        """This function returns the agent filepaths as an list of strings"""
        agent_file_paths = []

        # Get agent file path names, sort in alphabetical order and return as an array of strings
        files = os.listdir(__AGENT_FILE_PATH__)
        sorted_files = sorted(files)
        for agents in sorted_files:
            if os.path.isfile(os.path.join(__AGENT_FILE_PATH__, agents)):
                agent_file_paths.append('agents/' + agents)

        return agent_file_paths


    def __create_agent_buttons(self) -> None:
        """This function creates all of the Valorant agent buttons based on the file count of the /agents folder"""
        # Get grid size (columns, rows)
        agent_grid = self.window.grid_size() 
        agent_count = self.__get_agent_count()
        max_agent_grid_columns = agent_grid[0] - 1
        agent_file_paths = self.__get_agent_file_names()
        #Generate Buttons below readme
        current_row = 1
        current_column = 0
        # Loop through agents folder and create button based on how many agents there are
        for agent in range(agent_count):
            # Use partial to create partial button functions on-click
            command = partial(Thread_instalock, agent_file_paths[agent])
            agent_photo = tk.PhotoImage(file=agent_file_paths[agent])
            button = tk.Button(self.window, image= agent_photo, command=command)
            # Keep a reference to the image to prevent garbage collection
            button.image = agent_photo 
            button.grid(row=current_row, column=current_column, sticky="nsew")
            current_column += 1
            # Go to next row if all columns are filled
            if current_column >= max_agent_grid_columns - 1:
                current_column = 0
                current_row += 1
    

    def __change_window_title(self) -> None:
        self.window.title("Agent Selected")
        self.window.iconify()
        


