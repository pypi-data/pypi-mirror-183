class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'

class Logger:
    def __init__(self,file_path=None,should_print_to_screen=False):
        self.file_path = file_path
        self.should_print_to_screen = should_print_to_screen
        
    def empty_log(self):
        if self.file_path is None:
            return
        with open(self.file_path,'wt',encoding='utf-8') as f:
            f.write('')

    def log_colored_string(self,s,color=''):
        s = f"{color}{s}{Colors.ENDC}"
        if self.should_print_to_screen:
            print(s)
            
        if self.file_path is None:
            return #s
        with open(self.file_path,'at',encoding='utf-8') as f:
            f.write(s+'\n')
       # return s

    def green(self,s):
        self.log_colored_string(s,color=Colors.GREEN)

    def red(self,s):
        self.log_colored_string(s,color=Colors.RED)

    def yellow(self,s):
        self.log_colored_string(s,color=Colors.YELLOW)

    def cyan(self,s):
        self.log_colored_string(s,color=Colors.CYAN)

    def blue(self,s):
        self.log_colored_string(s,color=Colors.BLUE)

    def purple(self,s):
        self.log_colored_string(s,color=Colors.PURPLE)
        
    def bold(self,s):
        self.log_colored_string(s,color=Colors.BOLD)
        
    def underline(self,s):
        self.log_colored_string(s,color=Colors.UNDERLINE)