class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        while '()' in command or '(al)' in command:
            command = command.replace('()', "o").replace("(al)", "al")
        return command