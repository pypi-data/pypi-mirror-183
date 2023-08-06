class DefaultMessages:
    START = "Started script execution"
    END = "Finished script execution"
    

class Script:

    def __init__(self, script_name = 'unknown', logger = None, messages = None):
        self.messages = messages or DefaultMessages
        self.logger = logger 

    def add_message(self, message, type = 'info'):
        
        if (self.logger):
            if (type == 'info'):
                self.logger.info(message)
            elif (type == 'debug'):    
                self.logger.debug(message) 
            elif (type == 'warning'):    
                self.logger.warning(message)    
            elif (type == 'success'):    
                self.logger.success(message)          
            elif (type == 'error'):    
                self.logger.error(message)  
            else:
                self.logger.info(message)

        else:
            print(message)    

    def start(self):
        self.add_message(self.messages.START)
        
    def end(self):
        self.add_message(self.messages.END)