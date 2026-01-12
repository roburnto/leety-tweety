# Last updated: 1/12/2026, 1:41:37 PM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def is_letter_log(log):
            return log.split()[1].isalpha()
        
        letter_logs = []
        
        digit_logs = []
        
        for log in logs:
            if is_letter_log(log):
                letter_logs.append(log)
            else:
                digit_logs.append(log)
                
        letter_logs.sort(key = lambda log: (log.split(" ",1)[1], log.split(" ", 1)[0]))
        
        return letter_logs + digit_logs
        