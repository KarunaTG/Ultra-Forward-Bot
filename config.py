import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "2229357")
    API_HASH = environ.get("API_HASH", "31f183a5a075fd4996cb8ad59e7b794f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7857396933:AAEYHWzqQjoyGa9lbhrmoI7dE0qheQjwUNo") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ayesha616161:Karuna@2000@cluster0.1s5zgkb.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "UltimateForwardRoBot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '794968418').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001500025641'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1001222686323") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
