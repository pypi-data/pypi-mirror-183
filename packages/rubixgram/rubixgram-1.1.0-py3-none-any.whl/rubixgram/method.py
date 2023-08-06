import datetime
from rubixgram.encode import welcome , web , android , encoderjson , encoder_photo
import json
from json import dumps, loads
import random
from random import randint, choice
from requests import (post, get)
import urllib
from urllib import request
from pathlib import Path
from rubixgram.sendserver import (send_server_rubika)
from re import findall
from tinytag import TinyTag
from rubixgram.PostData import (http,httpfiles)
import asyncio
from asyncio import (run)

get_url = lambda url_number: f"https://messengerg2c{url_number}.iranlms.ir/"
 
class Client:
    ser_full = send_server_rubika()
    server_Message = ser_full.server_full()
    ser_file = send_server_rubika()
    server_files = ser_file.server_full()
    
    def __init__(self, Sh_account: str):
        self.Auth = str("".join(findall(r"\w",Sh_account)))
        self.enc = encoderjson(Sh_account)
        self.print = welcome
        
        if self.Auth.__len__() < 32:
        	print("Your AUTH is incorrec .")
        else:
            if self.Auth.__len__() > 32:
            	print("Your AUTH is incorrec .")
            	
    def excute(self, method):
        while 1:
            try:
                loop = asyncio.get_event_loop()
                requests = self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_Message,self.Auth,method))).get("data_enc"))
                return loads(requests)
                break
            except: continue
			
    def sendMessage(self, chat_id,text,metadata=[],message_id=None):
        method = {
            "method":"sendMessage",
            "input":{
                "object_guid":chat_id,
                "rnd":f"{randint(100000,999999999)}",
                "text":text,
                "reply_to_message_id":message_id
            },
            "client": web
        }
        if metadata != [] : method["input"]["metadata"] = {"meta_data_parts":metadata}
        return self.excute(method)
        
        
    def editMessage(self, gap_guid, newText, message_id):
        method = {
            "method":"editMessage",
            "input":{
                "message_id":message_id,
                "object_guid":gap_guid,
                "text":newText
            },
            "client": web
        }
        return self.excute(method)
        

    def deleteMessages(self, chat_id, message_ids):
        method = {
            "method":"deleteMessages",
            "input":{
                "object_guid":chat_id,
                "message_ids":message_ids,
                "type":"Global"
            },
            "client": web
        }
        return self.excute(method)
                

    def getMessagefilter(self, chat_id, filter_whith):
        method = {
            "method":"getMessages",
            "input":{
                "filter_type":filter_whith,
                "max_id":"NaN",
                "object_guid":chat_id,
                "sort":"FromMax"
            },
            "client": web
        }
        return self.excute(method).get("data").get("messages")
        

    def getMessages(self, chat_id, min_id):
        method = {
            "method":"getMessagesInterval",
            "input":{
                "object_guid":chat_id,
                "middle_message_id":min_id
            },
            "client": web
        }
        return self.excute(method).get("data").get("messages")
        

    def getChats(self, start_id=None):
        method = {
            "method":"getChats",
            "input":{
                "start_id":start_id
            },
            "client": web
        }
        return self.excute(method).get("data").get("chats")
        

    def deleteUserChat(self, user_guid, last_message):
        method = {
            "method":"deleteUserChat",
            "input":{
                "last_deleted_message_id":last_message,
                "user_guid":user_guid
            },
            "client": web
        }
        return self.excute(method)
        

    def getInfoByUsername(self, username):
        method = {
            "method":"getObjectByUsername",
            "input":{
                "username":username
            },
            "client": web
        }
        return self.excute(method)
        

    def banGroupMember(self, chat_id, user_id):
        method = {
            "method":"banGroupMember",
            "input":{
                "group_guid": chat_id,
                "member_guid": user_id,
                "action":"Set"
            },
            "client": web
        }
        return self.excute(method)
        

    def unbanGroupMember(self, chat_id, user_id):
        method = {
            "method":"banGroupMember",
            "input":{
                "group_guid": chat_id,
                "member_guid": user_id,
                "action":"Unset"
            },
            "client": android
        }
        return self.excute(method)
        

    def getGroupInfo(self, chat_id):
        method = {
            "method":"getGroupInfo",
            "input":{
                "group_guid": chat_id
            },
            "client": web
        }
        return self.excute(method)
        

    def invite(self, chat_id, user_ids):
        method = {
            "method":"addGroupMembers",
            "input":{
                "group_guid": chat_id,
                "member_guids": user_ids
            },
            "client": web
        }
        return self.excute(method)
        

    def inviteChannel(self, chat_id, user_ids):
        method = {
            "method":"addChannelMembers",
            "input":{
                "channel_guid": chat_id,
                "member_guids": user_ids
            },
            "client": web
        }
        return self.excute(method)
        

    def getGroupAdmins(self, chat_id):
        method = {
            "method":"getGroupAdminMembers",
            "input":{
                "group_guid":chat_id
            },
            "client": android
        }
        return self.excute(method)
        

    def getChannelInfo(self, channel_guid):
        method = {
            "method":"getChannelInfo",
            "input":{
                "channel_guid":channel_guid
            },
            "client": android
        }
        return self.excute(method)
        

    def addAddressBook(self, first_num, last_num, numberPhone):
        method = {
            "method":"addAddressBook",
            "input":{
                "first_name":first_num,
                "last_name":last_num,
                "phone":numberPhone
            },
            "client": android
        }
        return self.excute(method)


    def getMessagesInfo(self, chat_id, message_ids):
        method = {
            "method":"getMessagesByID",
            "input":{
                "object_guid": chat_id,
                "message_ids": message_ids
            },
            "client": android
        }
        return self.excute(method).get("data").get("messages")


    def getMessages_info_android(self, chat_id, message_ids):
        method = {
            "method":"getMessagesByID",
            "input":{
                "message_ids": message_ids,
                "object_guid": chat_id
            },
            "client": android
        }
        return self.excute(method).get("data").get("messages")


    def setMembersAccess(self, chat_id, access_list):
        method = {
            "method":"setGroupDefaultAccess",
            "input":{
                "access_list": access_list,
                "group_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def getGroupMembers(self, chat_id, start_id=None):
        method = {
            "method":"getGroupAllMembers",
            "input":{
                "group_guid": chat_id,
                "start_id": start_id
            },
            "client": web
        }
        return self.excute(method)


    def getGroupLink(self, chat_id):
        method = {
            "method":"getGroupLink",
            "input":{
                "group_guid":chat_id
            },
            "client": web
        }
        return self.excute(method).get("data").get("join_link")


    def getChannelLink(self, chat_id):
        method = {
            "method":"getChannelLink",
            "input":{
                "group_guid":chat_id
            },
            "client": android
        }
        return self.excute(method).get("data").get("join_link")


    def changeGroupLink(self, chat_id):
        method = {
            "method":"setGroupLink",
            "input":{
                "group_guid": chat_id
            },
            "client": android
        }
        return self.excute(method).get("data").get("join_link")


    def changeChannelLink(self, chat_id):
        method = {
            "method":"setChannelLink",
            "input":{
                "channel_guid": chat_id
            },
            "client": android
        }
        return self.excute(method).get("data").get("join_link")


    def setGroupTimer(self, chat_id, time):
        method = {
            "method":"editGroupInfo",
            "input":{
                "group_guid": chat_id,
                "slow_mode": time,
                "updated_parameters":["slow_mode"]
            },
            "client": android
        }
        return self.excute(method)
        
        
    def setGroupAdmin(self, chat_id, user_id):
        method = {
            "method":"setGroupAdmin",
            "input":{
                "group_guid": chat_id,
                "access_list":["PinMessages","DeleteGlobalAllMessages","BanMember","SetMemberAccess"],
                "action": "SetAdmin",
                "member_guid": user_id
            },
            "client": android
        }
        return self.excute(method)


    def deleteGroupAdmin(self,group_guid,user_id):
        method = {
            "method":"setGroupAdmin",
            "input":{
                "group_guid": group_guid,
                "action": "UnsetAdmin",
                "member_guid": user_id
            },
            "client": android
        }
        return self.excute(method)


    def setChannelAdmin(self, chat_id, user_id, access_list=[]):
        method = {
            "method":"setGroupAdmin",
            "input":{
                "group_guid": chat_id,
                "access_list": access_list,
                "action": "SetAdmin",
                "member_guid": user_id
            },
            "client": android
        }
        return self.excute(method)


    def getStickersByEmoji(self,emojee):
        method = {
            "method":"getStickersByEmoji",
            "input":{
                "emoji_character": emojee,
                "suggest_by": "All"
            },
            "client": web
        }
        return self.excute(method).get("data").get("stickers")


    def setActionChatun(self,guid):
        method = {
            "method":"setActionChat",
            "input":{
                "action": "Unmute",
                "object_guid": guid
            },
            "client": android
        }
        return self.excute(method)


    def setActionChatmut(self,guid):
        method = {
            "method":"setActionChat",
            "input":{
                "action": "Mute",
                "object_guid": guid
            },
            "client": android
        }
        return self.excute(method)


    def sendPoll(self,guid,SOAL,LIST):
        method = {
            "method":"createPoll",
            "input":{
                "allows_multiple_answers": "false",
                "is_anonymous": "true",
                "object_guid": guid,
                "options":LIST,
                "question":SOAL,
                "rnd":f"{randint(100000,999999999)}",
                "type":"Regular"
            },
            "client": android
        }
        return self.excute(method)


    def forwardMessages(self, From, message_ids, to):
        method = {
            "method":"forwardMessages",
            "input":{
                "from_object_guid": From,
                "message_ids": message_ids,
                "rnd": f"{randint(100000,999999999)}",
                "to_object_guid": to
            },
            "client": android
        }
        return self.excute(method)


    def chatGroupvisit(self,guid,visiblemsg):
        method = {
            "method":"editGroupInfo",
            "input":{
                "chat_history_for_new_members": "Visible",
                "group_guid": guid,
                "updated_parameters": visiblemsg
            },
            "client": android
        }
        return self.excute(method)


    def chatGrouphidden(self,guid,hiddenmsg):
        method = {
            "method":"editGroupInfo",
            "input":{
                "chat_history_for_new_members": "Hidden",
                "group_guid": guid,
                "updated_parameters": hiddenmsg
            },
            "client": android
        }
        return self.excute(method)


    def pin(self, chat_id, message_id):
        method = {
            "method":"setPinMessage",
            "input":{
                "action":"Pin",
                "message_id": message_id,
                "object_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def unpin(self, chat_id, message_id):
        method = {
            "method":"setPinMessage",
            "input":{
                "action":"Unpin",
                "message_id": message_id,
                "object_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def logout(self):
        method = {
            "method":"logout",
            "input":{},
            "client": android
        }
        return self.excute(method)


    def joinGroup(self, link):
        hashLink = link.split("/")[-1]
        method = {
            "method":"joinGroup",
            "input":{
                "hash_link": hashLink
            },
            "client": android
        }
        return self.excute(method)


    def joinChannelByLink(self, link):
        hashLink = link.split("/")[-1]
        method = {
            "method":"joinChannelByLink",
            "input":{
                "hash_link": hashLink
            },
            "client": android
        }
        return self.excute(method)


    def deleteChatHistory(self, chat_id, msg_id):
        method = {
            "method":"deleteChatHistory",
            "input":{
                "last_message_id": msg_id,
                "object_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)
        

    def leaveGroup(self,chat_id):
        if "https://" in chat_id:
            guid = Client.joinGroup(self,chat_id)["data"]["group"]["group_guid"]
        else:
            guid = chat_id

        method = {
            "method":"leaveGroup",
            "input":{
                "group_guid": guid
            },
            "client": android
        }
        return self.excute(method)


    def editnameGroup(self,groupgu,namegp,biogp=None):
        method = {
            "method":"editGroupInfo",
            "input":{
                "description": biogp,
                "group_guid": groupgu,
                "title":namegp,
                "updated_parameters":["title","description"]
            },
            "client": android
        }
        return self.excute(method)


    def editbioGroup(self,groupgu,biogp,namegp=None):
        method = {
            "method":"editGroupInfo",
            "input":{
                "description": biogp,
                "group_guid": groupgu,
                "title":namegp,
                "updated_parameters":["title","description"]
            },
            "client": android
        }
        return self.excute(method)


    def joinChannelByID(self, chat_id:str):
        id = chat_id.split("@")[-1]
        guid = Client.getInfoByUsername(self,id)["data"]["channel"]["channel_guid"]
        method = {
            "method":"joinChannelAction",
            "input":{
                "action": "Join",
                "channel_guid": guid
            },
            "client": android
        }
        return self.excute(method)


    def LeaveChannel(self,chat_id):
        if "https://" in chat_id:
            guid = Client.joinChannelByLink(self,chat_id)["data"]["group"]["channel_guid"]
        else:
            guid = chat_id

        method = {
            "method":"joinChannelAction",
            "input":{
                "action": "Leave",
                "channel_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def block(self, chat_id):
        method = {
            "method":"setBlockUser",
            "input":{
                "action": "Block",
                "user_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def unblock(self, chat_id):
        method = {
            "method":"setBlockUser",
            "input":{
                "action": "Unblock",
                "user_guid": chat_id
            },
            "client": android
        }
        return self.excute(method)


    def getChannelMembers(self, channel_guid, text=None, start_id=None):
        method = {
            "method":"getChannelAllMembers",
            "input":{
                "channel_guid":channel_guid,
                "search_text":text,
                "start_id":start_id,
            },
            "client": android
        }
        return self.excute(method)


    def startVoiceChat(self, chat_id):
        method = {
            "method":"createGroupVoiceChat",
            "input":{
                "chat_guid":chat_id
            },
            "client": web
        }
        return self.excute(method)


    def editVoiceChat(self,chat_id,voice_chat_id, title):
        method = {
            "method":"setGroupVoiceChatSetting",
            "input":{
                "chat_guid":chat_id,
                "voice_chat_id" : voice_chat_id,
                "title" : title ,
                "updated_parameters": ["title"]
            },
            "client": web
        }
        return self.excute(method)


    def getUserInfo(self, chat_id):
        method = {
            "method":"getUserInfo",
            "input":{
                "user_guid":chat_id
            },
            "client": web
        }
        return self.excute(method)


    def finishVoiceChat(self, chat_id, voice_chat_id):
        method = {
            "method":"discardGroupVoiceChat",
            "input":{
                "chat_guid":chat_id,
                "voice_chat_id" : voice_chat_id
            },
            "client": web
        }
        return self.excute(method)


    def getChatsUpdate(self):
        time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
        method = {
            "method":"getChatsUpdates",
            "input":{
                "state":time_stamp,
            },
            "client": web
        }
        return self.excute(method).get('data').get('chats')


    def getMessagesChats(self, start_id=None):
        time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
        method = {
            "method":"getChats",
            "input":{
                "start_id":start_id
            },
            "client": web
        }
        return self.excute(method).get('data').get('chats')


    def SeeGroupBylink(self,link_gh):
        method = {
            "method":"groupPreviewByJoinLink",
            "input":{
                "hash_link": link_gh
            },
            "client": web
        }
        return self.excute(method).get("data")
        

    def _requestSendFile(self, file):
        method = {
            "method":"requestSendFile",
            "input":{
                "file_name": str(file.split("/")[-1]),
                "mime": file.split(".")[-1],
                "size": Path(file).stat().st_size
            },
            "client": web
        }
        return self.excute(method).get("data")


    def Devices_rubika(self):
        method = {
            "method":"getMySessions",
            "input":{

            },
            "client": android
        }
        return self.excute(method)


    def addFolder(self, Name = "Arsein", include_chat = None,include_object = None ,exclude_chat = None,exclude_object = None):
        method = {
            "method":"addFolder",
            "input":{
                "exclude_chat_types": exclude_chat,
                "exclude_object_guids": exclude_object,
                "include_chat_types": include_chat,
                "include_object_guids": include_object,
                "is_add_to_top":True,
                "name": Name
            },
            "client": web
        }
        return self.excute(method)


    def deleteFolder(self,folder_id):
        method = {
            "method":"deleteFolder",
            "input":{
                "folder_id": folder_id
            },
            "client": web
        }
        return self.excute(method)


    def addChannel(self,title,typeChannell,bio,guidsUser = None):
        method = {
            "method":"addChannel",
            "input":{
                "addChannel": typeChannell,
                "description": bio,
                "member_guids": guidsUser,
                "title": title,
            },
            "client": web
        }
        return self.excute(method)


    def addGroup(self,title,guidsUser = None):
        method = {
            "method":"addGroup",
            "input":{
                "member_guids": guidsUser,
                "title": title
            },
            "client": web
        }
        return self.excute(method)


    def breturn(self,start_id = None):
        method = {
            "method":"getBreturnUsers",
            "input":{
                "start_id": start_id
            },
            "client": web
        }
        return self.excute(method).get("data").get("abs_users")


    def CountOnline(self,guid):
        method = {
            "method":"getGroupOnlineCount",
            "input":{
                "group_guid": guid
            },
            "client": android
        }
        return self.excute(method).get('data').get('online_count')


    def editUser(self,first_name = None,last_name = None,bio = None):
        method = {
            "method":"updateProfile",
            "input":{
                "bio": bio,
                "first_name": first_name,
                "last_name": last_name,
                "updated_parameters":["first_name","last_name","bio"]
            },
            "client": web
        }
        return self.excute(method)


    def editusername(self,username):
        method = {
            "method":"updateUsername",
            "input":{
                "username": username
            },
            "client": web
        }
        return self.excute(method)


    def ProfileEdit(self,first_name = None,last_name = None,bio = None,username = None):
        while 1:
            try:
                Client.editUser(self,first_name = first_name,last_name = last_name,bio = bio)
                Client.editusername(self,username)
                ok = "ok"
                break
                return ok
            except:continue


    def getChatGroup(self,guid_gap):
        while 1:
            try:
                lastmessages = Client.getGroupInfo(self, guid_gap)["data"]["chat"]["last_message_id"]
                messages = Client.getMessages(self, guid_gap, lastmessages)
                return messages
                break
            except:
                continue


    def getChatChannel(self,guid_ch):
        while 1:
            try:
                lastmessages = Client.getChannelInfo(self, guid_ch)["data"]["chat"]["last_message_id"]
                messages = Client.getMessages(self, guid_ch, lastmessages)
                return messages
                break
            except:
                continue
                
    @staticmethod
    def tmp_rubik():
        tmp_session = ""
        choices = [*"abcdefghijklmnopqrstuvwxyz0123456789"]
        for i in range(32): tmp_session += choice(choices)
        return tmp_session

    def SendCodeSMS(self,phonenumber):
        tmp = Client.tmp_rubik()
        enc = encoderjson(tmp)
        method = {
            "method":"sendCode",
            "input":{
                "phone_number":f"98{phonenumber[1:]}",
                "send_type":"SMS"
            },
            "client": web
        }
        return self.excute(method)


    def GetCodeSMS(self,phonenumber):
        tmp = Client.tmp_rubik()
        enc = encoderjson(tmp)
        method = {
            "method":"sendCode",
            "input":{
                "phone_number":f"98{phonenumber[1:]}",
                "send_type":"Internal"
            },
            "client": android
        }
        return self.excute(method)


    def Send_Code_pass(self,phone_number:str,pass_you=None):
        tmp = Client.tmp_rubik()
        enc = encoderjson(tmp)
        method = {
            "method":"sendCode",
            "input":{
                "pass_key":pass_you,
                "phone_number": f"98{phone_number[1:]}",
                "send_type":'SMS'
            },
            "client": web
        }
        return self.excute(method)


    def getServiceInfo(self, guid):
        method = {
            "method":"getServiceInfo",
            "input":{
                "service_guid": guid
            },
            "client": web
        }
        return self.excute(method)


    def ClearAccounts(self):
        method = {
            "method":"terminateOtherSessions",
            "input":{},
            "client": web
        }
        return self.excute(method)


    def HidePhone(self,**kwargs):
        method = {
            "method":"setSetting",
            "input": {
                "settings": kwargs,
                "update_parameters":["show_my_phone_number"]
            },
            "client": web
        }
        return self.excute(method)


    def HideOnline(self,**kwargs):
        method = {
            "method":"setSetting",
            "input": {
                "settings": kwargs,
                "update_parameters":["show_my_last_online"]
            },
            "client": web
        }
        return self.excute(method)


    def Postion(self,ChG,guiduser):
        method = {
            "method":"requestChangeObjectOwner",
            "input": {
                "object_guid": ChG,
                "new_owner_user_guid": guiduser
            },
            "client": android
        }
        return self.excute(method)


    def getPostion(self,guid):
        method = {
            "method":"getPendingObjectOwner",
            "input": {
                "object_guid": guid
            },
            "client": android
        }
        return self.excute(method)


    def twolocks(self,ramz,hide):
        method = {
            "method":"setupTwoStepVerification",
            "input": {
                "hint": hide,
                "password": ramz
            },
            "client": web
        }

        while 1:
            try:
                loop = asyncio.get_event_loop()
                locked = loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_Message,self.Auth,method))).get("data_enc")))
                if locked["status"] == 'ERROR_GENERIC':#
                    return locked["client_show_message"]["link"]["alert_data"]["message"]
                    break
                else:
                    return locked
                    break
            except: continue


    def Search_in_account(self,text):
        method = {
            "method":"searchGlobalMessages",
            "input": {
                "search_text": text,
                "start_id": 0,
                "type": "Text"
            },
            "client": web
        }

        while 1:
            try:
                loop = asyncio.get_event_loop()
                getsearchm = self.excute(method).get("data").get("messages")
                for s in getsearchm:
                    return s
                    break
            except: continue


    def Search_in_rubika(self,text):
        method = {
            "method":"searchGlobalObjects",
            "input": {
                "search_text": text
            },
            "client": web
        }
        return self.excute(method)


    def votePoll(self,votePoll):
        method = {
            "method":"votePoll",
            "input": {
                "poll_id": votePoll,
                "selection_index": 0
            },
            "client": web
        }
        return self.excute(method)


    def getAbsObjects(self,guids):
        method = {
            "method":"getAbsObjects",
            "input": {
                "objects_guids": guids
            },
            "client": web
        }
        return self.excute(method)


    def getLinkFromAppUrl(self,linkpost):
        method = {
            "method":"getLinkFromAppUrl",
            "input": {
                "app_url": linkpost
            },
            "client": web
        }
        return self.excute(method).get("data").get("link").get("open_chat_data")


    def getContactsLastOnline(self,user_guids:list):
        method = {
            "method":"getContactsLastOnline",
            "input": {
                "user_guids": user_guids
            },
            "client": web
        }
        return self.excute(method)


    def getChatAds(self):
        time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
        method = {
            "method":"getChatAds",
            "input": {
                "state": time_stamp
            },
            "client": web
        }
        return self.excute(method)


    def Sign_messageChannel(self,guidchannel,sing):
        method = {
            "method":"editChannelInfo",
            "input": {
                "channel_guid": guidchannel,
                "sign_messages": sing,
                "updated_parameters": ["sign_messages"]
            },
            "client": web
        }
        return self.excute(method)


    def changeChannel_ID(self,guidchannel,username):
        method = {
            "method":"updateChannelUsername",
            "input": {
                "channel_guid": guidchannel,
                "username": username
            },
            "client": web
        }
        return self.excute(method)
        
#Files 
    def _uploadFile(self, file):
        if not "http" in file:
            REQUES = Client._requestSendFile(self, file)
            bytef = open(file,"rb").read()

            hash_send = REQUES["access_hash_send"]
            file_id = REQUES["id"]
            url = REQUES["upload_url"]

            header = {
                'auth':self.Auth,
                'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
                'chunk-size':str(Path(file).stat().st_size),
                'file-id':str(file_id),
                'access-hash-send':hash_send,
                "content-type": "application/octet-stream",
                "content-length": str(Path(file).stat().st_size),
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.1"
            }

            if len(bytef) <= 131072:
                header["part-number"], header["total-part"] = "1","1"

                while True:
                    try:
                        loop = asyncio.get_event_loop()
                        j = loop.run_until_complete(httpfiles(url,bytef,header))
                        j = loads(j)['data']['access_hash_rec']
                        break
                    except Exception as e:
                        continue

                return [REQUES, j]
            else:
                t = round(len(bytef) / 131072 + 1)
                for i in range(1,t+1):
                    if i != t:
                        k = i - 1
                        k = k * 131072
                        while True:
                            try:
                                header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
                                loop = asyncio.get_event_loop()
                                o = loop.run_until_complete(httpfiles(url,bytef[k:k + 131072],header))
                                o = loads(o)['data']
                                break
                            except Exception as e:
                                continue
                    else:
                        k = i - 1
                        k = k * 131072
                        while True:
                            try:
                                header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
                                loop = asyncio.get_event_loop()
                                p = loop.run_until_complete(httpfiles(url,bytef[k:],header))
                                p = loads(p)['data']['access_hash_rec']
                                break
                            except Exception as e:
                                continue
                        return [REQUES, p]
        else:
            REQUES = {
                "method":"requestSendFile",
                "input":{
                    "file_name": file.split("/")[-1],
                    "mime": file.split(".")[-1],
                    "size": len(get(file).content)
            },
            "client": web
        }

        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,REQUES))).get("data_enc"))).get("data")
                break
            except: continue

            hash_send = REQUES["access_hash_send"]
            file_id = REQUES["id"]
            url = REQUES["upload_url"]
            bytef = get(file).content

            header = {
                'auth':self.Auth,
                'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
                'chunk-size':str(len(get(file).content)),
                'file-id':str(file_id),
                'access-hash-send':hash_send,
                "content-type": "application/octet-stream",
                "content-length": str(len(get(file).content)),
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.1"
            }

            if len(bytef) <= 131072:
                header["part-number"], header["total-part"] = "1","1"

                while True:
                    try:
                        loop = asyncio.get_event_loop()
                        j = loop.run_until_complete(httpfiles(url,bytef,header))
                        j = loads(j)['data']['access_hash_rec']
                        break
                    except Exception as e:
                        continue

                return [REQUES, j]
            else:
                t = round(len(bytef) / 131072 + 1)
                for i in range(1,t+1):
                    if i != t:
                        k = i - 1
                        k = k * 131072
                        while True:
                            try:
                                header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
                                loop = asyncio.get_event_loop()
                                o = loop.run_until_complete(httpfiles(url,bytef[k:k + 131072],header))
                                o = loads(o)['data']
                                break
                            except Exception as e:
                                continue
                    else:
                        k = i - 1
                        k = k * 131072
                        while True:
                            try:
                                header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
                                loop = asyncio.get_event_loop()
                                p = loop.run_until_complete(httpfiles(url,bytef[k:],header))
                                p = loads(p)['data']['access_hash_rec']
                                break
                            except Exception as e:
                                continue
                        return [REQUES, p]

    @staticmethod
    def _getImageSize(image_bytes:bytes):
        import io, PIL.Image
        im = PIL.Image.open(io.BytesIO(image_bytes))
        width, height = im.size
        return [width , height]

    def uploadAvatar_replay(self,myguid,files_ide):
        method = {
            "method":"uploadAvatar",
            "input":{
                "object_guid":myguid,
                "thumbnail_file_id":files_ide,
                "main_file_id":files_ide
            },
            "client": web
        }
        return self.excute(method)

    def uploadAvatar(self,myguid,main,thumbnail=None):
        mainID = str(Client._uploadFile(self, main)[0]["id"])
        thumbnailID = str(Client._uploadFile(self, thumbnail or main)[0]["id"])
        method = {
            "method":"uploadAvatar",
            "input":{
                "object_guid":myguid,
                "thumbnail_file_id":thumbnailID,
                "main_file_id":mainID
            },
            "client": web
        }
        return self.excute(method)
        
    def deleteAvatar(self,myguid,avatar_id):
        method = {
            "method":"deleteAvatar",
            "input":{
                "object_guid":myguid,
                "avatar_id":avatar_id
            },
            "client": web
        }
        return self.excute(method)
                
    def sendsticker(self,guid,emoji,w_h_rati,sticker_id,file_id,access_hash,set_id):
        method = {
            "method": "sendMessage",
            "input": {
                "object_guid": guid,
                "rnd": f"{randint(100000,999999999)}",
                "sticker": {
                  "emoji_character": emoji,
                  "w_h_ratio": w_h_rati,
                  "sticker_id": sticker_id,
                  "file": {
                    "file_id": file_id,
                    "mime": "png",
                    "dc_id": 32,
                    "access_hash_rec": access_hash,
                    "file_name": "sticker.png"
                  },
                  "sticker_set_id": set_id
                }
            },
            "client": android
        }
        return self.excute(method)
        

    def sendDocument(self, chat_id, file, caption=None, message_id=None):
        uresponse = Client._uploadFile(self, file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

        inData = {
            "method":"sendMessage",
            "input":{
                "object_guid":chat_id,
                "reply_to_message_id":message_id,
                "rnd":f"{randint(100000,999999999)}",
                "file_inline":{
                    "dc_id":str(dc_id),
                    "file_id":str(file_id),
                    "type":"File",
                    "file_name":file_name,
                    "size":size,
                    "mime":mime,
                    "access_hash_rec":access_hash_rec
                }
            },
            "client": web
        }

        if caption != None: inData["input"]["text"] = caption


        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue


    def sendDocument_rplay(self,chat_id,file_id,mime,dc_id,access_hash_rec,file_name,size,caption=None,message_id=None):
        inData = {
            "method":"sendMessage",
            "input":{
                "object_guid":chat_id,
                "reply_to_message_id":message_id,
                "rnd":f"{randint(100000,999999999)}",
                "file_inline":{
                    "dc_id":str(dc_id),
                    "file_id":str(file_id),
                    "type":"File",
                    "file_name":file_name,
                    "size":size,
                    "mime":mime,
                    "access_hash_rec":access_hash_rec
                }
            },
            "client": web
        }

        if caption != None: inData["input"]["text"] = caption


        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue


    def sendVoice(self, chat_id, file, time, caption=None, message_id=None):
        uresponse = Client._uploadFile(self, file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

        inData = {
                "method":"sendMessage",
                "input":{
                    "file_inline": {
                        "dc_id": dc_id,
                        "file_id": file_id,
                        "type":"Voice",
                        "file_name": file_name,
                        "size": size,
                        "time": time,
                        "mime": mime,
                        "access_hash_rec": access_hash_rec,
                    },
                    "object_guid":chat_id,
                    "rnd":f"{randint(100000,999999999)}",
                    "reply_to_message_id":message_id
                },
                "client": web
            }

        if caption != None: inData["input"]["text"] = caption


        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue

    def sendGif(self, chat_id, file, caption=None, message_id=None, thumbnail=None):
        uresponse = Client._uploadFile(self, file)
        if thumbnail == None: thumbnail = r"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACAWGBwYFCAcGhwkIiAmMFA0MCwsMGJGSjpQdGZ6eHJm\ncG6AkLicgIiuim5woNqirr7EztDOfJri8uDI8LjKzsb/2wBDASIkJDAqMF40NF7GhHCExsbGxsbG\nxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsb/wAARCAAyADIDASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDXqCXo\nasVXk70DKwHNSBaRRzUgrnZqMUfMKtkcCq24KcmntdxgDmtIEyJ8UVB9ti9aKskmB4qJ/uk1L2qC\nZtsZpiII5P3hB6VDLOySZ7UyVJDEWWoXLGD5uoqFHQtvUnln3rkVB5bv3qqk3Y1filUKM09kCV2R\nfZ39aKtectFK7K5URwagzrila4klcJiqdtbsrA5q+jLE4ZhVXsyErq5bCFYAMVQuVYKVC9av/akc\ncGmy4ZeKaIaZgeWVlANX1jDKKbdRYYNQJQqdamRpAk8pfWiq/n+9FSWPtifM61LcdKKKctyIbEMJ\nO4c1oj7lFFUiWQXH+qNZLmiihjiNzRRRUlH/2Q==\n"
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        size = str(len(get(file).content if "http" in file else open(file,"rb").read()))
        time =  round(TinyTag.get(file).duration * 1000)

        inData = {
                "method":"sendMessage",
                "input":{
                    "file_inline": {
                        "access_hash_rec":access_hash_rec,
                        "auto_play":False,
                        "dc_id":dc_id,
                        "file_id":file_id,
                        "file_name":file_name,
                        "height":360,
                        "mime":mime,
                        "size":size,
                        "thumb_inline":thumbnail,
                        "time":time,
                        "type":"Gif",
                        "width":360,
                    },
                    "is_mute":False,
                    "object_guid":chat_id,
                    "rnd":f"{randint(100000,999999999)}",
                    "reply_to_message_id":message_id
                },
                "client": android
            }

        if caption != None: inData["input"]["text"] = caption


        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue

    def sendVideo(self, chat_id, file, caption=None, message_id=None):
        uresponse = Client._uploadFile(self, file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        size = str(len(get(file).content if "http" in file else open(file,"rb").read()))
        time =  round(TinyTag.get(file).duration * 1000)

        inData = {
                "method":"sendMessage",
                "input":{
                    "file_inline": {
                        "access_hash_rec":access_hash_rec,
                        "auto_play":False,
                        "dc_id":dc_id,
                        "file_id":file_id,
                        "file_name":file_name,
                        "height":360,
                        "mime":mime,
                        "size":size,
                        "thumb_inline":file,
                        "time":time,
                        "type":"Video",
                        "width":360,
                    },
                    "is_mute":False,
                    "object_guid":chat_id,
                    "rnd":f"{randint(100000,999999999)}",
                    "reply_to_message_id":message_id
                },
                "client": android
            }

        if caption != None: inData["input"]["text"] = caption


        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue


    def sendPhoto(self, chat_id, file, size=[], thumbnail=None, caption=None, message_id=None):
        uresponse = Client._uploadFile(self, file)
        if thumbnail == None: thumbnail = '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'
        elif "." in thumbnail:thumbnail = str(Client._getThumbInline(open(file,"rb").read() if not "http" in file else get(file).content))

        if size == []: size = encoder_photo.getThumbInline(open(file,"rb").read() if not "http" in file else get(file).content)

        file_inline = {
            "dc_id": uresponse[0]["dc_id"],
            "file_id": uresponse[0]["id"],
            "type":"Image",
            "file_name": file.split("/")[-1],
            "size": str(len(get(file).content if "http" in file else open(file,"rb").read())),
            "mime": file.split(".")[-1],
            "access_hash_rec": uresponse[1],
            "width": size[0],
            "height": size[1],
            "thumb_inline": thumbnail
        }

        inData = {
                "method":"sendMessage",
                "input":{
                    "file_inline": file_inline,
                    "object_guid": chat_id,
                    "rnd": f"{randint(100000,999999999)}",
                    "reply_to_message_id": message_id
                },
                "client": web
            }
        if caption != None: inData["input"]["text"] = caption

        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue

    def sendMusic(self, chat_id, file, time, caption=None, message_id=None):
        uresponse = Client._uploadFile(self, file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

        inData = {
                "method":"sendMessage",
                "input":{
                    "file_inline": {
                        "dc_id": dc_id,
                        "file_id": file_id,
                        "type":"Music",
                        "music_performer":"",
                        "file_name": file_name,
                        "size": size,
                        "time": time,
                        "mime": mime,
                        "access_hash_rec": access_hash_rec,
                    },
                    "object_guid":chat_id,
                    "rnd":f"{randint(100000,999999999)}",
                    "reply_to_message_id":message_id
                },
                "client": android
            }

        if caption != None: inData["input"]["text"] = caption

        while 1:
            try:
                loop = asyncio.get_event_loop()
                return loads(self.enc.decrypt(loads(loop.run_until_complete(http(Client.server_files,self.Auth,inData))).get("data_enc")))
                break
            except: continue