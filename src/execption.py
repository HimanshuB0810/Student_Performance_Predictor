import sys
import logging

def error_message_detail(error,error_detail:sys): #tb=trace_back
    _,_,exc_tb=error_detail.exc_info() #starting 2 info is not needed,3th variable gives details of on which file error has occured, which line execption occured.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number[{1}] error message [{2}]".format(
         file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
       

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

