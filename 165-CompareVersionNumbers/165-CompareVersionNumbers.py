# Last updated: 1/12/2026, 1:42:01 PM
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split and strip leading zeros, ensuring empty strings are treated as "0"
        v1_stripped = [int(part.lstrip('0') or '0') for part in version1.split(".")]
        v2_stripped = [int(part.lstrip('0') or '0') for part in version2.split(".")]

        # Compare up to the maximum length of both lists
        max_length = max(len(v1_stripped), len(v2_stripped))

        for i in range(max_length):
            # Get the part value or treat missing parts as 0
            v1 = v1_stripped[i] if i < len(v1_stripped) else 0
            v2 = v2_stripped[i] if i < len(v2_stripped) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
