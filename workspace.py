#class Message:
 #   '''
  #  otherMessage: A string message for the entity being spoken to
   # userOptions: A list of string dialog options from which the user can choose
    #messageLinks: A list of Message objects indicating the Message that follows each userOption.
     #             The index of each item messageLinks must correspond with the index of an item in userOptions.
    #prevMessage: The message that lead to this message. 
    #'''
    #def __init__(self, otherMessage, userOptions, messageLinks=None):
     #   self.otherMessage = otherMessage 
      #  self.userOptions = userOptions 
       # self.messageLinks = messageLinks 
        #self.prevMessage = None
    

#def getNumLeading(s, char):
 #   num = 0
  #  pos = 0
   # while pos<len(s) and s[pos]==char:
    #    num+=1
     #   pos+=1
    #return num

#Construct message tree from file
#def loadMessage(fileName):
 #   fh = open(fileName)
  #  root = Message("", []) #empty root to which real root will be attached
   # lastMsg = root #previous message processed
   # prevLevel = 0 #level of message on last pass
    #for line in fh:
     #   line = line.strip()
      #  if len(line)==0:
       #     continue
        #parts = line.split(";")
        #print (parts)
        #Get other entity's message text
        #otherMsg = parts[0].strip()
        #Get array of string user responses by splitting on the '|'
        #user = [x.strip() for x in parts[1].split("|")]
        #get count of leading '.' before the other to determine position in dialog tree
        #level = getNumLeading(otherMsg, '.')
        #Create new Message to add to dialog
        #newMsg = Message(otherMsg[level:],user)

        #if level == prevLevel:
         #   newMsg.prevMessage = lastMsg.prevMessage
          #  lastMsg.prevMessage.messageLinks.append(newMsg)
            
       # elif level > prevLevel:
        #    newMsg.prevMessage = lastMsg
         #   if lastMsg.messageLinks == None:
#                lastMsg.messageLinks = [newMsg]
#            else:
#                lastMsg.messageLinks.append(newMsg)
            
#        else: #level < prevLevel
#            newMsg.prevMessage = lastMsg.prevMessage.prevMessage
#            lastMsg.prevMessage.prevMessage.messageLinks.append(newMsg)
            #If fewer links than user options in lastMsg, then need to fill
            #links with None values
#            nOpts=len(lastMsg.prevMessage.userOptions)
#            nLinks=len(lastMsg.prevMessage.messageLinks)
#            while nOpts > nLinks:
#                lastMsg.prevMessage.messageLinks.append(None)
#                nLinks+=1
            
#        lastMsg=newMsg
#        prevLevel = level
#    return root.messageLinks[0]

#Run the dialog from a root    
#def showDialog(rootMessage):
#    current = rootMessage
#    while current!=None:
#        print ("\nNPC: "+current.otherMessage)
#        choice = 1
#        for option in current.userOptions:
#            print str(choice)+". "+option
#            choice+=1

#        nextIndex = raw_input("Select an option: ")
#        if current.messageLinks==None:
#            current = current.messageLinks
#        else:
#            current = current.messageLinks[int(nextIndex)-1]
    

#data = loadMessage("convo1.dat")
#showDialog(data)


#class Dialogue:
#    maidLn1 = print("Hello sir knight")
#    maidLn2 = print("How can I be of service today?")

#Dialogue.maidLn1
#Dialogue.maidLn2






            
print("""'\033[1;32;40m\033[1;32;40mDungeon Master:\033[0;0m\033[0;0mYou walk downstairs after getting dressed and ready for the day. You remember that there was an adventurers guild
within the down. They are sure to have some work for a budding warrior such as yourself. As you step down into the main room,
you see the Inn Keeper behind the bar and Hilda near the firepit cleaning the general area. There are also a couple patrons at the tables having breakfast.
What will you do?""")
print(f"[1] Talk to the Inn Keeper\n"
      f"[2] Talk to Hilda\n"
      f"[3] Talk to the other inn patrons.\n"
      f"[4] Leave the Inn")
firstday_answ = input()

if firstday_answ == "1" :
    print("\033[1;32;40mDungeon Master:\033[0;0m You approach the Inn Keeper and say good morning.")
    print("""Inn Keeper:\033[95mHey there how did you sleep? I trust you managed to find your room okay despite the scuffle here last night.That bard is always causing some
sort of trouble. Only reason I haven't kicked him out yet is because he's actually a pretty alright guy. Heard he once Helped the local magistrate track down a doppleganger once. """)