

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.util import LOG

log.info("This is a logged info level message outside of the MycroftSkill class scope")

def my_special_function():
    LOG.info("Another usage of LOG.")
class LoggingSkill(MycroftSkill):
    @intent_handler(IntentBuilder('HelloworldIntent').require('HelloWorld'))
    def handle_hello_world_intent(self, message):

        self.log.info("This is an info level log message.")
        self.speak_dialog("hello.world")
        my_special_function()

def create_skill():
    return LoggingSkill() 


           
class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('r.n.i.t').require('nameKeyword'))
    def handle_thank_you_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("rnit")

    
    @intent_handler(IntentBuilder('joke')
                    .require('j.o.k.e'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
        self.speak_dialog("hello.world")

    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
