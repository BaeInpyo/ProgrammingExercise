"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3362/
"""

import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4_chunk = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
        ipv4_regex = "^" + r"\.".join([ipv4_chunk]*4) + "$"
        ipv6_chunk = r"([0-9a-fA-F]{1,4})"
        ipv6_regex = "^" + r"\:".join([ipv6_chunk]*8) + "$"

        if re.match(ipv4_regex, IP):
            return "IPv4"
        elif re.match(ipv6_regex, IP):
            return "IPv6"
        else:
            return "Neither"