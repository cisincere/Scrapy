class Replay():
    def __init__(self):
        self.rpid = 0
        self.oid = 0
        self.type = 0
        self.mid = 0
        self.root = 0
        self.parent = 0
        self.dialog = 0
        self.count = 0
        self.rcount = 0
        self.state = 0
        self.fansgrade = 0
        self.attr = 0
        self.ctime = 0
        self.rpid_str = ''
        self.root_str = ''
        self.parent_str = ''
        self.like = 0
        self.action = 0
        self.assist = 0
        self.invisible = False
        self.dynamic_id_str = ''
        self.member = None
        self.content = None
        self.up_action = None
        self.reply_control = None
        self.folder = None

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            if key == 'member':
                member = Member()
                member.analyze_json(json['member'])
                self.member = member
                continue
            if 'content' == key:
                content = Content()
                content.analyze_json(json['content'])
                self.content = content
                continue
            if key == 'up_action':
                up_action = UpAction()
                up_action.analyze_json(json['up_action'])
                self.up_action = up_action
                continue
            if key == 'reply_control':
                reply_control = ReplyControl()
                reply_control.analyze_json(json['reply_control'])
                self.reply_control = reply_control
                continue
            if key == 'folder':
                folder = Folder()
                folder.analyze_json(json['folder'])
                self.folder = folder
                continue
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:

        return '    {' + f"""
        "rpid":{self.rpid},
        "oid":{self.oid},
        "type":{self.type},
        "mid":{self.mid},
        "root":{self.root},
        "parent":{self.parent},
        "dialog":{self.dialog},
        "count":{self.count},
        "rcount":{self.rcount},
        "state":{self.state},
        "fansgrade":{self.fansgrade},
        "attr":{self.attr},
        "ctime":{self.ctime},
        "rpid_str":'{self.rpid_str}',
        "root_str":'{self.root_str}',
        "parent_str":'{self.parent_str}',
        "like":{self.like},
        "action":{self.action},
        "assist":{self.assist},
        "invisible":{self.invisible},
        "dynamic_id_str":'{self.dynamic_id_str}',
        "member":{self.member},
        "content":{self.content},
        "up_action":{self.up_action},
        "reply_control":{self.reply_control},
        "folder":{self.folder}
        """ + '}'


class Member(object):
    def __init__(self):
        self.mid = ''
        self.uname = ''
        self.sex = ''
        self.sign = ''
        self.avatar = ''
        self.rank = ''
        self.face_nft_new = 0
        self.is_senior_member = 0
        self.senior = {},
        self.level_info = {},
        self.pendant = {},
        self.nameplate = {},
        self.official_verify = {},
        self.vip = {},
        self.fans_detail = None,
        self.user_sailing = {},
        self.is_contractor = False,
        self.contract_desc = '',
        self.nft_interaction = None,
        self.avatar_item = {},

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:
        return '{' + f"""
        "mid" : '{self.mid}',
        "uname" : '{self.uname}',
        "sex" : '{self.sex}',
        "sign" : '{self.sign}',
        "avatar" : '{self.avatar}',
        "rank" : '{self.rank}',
        "face_nft_new": {self.face_nft_new},
        "is_senior_member": {self.is_senior_member},
        "senior" : {self.senior},
        "level_info" : {self.level_info},
        "pendant" : {self.pendant},
        "nameplate" : {self.nameplate},
        "official_verify" : {self.official_verify},
        "vip" : {self.vip},
        "fans_detail"  : {self.fans_detail},
        "user_sailing" : {self.user_sailing},
        "is_contractor" : {self.is_contractor},
        "contract_desc" : '{self.contract_desc}',
        "nft_interaction" : {self.nft_interaction},
        "avatar_item" : {self.avatar_item}
        """ + '}'


class Content(object):
    def __init__(self):
        self.message = ''
        self.members = []
        self.emote = {}
        self.jump_url = {}
        self.max_line = 0

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:
        return '{' + \
            '"message" : "' + self.message + '",' + \
            '"members" :  "' + str(self.members) + '",' + \
            '"emote" :  "' + str(self.emote) + '",' + \
            '"jump_url" : "' + str(self.jump_url) + '",' + \
            '"max_line":  ' + str(self.max_line) + ',' + \
            '}'


class UpAction(object):
    def __init__(self):
        self.like = False
        self.reply = False

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:
        return ' {' + f"""
            "like": {self.like},
            "reply": {self.reply}
        """ + '}'


class ReplyControl(object):
    def __init__(self):
        self.max_line = 0,
        self.sub_reply_entry_text = ''
        self.sub_reply_title_text = ''
        self.time_desc = ''
        self.location = ''
        self.fold_pictures = True

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:
        return '{' + f"""
        "max_line": {self.max_line},
        "sub_reply_entry_text": '{self.sub_reply_entry_text}',
        "sub_reply_title_text": '{self.sub_reply_title_text}',
        "time_desc": '{self.time_desc}',
        "location": '{self.location}',
        "fold_pictures": {self.fold_pictures}
        """ + '        }'


class Folder(object):
    def __init__(self):
        self.has_folde = False,
        self.is_folded = False,
        self.rule = ''

    def analyze_json(self, json):
        for key in self.__dict__.keys():
            self.__setattr__(key, json.get(key))

    def __str__(self) -> str:
        return '{' + f"""
        "has_folde": {self.has_folde},
        "is_folded": {self.is_folded},
        "rule": {self.rule}
        """ + '}'
