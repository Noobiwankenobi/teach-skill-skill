from mycroft import MycroftSkill, intent_file_handler


class TeachSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.teach.intent')
    def handle_skill_teach(self, message):
        self.speak_dialog('skill.teach')


def create_skill():
    return TeachSkill()

