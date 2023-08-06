import html

import damv1env as env
import damv1time7 as time7
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStoreTypes

class sanbox():
    def evernote_generate_report(self,_nameof_msg_rpt, _lst_grplines, _tmplt_wrapper):
        try:
            dev_token = env.sandbox_evernote.dev_token._value_.strip()
            client = EvernoteClient(token=dev_token) 
            # - - - - - | prepared new Note
            userStore = client.get_user_store() 
            noteStore = client.get_note_store()
            newtitle = f'Report {time7.currentTime7()}'
            note = Types.Note() 
            note.title =  f'\U0001F4D1 {newtitle}'
            note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">' 
            contexid = str(time7.generate_uuids_byTime7())
            note.content += _tmplt_wrapper.format(\
                value_str_ervnt_rptname = html.escape(_nameof_msg_rpt), \
                value_str_contexid = html.escape(contexid), \
                value_strlst_grplines = ''.join(_lst_grplines)
            )
            # - - - - - | prepared created Note
            created_note = noteStore.createNote(note)
            noteGuid = created_note.guid
            print(time7.currentTime7(),'      Successfully created a new note with ( うまい ):')
            print(time7.currentTime7(),'        GUID: ', noteGuid)
            print(time7.currentTime7(),'        Title ( タイトル ): ', newtitle)
            # - - - - - | prepared shareable Note
            user = userStore.getUser(dev_token).shardId
            shareKey = noteStore.shareNote(dev_token, noteGuid)
            print(time7.currentTime7(),'        Note URL set to clipboard. The note has been shared with the following URL ( リンク ):')
            shareable = "%s/shard/%s/sh/%s/%s" % ("https://sandbox.evernote.com/", user, noteGuid, shareKey)	 
            print(time7.currentTime7(),f'        {shareable}')         
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    