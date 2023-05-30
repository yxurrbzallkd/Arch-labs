from .connection_to_logger import get_msgs
from .connection_to_messages import messages_get_all

def get_all_msgs():
	logger_msgs = get_msgs()
	messager_msgs = messages_get_all()
	result = "	logger:\n"+logger_msgs+"\n"
	for k in messager_msgs:
		result += "\tmessages "+str(k)+":\n"+messager_msgs[k]
	return result
